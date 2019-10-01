#//Virtual Reality-Rutina de prueba
from _Main import *
import _Main

steps=0
def virtualReality(steps):
	steps=inc(steps,5)
	move(steps)
	delay(5)
	steps=dec(steps,1)
	object(steps)
	delay(5)
	temperature(2)
	delay(5)

def main():
	virtualReality(steps)


main()