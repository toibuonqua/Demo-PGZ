def draw_line():
    # screen.clear()
    screen.draw.line(
        (random.choice(range(HEIGHT//2, WIDTH//2 + 1)), random.choice(range(HEIGHT//2, WIDTH//2 + 1))), 
        (random.choice(range(0,501)), random.choice(range(0,501))), 
        (255, 0, 0)
    )

def update():
    draw_line()