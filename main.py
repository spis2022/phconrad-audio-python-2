# to install wave, type this in Shell:
#  python3 -m poetry add wave
#  python3 -m poetry lock
#  python3 -m poetry install
from replit import audio
from make_waves import make_wave_file
from make_sine_wav import plot_one_period_sine 
from make_sine_wav import make_sine_audio_file


def play_file(filename='audio.wav'):
      
    source = audio.play_file(filename)
    
    
    volume = 1
    loops = 0
    
    print('type "up" or "down" to change volume')
    print('type "loop" to add another loop')
    print('press enter to play/pause')
    
    while True:
        print(
            f'volume is at {source.volume * 100}% with',
            f'{source.loops_remaining} loops remaining.'
        )
    
        cmd = input('> ').lower()
    
        if cmd == 'up':
            source.volume += .25
            volume += .25
        elif cmd == 'down':
            source.volume -= .25
            volume -= .25
        elif cmd == 'loop':
            loops += 1
            source.set_loop(source.loops_remaining + 1)
        else:
            source.paused = not source.paused


if __name__=="__main__":   
  # play_file()
  # plot_one_period_sine(44100, 32767)
  # make_wave_file('white_noise.wav'); play_file('white_noise.wav')

  make_sine_audio_file(filename='my_sine.wav'); play_file('my_sine.wav')
    
  