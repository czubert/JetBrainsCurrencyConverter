import json

# write your code here
json_string = input()

py_string = json.loads(json_string)
print(type(py_string))
print(py_string)
