from __future__ import unicode_literals
import youtube_dl
from youtube_dl import YoutubeDL
import json
from pyglet.media import Source, Player, load

with open('songlist.json') as j:
    songlist = json.load(j)
print('Hello, this is Music app.')
print('Pick an option:')
def emptylist():
    print('Song list is empty')
    input('Press enter to continue...')
def notemptylist(a):
    for i, j in enumerate(a, 1):
        print('{}. {}'.format(i, j['TITLE']))
while True:
    print('1. Show all songs')
    print("2. Show a song's detail")
    print('3. Play a song')
    print('4. Search and download songs')
    print('5. Exit')
    option = int(input(''))
    if option == 1:
        if songlist == []:
            emptylist()
        else:
            notemptylist(songlist)
            useless = input('Press enter to continue...')
    elif option == 2:
        if songlist == []:
            emptylist()
        else:
            notemptylist(songlist)
            while True:
                print('Enter song number')
                songdetail = int(input('')) - 1
                print('TITLE: ', songlist[songdetail]['TITLE'])
                print('ID: ', songlist[songdetail]['ID'])
                print('CREATOR: ', songlist[songdetail]['CREATOR'])
                print('DURATION: ', songlist[songdetail]['DURATION'])
                input('Press enter to continue...')
                print("Do you wanna get more song's informations? (Press y for yes, and n for no)")
                more = input('')
                if more == 'y':
                    pass
                elif more == 'n':
                    break
    elif option == 3:
        if songlist == []:
            emptylist()
        else:
            notemptylist(songlist)
            while True:
                print('Enter song number')
                songplay = int(input('')) - 1
                player = Player()
                Source = load(songlist[songplay]['ID'] + '.mp3')
                player.queue(Source)
                player.play()
                while True:
                    print('Enter playback options (play, pause, stop)')
                    playorpause = input('')
                    if playorpause == 'play':
                        player.play()
                    elif playorpause == 'pause':
                        player.pause()
                    elif playorpause == 'stop':
                        player.pause()
                        break
                print('Do you wanna play music more? (Press y for yes, and n for no)')
                more = input('')
                if more == 'y':
                    pass
                elif more == 'n':
                    break
    elif option == 4:
        print("Enter the song's name you wanna search")
        searchname = input('')
        options = {
            'default_search': 'ytsearch7',
            'quiet': True,
            'no_warnings': True,
            }
        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(searchname, False)
        for i, j in enumerate(search_result['entries'],1):
            print('{}. {}'.format(i, j['title']))
        print("Enter the song's position that you wanna download")
        print("Press 0 if you don't wanna download anything")
        downsong = int(input(''))
        if downsong == 0:
            pass
        elif 1 <= downsong <= 7:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'outtmpl': '%(id)s.%(ext)s',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([search_result['entries'][downsong-1]['webpage_url']])
            newsong = {
                'ID': search_result['entries'][downsong-1]['id'],
                'TITLE': search_result['entries'][downsong-1]['title'],
                'CREATOR': search_result['entries'][downsong-1]['creator'],
                'DURATION': search_result['entries'][downsong-1]['duration'],
            }
            songlist.append(newsong)
            print('Done.')
            print('Do ya wanna play it? (press "y" for yes, and press "n" for no)')
            playornot = input('')
            if playornot == 'y':
                player = Player()
                Source = load(search_result['entries'][downsong-1]['id'] + '.mp3')
                player.queue(Source)
                player.play()
                while True:
                    print('Enter playback options (play, pause, stop)')
                    playorpause = input('')
                    if playorpause == 'play':
                        player.play()
                    elif playorpause == 'pause':
                        player.pause()
                    elif playorpause == 'stop':
                        player.pause()
                        break
            elif playornot == 'n':
                pass
    elif option == 5:
        with open('songlist.json', 'w') as f:
            json.dump(songlist, f)
        break