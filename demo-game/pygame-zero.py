# type: ignore
import pgzrun

WIDTH = 200
HEIGHT = 200

TITLE = "CHÀO MỪNG CÁC BẠN ĐẾN VỚI PYGAME ZERO"
RECT = Rect((10, 10), (80, 80))

def draw():
    screen.draw.textbox("Chào mừng các bạn", RECT)
    
pgzrun.go()
