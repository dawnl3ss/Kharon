import json
import os
import time

def get_list():
    return json.load(open("src/json/tool_list.json"))

def check_if_exist(tool):
    exist = False

    if exist == False:
        print("└──────⮞ Checking tools... ({})".format(tool))
        #time.sleep(2)
    return exist