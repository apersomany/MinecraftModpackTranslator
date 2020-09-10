import configparser
import glob
from shutil import rmtree, make_archive
from json import loads, dumps
from os import makedirs
from os.path import isfile, isdir
from googletrans import Translator
from zipfile import ZipFile

config = configparser.ConfigParser()
config.read("config.ini")
lang = config["mods"]["TargetLanguage"]
flang = config["mods"]["LanguageFileName"]

translator = Translator()
files = glob.glob("mods/*.jar")

mcmeta = dumps({
    "pack": {
        "pack_format": 3,
        "description": "Mod Translations"
    }
}, indent=4)

if(isdir("tmp")):
    rmtree("tmp")
makedirs("tmp")
open("tmp/pack.mcmeta", "w").write(mcmeta)

for a in files:
    with(ZipFile(a, "r")) as jar:
        if "mcmod.info" in jar.namelist():
            tmp = loads(jar.read("mcmod.info").replace(b"\n", b""))
            info = tmp[0] if isinstance(tmp, list) else tmp["modList"][0]
            p = ""
            for b in jar.namelist():
                if("en_us.lang" in b.lower()):
                    p = b
            if p != "":
                if ("assets/" + info["modid"] + "/lang/" + flang + ".lang").lower() in [l.lower() for l in jar.namelist()]:
                    print(info["name"] + " already has a translation")
                else:
                    print("Translating " + info["name"])
                    makedirs("tmp/assets/" + info["modid"] + "/lang/")
                    jar.extract(p, "tmp/tmp/")
                    orig = open("tmp/tmp/" + p, "r", encoding="utf-8").read().splitlines()
                    key = [[]]
                    val = [[]]
                    size = 0
                    c = 0
                    for b in orig:
                        if "=" in b:
                            size += len(b)
                            if size > 15000:
                                c += 1
                                size = 0
                                key.append([])
                                val.append([])
                            key[c].append(b.split("=")[0])
                            val[c].append(b.split("=")[1])
                    tmp = ""
                    for c in range(len(key)):
                        b = 0
                        for translation in translator.translate(val[c], dest=lang):
                            tmp += key[c][b] + "=" + translation.text.replace("% ", "%").replace("$ ", "$").replace("§ ", "") + (" (" + val[c][b].replace("%s", "") + ")\n" if config["ftbquests"].getboolean("IncludeOriginalText") else "")
                            b += 1
                    open("tmp/assets/" + info["modid"] + "/lang/" + flang + ".lang", "w", encoding="utf-8").write(tmp)
                    rmtree("tmp/tmp")
            else:
                print(info["name"] + " doesn't have a lang file, skipping")

print("Zipping files")
make_archive("translations", "zip", "tmp")
print("Cleaning Up")
rmtree("tmp")