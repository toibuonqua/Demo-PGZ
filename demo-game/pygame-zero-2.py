# type: ignore
import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "CHÀO MỪNG CÁC BẠN ĐẾN VỚI PYGAME ZERO"

lasers = list()
player = Actor('apple-50-50')

def draw():
    screen.clear()
    player.draw()
    for laser in lasers:
        laser.draw()

def fire_laser():
    lasers.append(Actor('apple-50-50', center=player.pos))

def on_mouse_down():
    clock.schedule(fire_laser, 1.0)

def on_mouse_move(pos):
    player.pos = pos
    
pgzrun.go()
