import json

def check_for_all():
    tlist = json.load(open("json/tool_list.json"))

    for tool in tlist:
        check_for(tool)

def check_for(tool_name):
    pass