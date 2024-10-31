import os
import sys
from typing import List, Optional
import yaml

languages = {}
commands = {}
languages_present = {}


def get_command(lang: str, value: str) -> Optional[str]:
    """Retrieve a specific command for the given language and command name."""
    try:
        return commands[lang][value]
    except KeyError:
        print(f"Command '{value}' not found in language '{lang}'.")
        return None


def get_string(lang: str):
    """Retrieve all strings for a specified language."""
    return languages.get(lang)


# Load command mappings for each language file in ./strings
for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        with open(f"./strings/{filename}", encoding="utf8") as f:
            commands[language_name] = yaml.safe_load(f)

# Load translation strings for each language in ./strings/langs/
for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        with open(r"./strings/langs/en.yml", encoding="utf8") as f:
            languages["en"] = yaml.safe_load(f)
        languages_present["en"] = languages["en"].get("name", "English")

    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        with open(r"./strings/langs/" + filename, encoding="utf8") as f:
            languages[language_name] = yaml.safe_load(f)
        # Ensure missing keys in non-English languages are populated with English defaults
        for item in languages["en"]:
            languages[language_name].setdefault(item, languages["en"][item])

    try:
        languages_present[language_name] = languages[language_name]["name"]
    except KeyError:
        print(
            "There is an issue with a language file. Please report it to the DNS NETWORK at @DNS_NETWORK on Telegram."
        )
        sys.exit()

# Example usage to retrieve a command in English
GETLOG_COMMAND = get_command("en", "GETLOG_COMMAND")
