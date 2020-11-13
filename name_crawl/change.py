import json

with open("name.json","r") as f:
    name_dict = json.load(f)
with open("name.txt","w") as f:
    for name in name_dict.keys():
        f.write("{}\t{}\n".format(name,name_dict[name]))
