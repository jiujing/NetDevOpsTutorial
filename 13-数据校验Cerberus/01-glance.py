from cerberus import Validator, schema

schema = {'status':{'type':'string','allowed':['up']}}
v = Validator(schema,allow_unknown=True)

intf = {'name':'Eth1/1','status':'down'}
result = v.validate(intf,schema)
print(result)
print(v.errors)


schema = {'inc':{'type':'integer','min':9,'max':9}}
v = Validator(schema,allow_unknown=True)

intf = {'name':'Eth1/1','status':'up','inc':10}
result = v.validate(intf,schema)
print(result)
print(v.errors)
