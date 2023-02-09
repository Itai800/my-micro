def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
sprite = game.create_sprite(randint(0, 4), 4)
game.set_life(3)
dot = game.create_sprite(randint(0, 4), 0)

def on_forever():
    global dot
    dot.change(LedSpriteProperty.Y, 1)
    basic.pause(500)
    if sprite.is_touching(dot):
        dot.delete()
        game.remove_life(1)
        basic.pause(500)
    if dot.get(LedSpriteProperty.Y) == 4:
        dot.delete()
        game.add_score(1)
        dot = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever)
