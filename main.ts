input.onButtonPressed(Button.A, function () {
    sprite.turn(Direction.Left, 90)
})
input.onButtonPressed(Button.AB, function () {
    while (true) {
        sprite.move(1)
        basic.pause(Interval)
    }
})
input.onButtonPressed(Button.B, function () {
    sprite.turn(Direction.Right, 90)
})
let sprite2: game.LedSprite = null
let Interval = 0
let sprite: game.LedSprite = null
let food = game.createSprite(randint(0, 4), randint(0, 4))
sprite = game.createSprite(2, 2)
Interval = 1000
let x = 0
let y = 0
let x1 = 0
let y1 = 0
game.setScore(0)
basic.forever(function () {
    if (sprite.isTouching(food)) {
        game.addScore(1)
        food.delete()
        Interval = Interval - 50
        food = game.createSprite(randint(0, 4), randint(0, 4))
    }
})
basic.forever(function () {
    basic.pause(1000)
    led.toggle(sprite.get(LedSpriteProperty.X), sprite.get(LedSpriteProperty.Y))
})
basic.forever(function () {
    if (game.score() >= 1) {
        sprite2 = game.createSprite(x, y)
        basic.pause(Interval - 250)
        sprite2.delete()
    }
})
basic.forever(function () {
    x = sprite.get(LedSpriteProperty.X)
    y = sprite.get(LedSpriteProperty.Y)
    basic.pause(Interval - 100)
})
