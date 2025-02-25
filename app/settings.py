import re
import yaml
import logging


logging.basicConfig(level=logging.INFO)

with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)


TOKEN = config["bot"]["token"]
ALLOWED_USERS = set(config["bot"]["allowed_users"])

URL_PATTERN = re.compile(r"https?://\S+")
