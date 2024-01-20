# type: ignore
import pgzrun
import random

WIDTH = 400
HEIGHT = 200

TITLE = "CHÀO MỪNG CÁC BẠN ĐẾN VỚI PYGAME ZERO"

apple = Actor('apple-50-50', topleft=(0,0))

def draw():
    apple.draw()

def becomeBrick():
    animate(apple,top=200, duration=3)
    
animate(apple, left=100, duration=3, on_finished=becomeBrick)


pgzrun.go()
