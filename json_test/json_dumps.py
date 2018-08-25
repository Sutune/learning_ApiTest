import json

data={'id':1,'name':'51zxw','password':'66666'}
print(type(data))

json_str=json.dumps(data)
print(type(json_str))
print(json_str)