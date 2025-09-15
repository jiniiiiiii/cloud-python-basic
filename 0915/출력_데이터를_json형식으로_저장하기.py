import json

Data_list = """[
    ["사과", "포도"],
    [100, 200]
]"""

json_Data_list = json.loads(Data_list)
print(json_Data_list)

strData = json.dumps(json_Data_list)
print(strData)