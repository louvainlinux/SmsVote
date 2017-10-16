# to querry the db
    # the list of all the votes, with their caracteristics
vote = [
        {"prefix" : "velo", "filtered" : False, "allowedEntry" : ["coucou", "salut"]},
        {"prefix" : "talent", "filtered": False, "allowedEntry": []},
        {"prefix" : "lln", "filtered" : True, "allowedEntry": ["haut", "bas"]}
        ]

# to copy the generated html file to the remote server
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
