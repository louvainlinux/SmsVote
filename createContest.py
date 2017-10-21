#!/usr/bin/python3

# this is installed with
# sudo aptitude install python3-mysql.connector
# pip3 install sshclient paramiko scp


import operator
import os
import paramiko
import scrypt
import config
import sys

import mysql.connector as mariadb

from string import Template
from time import localtime, strftime
from paramiko import SSHClient
from scp import SCPClient


# filter a given vote
def getVote(text, prefix):
    text = text.replace(prefix, '')
    while('  ' in text):
        text = text.replace('  ',' ')
    if text[0] == ' ':
        text = text[1:]
    if text[-1] == ' ':
        text = text[:-1] 
    return text

# read a file and return all of it's content
def readFile(f):
    with open(f, mode='r') as file:
        return file.read()

# write the given content to the given file (erase mode)
def writeFile(f, content):
    try:
        os.remove(f)
    except OSError:
        pass
    with open(f, mode='w+') as file:
        file.write(content)

# generate the result page with the given content (check html/*.template to see how it's structured)
def genPage(content, dest, total, prefix):
    sortedResult = sorted(content.items(), key=operator.itemgetter(1))
    entry = "";
    for (num, nbr) in reversed(sortedResult):
        entryTemplate = Template(readFile(config.path+"html/entry.template"))
        entry+=entryTemplate.substitute(
                title=num, 
                percent=(nbr/total * 100)
            )
        entry+="\n"

    pageTemplate = Template(readFile(config.path+"html/index.template"))
    page = pageTemplate.substitute(
            entry=entry, 
            prefix=prefix, 
            heure=strftime("le %d/%m/%Y à %H:%M:%S", localtime())
        )
    writeFile(dest, page)

# Fetch all the votte from the mariadb and filter them
def getAllVotes(prefix, isStrict, allowedEntry):
    cursor.execute("select TextDecoded from gammu."+prefix)
    
    result = {}

        # parsing the fetched votes
    while(1):
        row = cursor.fetchone ()
        if row == None:
            break
        vote = getVote(row[0], prefix)
        if isStrict and vote not in allowedEntry:
            continue
        if vote in result:
            result[vote] += 1
        else:
            result[vote] = 1
    return result

# send the given page to the remote server
def sendRemote(f, prefix):
    k = paramiko.RSAKey.from_private_key_file(config.rsakey)

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname = 'louvainlinux.org', username = 'sms-vote', pkey = k)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(f, config.remote+''.join(format(x,'02x') for x in scrypt.hash(config.salt+prefix,''))+'.html')
    if debug:
        print("Emplacement of the contest: http://louvainlinux.org/sms-vote/"+''.join(format(x,'02x') for x in scrypt.hash(config.salt+prefix,''))+'.html')

# test if a view with the given name exist, if not, it create it
def checkView(name):
    cursor.execute("SHOW FULL TABLES IN gammu WHERE TABLE_TYPE LIKE 'VIEW';")
    exist = False

    while(1):
        row = cursor.fetchone()
        if row == None:
            break
        if row[0] == name:
            exist = True
            break

    if not exist:
        print("Creating new view: "+name)
        if name == "filter":
            cursor.execute(readFile(config.path+"sql/createFilter.sql"))
        else:
            create = Template(readFile(config.path+'sql/createView.template'))
            cursor.execute(create.substitute(name=name))

# checking if an argment is present
debug = False
if len(sys.argv) > 1:
    debug = True

# init the db
mariadb_connection = mariadb.connect(host=config.db_host, user=config.db_user, password=config.db_pass, database=config.db_db, buffered=True)
cursor = mariadb_connection.cursor()

# check the existence of the filtered view in the db
checkView("filter")

# fetch all the votes
for voteEntry in config.vote:
    # check if the  view need to be generated
    checkView(voteEntry["prefix"])

    # get all the votes for a given prefix
    result = getAllVotes(voteEntry["prefix"], voteEntry["filtered"], voteEntry["allowedEntry"])

    # parse all the votes
    total = 0
    for key in result:
        total += result[key]

    #create the contest page here
    genPage(result, "out/"+voteEntry["prefix"]+".html", total, voteEntry["prefix"])

    #upload to the remote serve the result
    sendRemote("out/"+voteEntry["prefix"]+".html", voteEntry["prefix"])
