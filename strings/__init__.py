import os
import sys
from typing import List
import yaml

languages = {}
commands = {}
languages_present = {}

def get_command(value: str) -> List:
    try:
        return commands["command"][value]
    except KeyError:
        print(f"Command '{value}' not found in commands.yml.")
        return []

def get_string(lang: str):
    return languages.get(lang, languages["en"])

# Load commands from commands.yml
try:
    with open(r"./strings/commands.yml", encoding="utf8") as f:
        commands = yaml.safe_load(f)
except Exception as e:
    print(f"Error loading commands.yml: {e}")
    sys.exit()

# Load languages from langs directory
for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        try:
            with open(r"./strings/langs/" + filename, encoding="utf8") as f:
                languages[language_name] = yaml.safe_load(f)
            languages_present[language_name] = languages[language_name].get("name", language_name)
        except Exception as e:
            print(f"There is an issue with the language file '{filename}': {e}")
            sys.exit()

# Set default language if 'en' is missing
if "en" not in languages:
    print("English language file is missing in langs directory.")
    sys.exit()
