from aiy.leds import Leds, Color, Pattern

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
		'display': 'You got Yoshi!\nYoshi adds 2 extra points each turn!', 
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