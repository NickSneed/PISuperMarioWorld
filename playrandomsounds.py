import random
from aiy.voice.audio import play_wav
from aiy.board import Board, Led

TEST_SOUND_PATH = '/home/pi/GitHub/PIPlayRandomSounds/sounds/'

def main():
	with Board() as board:
		board.led.state = Led.ON
		play_wav(TEST_SOUND_PATH + 's1.wav')
		board.led.state = Led.OFF

		# While True will run forever
		while True:

			# Button press
			board.button.wait_for_press()
			board.led.state = Led.ON
			randomNum = str(random.randint(1,6))
			play_wav(TEST_SOUND_PATH + 's' + randomNum + '.wav')
			board.led.state = Led.OFF

			# Button release
			# board.button.wait_for_release()
			# print('button released')


if __name__ == '__main__':
    main()
