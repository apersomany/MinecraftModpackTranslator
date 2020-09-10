# MinecraftModpackTranslator
Translates Minecraft modpacks using the googletrans library. If anyone knows a better way to translate stuff (preferably offline with things like ml), please file an issue :)
## Setup
Install dependencies
```
pip install -r requirements.txt
```
## Usage
To translate mods, place your mods in a folder named mods and run Mods.py. After it's done, a resourepack with the the name of translations.zip will be created. Apply that resourcepack in minecraft, and you're good to go.

To translate FTBQuests, go to your minecraft intstance/server and copy config/ftbquests to the directory that FTBQuests is in and run FTBQuests.py. After it's done copy the ftbquests folder to where it originally was (ofc with overwrite) and launch your game/server.
## Configuring
### TargetLanguage
Your language in ISO 639-1 format

Examples: en, ko, zh
### LanguageFileName
Your language in ISO 639-1 + ISO 3166-2 format with an underscore in the middle

Examples: en_us, ko_kr, zh_cn 
### IncludeOriginalText
If set to yes, your translations will have the original text in parantheses.

Example: Make a crafting table -> 작업대를 만드세요 (Make a crafting table)
