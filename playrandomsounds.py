import random
from aiy.voice.audio import play_wav
from aiy.board import Board, Led
from aiy.leds import Leds, Color

TEST_SOUND_PATH = '/home/pi/GitHub/PIPlayRandomSounds/sounds/'

def main():
	
	with Board() as board, Leds() as leds:
		leds.update(Leds.rgb_on(Color.GREEN))
		play_wav(TEST_SOUND_PATH + 's1.wav')
		leds.update(Leds.rgb_off())

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			leds.update(Leds.rgb_on(Color.GREEN))
			randomNum = str(random.randint(1,6))
			play_wav(TEST_SOUND_PATH + 's' + randomNum + '.wav')
			leds.update(Leds.rgb_off())

if __name__ == '__main__':
    main()
