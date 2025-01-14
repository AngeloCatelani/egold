import json
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
# res = json.loads(test_string)
res = eval(test_string)
print(res)