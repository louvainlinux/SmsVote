#!/usr/bin/python3

# this is installed with
# sudo aptitude install python3-mysql.connector

import operator
import os

import mysql.connector as mariadb
from string import Template
from time import localtime, strftime
import paramiko
from paramiko import SSHClient
from scp import SCPClient

import config

def getVote(text):
    while('  ' in text):
        text = text.replace('  ',' ')
    if text[0] == ' ':
        text = text[1:]
    if text[-1] == ' ':
        text = text[:-1] 
    return text[len(config.prefix)+1:]


def readFile(f):
    with open(f, mode='r') as file:
        return file.read()

def writeFile(f, content):
    try:
        os.remove(f)
    except OSError:
        pass
    with open(f, mode='w+') as file:
        file.write(content)

#count the votes
    # fetch all the votes
mariadb_connection = mariadb.connect(host='localhost', user='pierre', password='', database='gammu')
cursor = mariadb_connection.cursor()
cursor.execute("select TextDecoded from gammu."+config.table)

result = {}

    # parsing the fetched votes
while(1):
    row = cursor.fetchone ()
    if row == None:
        break
    vote = getVote(row[0])
    if config.isStrict and vote not in config.allowedEntry:
        continue
    if vote in result:
        result[vote] += 1
    else:
        result[vote] = 1

total = 0
for key in result:
    total += result[key]

    #create the contest page here
sortedResult = sorted(result.items(), key=operator.itemgetter(1))
entry = "";
for (num, nbr) in reversed(sortedResult):
    entryTemplate = Template(readFile("./html/entry.template"))
    entry+=entryTemplate.substitute(
            title=num, 
            percent=(nbr/total * 100)
        )
    entry+="\n"

pageTemplate = Template(readFile("./html/index.template"))
page = pageTemplate.substitute(
        entry=entry, 
        prefix=config.prefix, 
        heure=strftime("le %d/%m/%Y à %H:%M:%S", localtime())
    )
writeFile("./out/index.html", page)



#upload to the remote serve the result
#pip3 install sshclient paramiko scp

k = paramiko.RSAKey.from_private_key_file(config.rsakey)

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname = 'louvainlinux.org', username = 'sms-vote', pkey = k)

with SCPClient(ssh.get_transport()) as scp:
    scp.put(config.local, config.remote+config.dest)
