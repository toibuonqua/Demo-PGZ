# type: ignore
import pgzrun

actor1 = Actor('apple-50-50', topleft=(10, 10))
actor2 = Actor('apple-50-50', topleft=(50, 60))

def draw():
    actor2.angle = 45
    actor1.draw()
    actor2.draw()
    
pgzrun.go()