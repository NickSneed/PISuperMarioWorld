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

			# Generate random number
			randomNum = random.randint(1,6)

			# Pick LED color
			ledColor = 'RED'
			if randomNum == 1:
				ledColor = 'GREEN'
			elif randomNum == 2:
				ledColor = 'BLUE'
			elif randomNum == 3:
				ledColor = 'PURPLE'
			elif randomNum == 4:
				ledColor = 'CYAN'
			elif randomNum == 5:
				ledColor = 'YELLOW'
			elif randomNum == 6:
				ledColor = 'RED'
			else: 
				ledColor = 'WHITE'

			# Turn on LED and play sound
			leds.update(Leds.rgb_on(Color[ledColor]))
			play_wav(TEST_SOUND_PATH + 's' + str(randomNum) + '.wav')
			leds.update(Leds.rgb_off())

if __name__ == '__main__':
    main()
