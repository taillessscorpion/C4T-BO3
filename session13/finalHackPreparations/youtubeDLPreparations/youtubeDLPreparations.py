import youtube_dl
import json

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=My1c0Iymy8o',
        download=False
    )
with open('DataYoutube.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)