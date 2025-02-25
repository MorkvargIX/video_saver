import os
import re
import yt_dlp

from app.settings import VIDEO_URL_PATTERNS


def is_video_url(url: str) -> bool:
    for pattern in VIDEO_URL_PATTERNS:
        if re.match(pattern, url):
            return True
    return False


def download_video(url: str) -> str:
    cookie_file = "cookies.txt"
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join("downloaded_videos", "%(title)s.%(ext)s"),
        "writethumbnail": True,
        "cookies": cookie_file,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)

    return video_file
