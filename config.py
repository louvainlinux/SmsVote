# to querry the db
prefix = '24h'
table = 'velo'

# to filter the incomming sms
isStrict = False
allowedEntry = ['coucou']

# destination of the index.html
dest = '24h_JuIkfefogs1.html'

# to copy the generated html file to the remote server
local = "./out/index.html"
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
