# to querry the db
    # the list of all the votes, with their caracteristics
vote = [
        {"prefix" : "24h", "filtered" : False, "allowedEntry" : ["coucou", "salut"]},
        {"prefix": "23h", "filtered": False, "allowedEntry": []}
        ]

# to copy the generated html file to the remote server
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
