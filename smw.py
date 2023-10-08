import random
import time
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
		'display': 'You got a mushroom', 
		'sound': 'smw_power-up.wav', 
		'color': Color.RED,
		'points': 2
	},
	{
		'id': 'coin',
		'display': 'Coin', 
		'sound': 'smw_coin.wav', 
		'color': Color.YELLOW,
		'points': 1
	},
	{
		'id': 'yohsi',
		'display': 'You got Yoshi', 
		'sound': 'smw_riding_yoshi.wav', 
		'color': Color.GREEN,
		'points': 0
	},
	{
		'id': 'courseClear',
		'display': 'You cleared the course', 
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
		print('Super Mario World')
		play_wav_async(soundsPath + startSound)
		fadeAnimation()
		print('Press the button to start')

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			play_wav_async(soundsPath + pressSound)
			flashAnimation(0.15);

			# Generate random number
			randomNum = random.randint(0,5)

			# Choose random action and increment points
			curAction = actions[randomNum];
			points = points + curAction['points'] + yoshi;

			# Special actions
			if curAction['id'] == 'gameOver':
				points = 0
			if curAction['id'] == 'gameOver':
				yoshi = 2

			# Actions
			if points < 20:
				print(curAction['display'] + ' | ' + curAction['points'] + 'pts')
				print('Total Points: ' + str(points))
				leds.update(Leds.rgb_on(curAction['color']))
				play_wav(soundsPath + curAction['sound'])
				leds.update(Leds.rgb_off())

			# Ending
			if points >= 20:
				points = 0
				print('You win!')
				play_wav_async(soundsPath + endSound)
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);
				flashAnimation(0.15);

if __name__ == '__main__':
    main()
