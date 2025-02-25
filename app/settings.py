import re
import yaml

with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

TOKEN = config["bot"]["token"]
ALLOWED_USERS = set(config["bot"]["allowed_users"])

URL_PATTERN = re.compile(r"https?://\S+")
VIDEO_URL_PATTERNS = [
    r"(https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+)",
    r"(https?://(?:www\.)?vimeo\.com/\d+)",
]
