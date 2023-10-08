import random
import time
from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern

# sounds configs
soundsPath = '/home/pi/GitHub/PIPlayRandomSounds/sounds/'
wavFiles = ['smw_1-up.wav', 'smw_power-up.wav', 'smw_game_over.wav', 'smw_coin.wav', 'smw_course_clear.wav', 'smw_riding_yoshi.wav']
ledColors = [Color.GREEN, Color.RED, Color.RED, Color.YELLOW, Color.PURPLE, Color.GREEN]
startSound = 'smw_keyhole_exit.wav'
pressSound = 'smw_princess_help.wav'

def flashAnimation():

	with Leds() as leds:
		ledTime = 0.15
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

def main():
	
	with Board() as board, Leds() as leds:
		play_wav_async(soundsPath + startSound)
		flashAnimation();
		leds.update(Leds.rgb_off())

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			flashAnimation();

			play_wav_async(soundsPath + pressSound)
			

			# Generate random number
			randomNum = random.randint(0,5)

			# Turn on LED and play sound
			leds.update(Leds.rgb_on(ledColors[randomNum]))
			print('Playing sound ' + str(randomNum))
			play_wav(soundsPath + wavFiles[randomNum])
			leds.update(Leds.rgb_off())

if __name__ == '__main__':
    main()
