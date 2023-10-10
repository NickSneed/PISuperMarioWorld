import time
from aiy.board import Board, Led
from aiy.leds import Leds, Color, Pattern

# Flashes colors
def flashAnimation(cycles):
	
	ledTime = 0.15

	with Leds() as leds:

		i = 0
		while i < cycles:	
			i += 1
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

# Fades up and down in red
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
