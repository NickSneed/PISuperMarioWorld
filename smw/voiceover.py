import argparse
from aiy.voice.tts import say

# Command args
parser = argparse.ArgumentParser()
parser.add_argument('--voice', type=str, default='False', help='Enables voice over')
args = parser.parse_args()

# Prints and does voice over
def printAndTalk(text):
	print(text)
	talk(text)

# Only voice over
def talk(text):
	if args.voice == 'True':
		say(text)