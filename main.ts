input.onButtonPressed(Button.A, function on_button_pressed_a() {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite : game.LedSprite = null
sprite = game.createSprite(randint(0, 4), 4)
game.setLife(3)
let dot = game.createSprite(randint(0, 4), 0)
basic.forever(function on_forever() {
    
    dot.change(LedSpriteProperty.Y, 1)
    basic.pause(500)
    if (sprite.isTouching(dot)) {
        dot.delete()
        game.removeLife(1)
        basic.pause(500)
    }
    
    if (dot.get(LedSpriteProperty.Y) == 4) {
        dot.delete()
        game.addScore(1)
        dot = game.createSprite(randint(0, 4), 0)
    }
    
})
