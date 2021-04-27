import socket
import json



name = socket.gethostname()
ip = socket.gethostbyname(name)

mjson = {"name ": [name],
         "ip " :[ip]}
with open("mjson.json", "w") as write_file:
    json.dump(mjson, write_file)







