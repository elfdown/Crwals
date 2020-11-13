import json

with open ("resualt.json","r") as f:
    name_dict = json.load(f)

name_dict=dict(sorted(name_dict.items(),key=lambda x:x[1],reverse=True))

with open("name.json","w") as f:
    json.dump(name_dict,fp=f,ensure_ascii = False, indent = 4)