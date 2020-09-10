import nbtlib
import configparser
from googletrans import Translator
from os import walk

config = configparser.ConfigParser()
config.read("config.ini")
lang = config["ftbquests"]["TargetLanguage"]

translator = Translator()
files = {}

for a, b, c in walk("ftbquests"):
    files[a] = c

if config["ftbquests"].getboolean("IncludeOriginalText"):
    for a in files:
        for b in files[a]:
            if b != "index.nbt" and b != "file.nbt":
                print("Translating " + a + "/" + b)
                with nbtlib.load(a + "/" + b) as c:
                    if "title" in c.root:
                        c.root["title"] = nbtlib.String(translator.translate(c.root["title"], dest=lang).text + " (" + c.root["title"] + ")")
                        print("Title : " + c.root["title"])
                    if "description" in c.root:
                        c.root["description"] = nbtlib.String(translator.translate(c.root["description"], dest=lang).text + (" (" + c.root["description"] + ")" if config["ftbquests"].getboolean("IncludeOriginalText") else ""))
                        print("Description : " + c.root["description"])