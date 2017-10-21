# the emplacement of the instalation
path= "/home/pierre/src/voteSMS/"

# the list of all the votes, with their caracteristics
vote = [
        {"prefix" : "folklo", "filtered": True, "allowedEntry": ["1","4","6","8","9","11","12","13","14","15","16","17","18","20","21","22","25","27","28","30","31","32","33","34","36","37","39","42","43","45","50","53","57","59","61","62","64","66","67","68","70","71","74"]}
        ]

# to copy the generated html file to the remote server
remote = "/var/www/louvainlinux/public/sms-vote/"
rsakey = "/home/pierre/.ssh/id_rsa2"
salt = 'yolo'

# to connect to the db
db_host = 'localhost' 
db_user = 'pierre'
db_pass = ''
db_db = 'gammu'
