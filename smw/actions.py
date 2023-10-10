from aiy.leds import Leds, Color, Pattern

actions = [
	{
		'id': '1up',
		'display': 'You got a 1UP!', 
		'color': Color.GREEN,
		'points': 4
	},
	{
		'id': 'mushroom',
		'display': 'You got a mushroom!', 
		'color': Color.RED,
		'points': 2
	},
	{
		'id': 'coin',
		'display': 'You collected a coin!', 
		'color': Color.YELLOW,
		'points': 1
	},
	{
		'id': 'yoshi',
		'display': 'You got Yoshi!\nYoshi adds 2 extra points each turn!', 
		'color': Color.GREEN,
		'points': 0
	},
	{
		'id': 'courseClear',
		'display': 'You cleared a course!',
		'color': Color.PURPLE,
		'points': 10
	},
	{
		'id': 'gameOver',
		'display': 'Game Over',
		'color': Color.RED,
		'points': 0
	}
]