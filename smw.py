import random
import time
import os
from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern

# sounds configs
soundsPath = '/home/pi/GitHub/PISuperMarioWorld/sounds/'
actions = [
	{
		'id': '1up',
		'display': 'You got a 1UP!', 
		'sound': 'smw_1-up.wav', 
		'color': Color.GREEN,
		'points': 4
	},
	{
		'id': 'mushroom',
		'display': 'You got a mushroom!', 
		'sound': 'smw_power-up.wav', 
		'color': Color.RED,
		'points': 2
	},
	{
		'id': 'coin',
		'display': 'You collected a coin!', 
		'sound': 'smw_coin.wav', 
		'color': Color.YELLOW,
		'points': 1
	},
	{
		'id': 'yoshi',
		'display': 'You got Yoshi!\nYoshi adds 2 points each turn!', 
		'sound': 'smw_riding_yoshi.wav', 
		'color': Color.GREEN,
		'points': 0
	},
	{
		'id': 'courseClear',
		'display': 'You cleared a course!', 
		'sound': 'smw_course_clear.wav', 
		'color': Color.PURPLE,
		'points': 10
	},
	{
		'id': 'gameOver',
		'display': 'Game Over', 
		'sound': 'smw_game_over.wav', 
		'color': Color.RED,
		'points': 0
	}
]
startSound = 'smw_keyhole_exit.wav'
pressSound = 'smw_princess_help.wav'
endSound = 'smw_castle_clear.wav'

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

		points = 0;
		yoshi = 0;

		# Play start sound and LED animation
		os.system('clear')
		print('Super Mario World')
		play_wav_async(soundsPath + startSound)
		fadeAnimation()
		print('Collect 20 points to win')
		print('Press the button to start')

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			os.system('clear')
			play_wav_async(soundsPath + pressSound)
			flashAnimation(0.15);

			# Generate random number
			randomNum = random.randint(0,5)

			# Choose random action and increment points
			curAction = actions[randomNum];
			points = points + curAction['points'] + yoshi;

			# Game over
			if curAction['id'] == 'gameOver':
				points = 0
				yoshi = 0

			# Actions
			print(curAction['display'])
			print(str(curAction['points'] + yoshi) + 'pts')
			print('Score: ' + str(points))
			if yoshi > 0:
				print('\nYou have Yoshi')
			leds.update(Leds.rgb_on(curAction['color']))
			play_wav(soundsPath + curAction['sound'])
			leds.update(Leds.rgb_off())

			# Get yoshi
			if curAction['id'] == 'yoshi':
				yoshi = 2

			# Ending
			if points >= 20:
				points = 0
				yoshi = 0
				print('You win!')
				play_wav_async(soundsPath + endSound)
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);

if __name__ == '__main__':
    main()
