# type: ignore
import pgzrun
from random import randint
import random

WIDTH = 800
HEIGHT = 600
RANGE_UP_LEVEL = {
    1: 40,
    2: 100,
    3: 180,
    4: 280,
    5: 400,
}
POINT = 0
HEALTH = 3
GAME_OVER = False
SPEED = 1

reset_button = Actor('reset-100-100', (WIDTH, HEIGHT))

class thing:
    def __init__(self, list_thing_images = []):
        self.list_things_images = list_thing_images
        self.list_things = []
        
    def __random_things_picture(self):
        return self.list_things_images[random.choice(range(len(self.list_things_images)))]
    
    def create_things(self, number):
        for index in range(number):
            self.list_things.append(Actor(self.__random_things_picture()))
    
    def init_things(self):
        for thing in self.list_things:
            thing.pos = randint(130, WIDTH-130), 0
    
    def draw_things(self):
        for thing in self.list_things:
            thing.draw()
        
    def check_things_drop_out(self):
        global HEALTH, GAME_OVER, SPEED
        self.check_game_over()
        for thing in self.list_things:
            if thing.y < HEIGHT:
                thing.y += SPEED
            else:
                HEALTH -= 1
                return self.reset_thing_pos(thing)
                
    def things_clicked(self, pos):
        global POINT
        self.check_update_speed()
        for thing in self.list_things:
            if abs(pos[0] - thing.x) < 50 and abs(pos[1] - thing.y) < 50:
                self.reset_thing_pos(thing)
                POINT += 1
                
    @classmethod
    def check_update_speed(cls):
        global SPEED
        for level in RANGE_UP_LEVEL:
            if POINT < RANGE_UP_LEVEL[level]:
                SPEED = 1 * level
                return
    
    @classmethod        
    def check_game_over(cls):
        global HEALTH, GAME_OVER
        if HEALTH <= 0:
            GAME_OVER = True
        return
        
    def reset_thing_pos(self, thing):
        thing.pos = randint(130, WIDTH-130), 0

things_obj = thing([
    'apple-50-50', 
])
things_obj.create_things(3)
things_obj.init_things()

def draw():
    screen.clear()
    if not GAME_OVER:
        screen.blit('sky-800-600', (0, 0))
        screen.draw.text(f"point: {POINT}", (10, 10), color="black", fontsize=60)
        screen.draw.text(f"health: {HEALTH}", (600, 10), color="black", fontsize=60)
        things_obj.draw_things()
    else:
        screen.fill((255,255,255))
        screen.blit('game-over', (135, 0))
        reset_button.pos = 50, 50
        reset_button.draw()
        screen.draw.text(f"point: {POINT}", (330, 10), color="black", fontsize=60)
    
def update():
    if not GAME_OVER:
        things_obj.check_things_drop_out()
    print(SPEED)

def on_mouse_down(pos):
    global GAME_OVER, POINT, HEALTH, SPEED
    if not GAME_OVER: 
        things_obj.things_clicked(pos)
    
    if abs(pos[0] - reset_button.x) < 100 and abs(pos[1] - reset_button.y) < 100:
        print('reset game')
        GAME_OVER = False
        things_obj.init_things()
        POINT = 0
        HEALTH = 3
        SPEED = 1
        reset_button.pos = WIDTH, HEIGHT
    
pgzrun.go()
