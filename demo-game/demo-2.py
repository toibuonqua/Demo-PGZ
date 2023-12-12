# type: ignore
import pgzrun
import random

WIDTH = 394
HEIGHT = 600

bird = Actor('yellowbird-midflap')
bird.pos = (75, HEIGHT/2)
bird.gravity = 0.1
bird.jump_strength = -50 
bird.dead = False

pipes = []
PIPE_ADD_INTERVAL = 120
pipe_add_counter = PIPE_ADD_INTERVAL

def update_bird():
    if not bird.dead:
        bird.y += bird.gravity
        bird.gravity += 0.1
        bird.image  = 'yellowbird-downflap'

        if bird.y > HEIGHT:
            bird.dead = True

        for pipe in pipes:
            if bird.colliderect(pipe):
                bird.dead = True

def update_pipes():
    global pipe_add_counter
    if not bird.dead:
        for pipe in pipes:
            pipe.left -= 2

            if pipe.right < 0:
                pipes.remove(pipe)

        pipe_add_counter -= 1
        if pipe_add_counter == 0:
            create_pipe()
            pipe_add_counter = PIPE_ADD_INTERVAL

def create_pipe():
    pipe_gap = random.choice(range(100, 125))
    pipe_y = HEIGHT - pipe_gap
    top_pipe = Actor('pipe-green-rotate', pos=(WIDTH, pipe_gap))
    bottom_pipe = Actor('pipe-green', pos=(WIDTH, HEIGHT))
    pipes.append(top_pipe)
    pipes.append(bottom_pipe)

def draw():
    screen.clear()
    screen.blit('background-night-500-700', (0, 0))
    bird.draw()
    for pipe in pipes:
        pipe.draw()

def update():
    update_bird()
    update_pipes()

def on_key_down():
    if not bird.dead:
        bird.gravity = 0
        bird.y += bird.jump_strength
        bird.image = 'yellowbird-upflap'

pgzrun.go()
