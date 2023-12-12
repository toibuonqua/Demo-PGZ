# type: ignore
import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor('mario_run_1', (WIDTH / 2, HEIGHT / 2))
bombs = []
explosions = []

def draw():
    screen.clear()
    player.draw()
    for bomb in bombs:
        bomb.draw()
    for explosion in explosions:
        explosion.draw()

def update():
    update_player()
    update_bombs()
    check_collisions()

def update_player():
    if keyboard.left:
        player.x -= 5
    elif keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    elif keyboard.down:
        player.y += 5

def update_bombs():
    for bomb in bombs:
        bomb.y += 2
        if bomb.y > HEIGHT:
            bombs.remove(bomb)

def check_collisions():
    for bomb in bombs:
        if bomb.colliderect(player):
            explode(bomb)
            bombs.remove(bomb)

def on_key_down(key):
    if key == keys.SPACE:
        create_bomb()

def create_bomb():
    new_bomb = Actor('yellowbird-midflap', (player.x, player.y))
    bombs.append(new_bomb)

def explode(bomb):
    explosion = Actor('reset-100-100', bomb.pos)
    explosions.append(explosion)

pgzrun.go()
