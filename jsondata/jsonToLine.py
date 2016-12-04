import json

with open("out.json") as f:
    data = json.load(f)
    #print(data)
    for i in data:
        print (json.dumps(i))
