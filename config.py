# to querry the db
prefix = '24h'
table = 'velo'

# to filter the incomming sms
isStrict = False
allowedEntry = ['coucou']

# to copy the generated html file to the remote server
local = "./out/index.html"
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
