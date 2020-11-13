import json
a = {"fed":'ef'}
b = {"edf":"fefew"}
a = dict(a,**b)
print(a)
print(b)
print(type(json.dumps(a)))
for i in a:
    print(a[i])
for i in {}:
    print(i)