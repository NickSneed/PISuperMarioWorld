# Imports
import argparse
import random
import os

# AIY imports
from aiy.voice.audio import play_wav, play_wav_async
from aiy.board import Board
from aiy.leds import Leds
from aiy.voice.tts import say

# SMW imports
from smw.strings import strings
from smw.actions import actions
from smw.ledAnimations import *
from smw.sounds import soundsPath, sounds

# Command args
parser = argparse.ArgumentParser()
parser.add_argument('--voice', type=str, default='False', help='Enables voice over')
args = parser.parse_args()

def printAndTalk(text):
	print(text)
	talk(text)

def talk(text):
	if args.voice == 'True':
		say(text)

def play(snd):
	play_wav(soundsPath + snd);

def playAsync(snd):
	play_wav_async(soundsPath + snd);

def main():
	
	with Board() as board, Leds() as leds:

		points = 0;
		yoshi = 0;

		# Play start sound and LED animation
		os.system('clear')
		print(strings['title'])
		playAsync(sounds['startSound'])
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
			playAsync(sounds['pressSound'])
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
			play(curAction['sound'])
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
				playAsync(sounds['endSound'])
				flashAnimation(9);

if __name__ == '__main__':
    main()
