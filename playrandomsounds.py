import random
import time
from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern

# sounds configs
soundsPath = '/home/pi/GitHub/PIPlayRandomSounds/sounds/'
wavFiles = ['smw_1-up.wav', 'smw_power-up.wav', 'smw_game_over.wav', 'smw_coin.wav', 'smw_course_clear.wav', 'smw_riding_yoshi.wav']
ledColors = [Color.GREEN, Color.RED, Color.RED, Color.YELLOW, Color.PURPLE, Color.GREEN]

actions = [
	{'wav': 'smw_1-up.wav', 'color': Color.GREEN},
	{'wav': 'smw_power-up.wav', 'color': Color.RED},
	{'wav': 'smw_coin.wav', 'color': Color.YELLOW},
	{'wav': 'smw_riding_yoshi.wav', 'color': Color.GREEN},
	{'wav': 'smw_course_clear.wav', 'color': Color.PURPLE},
	{'wav': 'smw_game_over.wav', 'color': Color.RED}
]
startSound = 'smw_keyhole_exit.wav'
pressSound = 'smw_princess_help.wav'

def flashAnimation(ledTime):

	with Leds() as leds:
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

def fadeAnimation():
	ledTime = 0.002

	with Leds() as leds:

		# Fade in
		i = 0
		while i < 256:
			leds.update(Leds.rgb_on((i,0,0)))
			i += 1
			time.sleep(ledTime)

		# Fade out
		i = 255
		while i > -1:
			leds.update(Leds.rgb_on((i,0,0)))
			i -= 1
			time.sleep(ledTime)

def main():
	
	with Board() as board, Leds() as leds:

		# Play start sound and LED animation
		play_wav_async(soundsPath + startSound)
		fadeAnimation()

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			play_wav_async(soundsPath + pressSound)
			flashAnimation(0.15);

			# Generate random number
			randomNum = random.randint(0,5)

			# Turn on LED and play sound
			print('Playing sound ' + str(randomNum))
			leds.update(Leds.rgb_on(actions[randomNum].color))
			play_wav(soundsPath + actions[randomNum].wav)
			leds.update(Leds.rgb_off())

if __name__ == '__main__':
    main()
