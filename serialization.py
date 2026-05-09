import json

data = {"name": "Ram"}

# Serialization
x = json.dumps(data)
print(x)
# Deserialization
y = json.loads(x)
print(y)