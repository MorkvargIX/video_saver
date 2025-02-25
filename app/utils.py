import re

from app.settings import VIDEO_URL_PATTERNS


def is_video_url(url: str) -> bool:
    for pattern in VIDEO_URL_PATTERNS:
        if re.match(pattern, url):
            return True
    return False
