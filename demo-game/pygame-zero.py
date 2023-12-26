# type: ignore
import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "CHÀO MỪNG CÁC BẠN ĐẾN VỚI PYGAME ZERO"
DIRECTION_RUN = 4

actor_1 = Actor('mario_run_1')
list_bricks = []

def actor_run():
    global DIRECTION_RUN
    if keyboard.up:
        DIRECTION_RUN = -4
        actor_1.y += DIRECTION_RUN
    if keyboard.down:
        DIRECTION_RUN = 4
        actor_1.y += DIRECTION_RUN
    if keyboard.left:
        DIRECTION_RUN = -4
        actor_1.x += DIRECTION_RUN
    if keyboard.right:
        DIRECTION_RUN = 4
        actor_1.x += DIRECTION_RUN

def on_key_down():
    if keyboard.space:
        create_brick()
        

def create_brick():
    global list_bricks
    list_bricks.append(Actor('brick_small', actor_1.pos))
    
def draw_bricks():
    for brick in list_bricks:
        brick.draw()

def bricks_fly():
    for brick in list_bricks:
        brick.x += 4

def draw():
    screen.clear()
    actor_1.draw()
    draw_bricks()
    
def update():
    actor_run()
    bricks_fly()
    
pgzrun.go()
