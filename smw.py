# Imports
import random
import os
import smw.helpers as helpers

from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board as board
from aiy.leds import Leds as leds
from smw.strings import strings
from smw.actions import actions
from smw.sounds import sounds

# Main
def main():

	points = 0;
	yoshi = 0;

	# start screen
	os.system('clear')
	print(strings['title'])
	play_wav_async(sounds['startSound'])
	helpers.fadeAni()
	print('')
	helpers.talk(strings['title'])
	helpers.printAndTalk(strings['instructions'])
	helpers.printAndTalk(strings['start'])

	# While True will run forever
	while True:

		# Button press
		board.button.wait_for_press()
		os.system('clear')
		play_wav_async(sounds['pressSound'])
		helpers.flashAni(1);

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
		print('Score: ' + str(points))
		print('')
		print(curAction['display'])
		
		if curAction['points'] + yoshi > 0:
			print(str(curAction['points'] + yoshi) + 'pts')

		if yoshi > 0:
			print('')
			print('You have Yoshi')

		leds.update(Leds.rgb_on(curAction['color']))
		play_wav(sounds[curAction['id']])
		leds.update(Leds.rgb_off())

		helpers.talk(curAction['display'])
		if curAction['id'] != 'gameOver':
			helpers.talk('You got ' + str(curAction['points'] + yoshi) + ' more points')
			helpers.talk('You have a total of  ' + str(points) + ' points')

		# Get yoshi
		if curAction['id'] == 'yoshi':
			yoshi = 2

		# Win
		if points >= 20:
			points = 0
			yoshi = 0
			os.system('clear')
			print(strings['win'])
			play_wav_async(sounds['endSound'])
			helpers.flashAni(9);

if __name__ == '__main__':
    main()
