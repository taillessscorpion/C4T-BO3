from pyglet.media import Source, Player, load
a = {
    'id': 'Lost3',
    }
player = Player()
Source = load(a['id'] +'.mp3')
player.queue(Source)
player.play()
while True:
    playorpause = input('Press pl for play, pa for pause, st for stop')
    if playorpause == 'pl':
        player.play()
    elif playorpause == 'pa':
        player.pause()
    elif playorpause == 'st':
        player.pause()
        break
