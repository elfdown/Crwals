import json


idlist = ['1','2','4','6','7']
for _id in idlist:#对于大类进行循环
    cir = ['1','2','3']
    for __id in cir:#对里边的男女以及其他进行循环
        catid = _id + '00' + __id
        with open("./json/{}.json".format(catid), 'rt') as f:
            cr = json.load(f)
            len_json = len(cr)
            bo = len_json//10

        for i in range(9):
            kv = cr[i*bo:(i+1)*bo]
            print(kv)
            k = i+1
            with open("./partjson/{}_{}.json".format(catid,i), 'w') as f:
                json.dump(kv,f)
                print(i)
                
        kv = cr[9*bo:]
        with open("./partjson/{}_{}.json".format(catid,9), 'w') as f:
            json.dump(kv,f)
            print("all done")
