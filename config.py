# to querry the db
prefix = '24h'
table = 'velo'

vote = [
        {"prefix" : "24h", "table" : "velo", "filtered" : False, "allowedEntry" : ["coucou"]},
        {"prefix": "talent", "table" : "velo", "filtered": False, "allowedEntry": []}
        ]

# to filter the incomming sms
isStrict = False
allowedEntry = ['coucou']

# to copy the generated html file to the remote server
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
