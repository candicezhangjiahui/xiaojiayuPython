import json
from jsoncompare import jsoncompare as json_comp

json_comp.long = int
json_comp.unicode = str
json_comp.xrange = range



a = [
  {
    "Key": "Name",
    "Value": "node1"
  },
  {
    "Key": "babyr",
    "Value": "jhonson"
  },
  {
    "Key": "managed",
    "Value": "yes"
  }
]

b = [
  {
    "Key": "Name",
    "Value": "node1"
  },
  {
    "Key": "owner",
    "Value": "jhonson"
  },
  {
    "Key": "managed",
    "Value": "No"
  }
]

# Compare respecting each array's order
json_comp.are_same(a, b)

print(json_comp.are_same(a, b)[1])