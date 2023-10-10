# Imports
import argparse
import random
import time
import os

# AIY imports
from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern
from aiy.voice.tts import say
from smw.strings import strings
from smw.actions import actions
from smw.ledAnimations import *

# Command args
parser = argparse.ArgumentParser()
parser.add_argument('--voice', type=str, default='False', help='Enables voice over')
args = parser.parse_args()

# Sounds configs
soundsPath = '/home/pi/GitHub/PISuperMarioWorld/sounds/'
startSound = 'smw_keyhole_exit.wav'
pressSound = 'smw_princess_help.wav'
endSound = 'smw_castle_clear.wav'

def printAndTalk(text):
	print(text)
	talk(text)

def talk(text):
	if args.voice == 'True':
		say(text)

def main():
	
	with Board() as board, Leds() as leds:

		points = 0;
		yoshi = 0;

		# Play start sound and LED animation
		os.system('clear')
		print(strings['title'])
		play_wav_async(soundsPath + startSound)
		fadeAnimation()
		print('')
		talk(strings['title'])
		printAndTalk(strings['instructions'])
		printAndTalk(strings['start'])

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			os.system('clear')
			play_wav_async(soundsPath + pressSound)
			flashAnimation(1);

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
			print('\n' + curAction['display'])
			
			if curAction['points'] + yoshi > 0:
				print(str(curAction['points'] + yoshi) + 'pts')

			if yoshi > 0:
				print('\nYou have Yoshi')

			leds.update(Leds.rgb_on(curAction['color']))
			play_wav(soundsPath + curAction['sound'])
			leds.update(Leds.rgb_off())

			talk(curAction['display'])
			if curAction['id'] != 'gameOver':
				talk('You got ' + str(curAction['points'] + yoshi) + ' more points')
				talk('You have a total of  ' + str(points) + ' points')

			# Get yoshi
			if curAction['id'] == 'yoshi':
				yoshi = 2

			# Ending
			if points >= 20:
				points = 0
				yoshi = 0
				os.system('clear')
				print(strings['win'])
				play_wav_async(soundsPath + endSound)
				flashAnimation(9);

if __name__ == '__main__':
    main()
