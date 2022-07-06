def on_button_pressed_a():
    sprite.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    while True:
        sprite.move(1)
        basic.pause(Interval)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    sprite.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite3: game.LedSprite = None
sprite2: game.LedSprite = None
Interval = 0
sprite: game.LedSprite = None
food = game.create_sprite(randint(0, 4), randint(0, 4))
sprite = game.create_sprite(2, 2)
Interval = 1000
x = 0
y = 0
x1 = 0
y1 = 0
game.set_score(0)

def on_forever():
    basic.pause(1000)
    led.toggle(sprite.get(LedSpriteProperty.X),
        sprite.get(LedSpriteProperty.Y))
basic.forever(on_forever)

def on_forever2():
    global x, y
    x = sprite.get(LedSpriteProperty.X)
    y = sprite.get(LedSpriteProperty.Y)
    basic.pause(Interval - 100)
basic.forever(on_forever2)

def on_forever3():
    global Interval, food
    if sprite.is_touching(food):
        game.add_score(1)
        food.delete()
        Interval = Interval - 50
        food = game.create_sprite(randint(0, 4), randint(0, 4))
basic.forever(on_forever3)

def on_forever4():
    global sprite2, sprite3
    if game.score() == 1:
        sprite2 = game.create_sprite(x, y)
        basic.pause(Interval - 250)
        sprite2.delete()
    if game.score() == 2:
        sprite3 = game.create_sprite(x1, y1)
        basic.pause(Interval - 250)
        sprite3.delete()
basic.forever(on_forever4)

def on_forever5():
    global x1, y1
    x1 = x
    y1 = y
    basic.pause(Interval - 200)
basic.forever(on_forever5)
