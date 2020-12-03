# -*- coding: iso-8859-1 -*-
import json 
import random
import easygui

json_file = open("whyYouAreAmazing.json")
data = json.load(json_file)
rand = random.randrange(0,13)
grund = data["gründe"][rand]["grund"]
easygui.msgbox(grund, "Du bist toll!!!", ok_button="Okay, ich bin toll")
