import random
import time
from aiy.voice.audio import play_wav
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern

TEST_SOUND_PATH = '/home/pi/GitHub/PIPlayRandomSounds/sounds/'

def main():
	
	with Board() as board, Leds() as leds:
		leds.update(Leds.rgb_on(Color.WHITE))
		play_wav(TEST_SOUND_PATH + 'start.wav')
		leds.update(Leds.rgb_off())

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()

			ledTime = 0.2
			leds.update(Leds.rgb_on(Color.GREEN))
			time.sleep(ledTime)
			leds.update(Leds.rgb_on(Color.BLUE))
			time.sleep(ledTime)
			leds.update(Leds.rgb_on(Color.YELLOW))
			time.sleep(ledTime)
			leds.update(Leds.rgb_on(Color.RED))
			time.sleep(ledTime)
			leds.update(Leds.rgb_on(Color.PURPLE))
			time.sleep(ledTime)
			leds.update(Leds.rgb_on(Color.WHITE))
			time.sleep(ledTime)

			# Generate random number
			randomNum = random.randint(1,6)
			randomNum = 1

			# Pick LED color
			ledColor = Color.RED
			if randomNum == 1:
				ledColor = Color.GREEN
			elif randomNum == 2:
				ledColor = Color.BLUE
			elif randomNum == 3:
				ledColor = Color.YELLOW
			elif randomNum == 4:
				ledColor = Color.RED
			elif randomNum == 5:
				ledColor = Color.PURPLE
			elif randomNum == 6:
				ledColor = Color.CYAN
			else: 
				ledColor = Color.WHITE

			# Turn on LED and play sound
			leds.update(Leds.rgb_on(ledColor))
			print('Playing sound ' + str(randomNum))
			play_wav(TEST_SOUND_PATH + 's' + str(randomNum) + '.wav')
			leds.update(Leds.rgb_off())

if __name__ == '__main__':
    main()
