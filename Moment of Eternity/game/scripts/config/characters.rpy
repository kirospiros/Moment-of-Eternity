## Определяем персонажей вместе с их изображениями.

define me = Character(
    _("Я"), image="main_character", color="#2E8B57"
)

## Enji

define enji_color = "#7B68EE"

define enji = Character(_("Энджи"), color=enji_color)

define enji_sprite_size = [400, 960]

image enji usual = im.Scale("sprites/enji/enji usual.png", *enji_sprite_size)
image enji upset = im.Scale("sprites/enji/enji upset.png", *enji_sprite_size)
image enji thinking = im.Scale("sprites/enji/enji thinking.png", *enji_sprite_size)
image enji sorried = im.Scale("sprites/enji/enji sorried.png", *enji_sprite_size)
image enji siding = im.Scale("sprites/enji/enji siding.png", *enji_sprite_size)
image enji irritated = im.Scale("sprites/enji/enji irritated.png", *enji_sprite_size)
image enji contemptuous = im.Scale("sprites/enji/enji contemptuous.png", *enji_sprite_size)
image enji speaking = im.Scale("sprites/enji/enji speaking.png", *enji_sprite_size)
image enji speaking down = im.Scale("sprites/enji/enji speaking down.png", *enji_sprite_size)
image enji smiling = im.Scale("sprites/enji/enji smiling.png", *enji_sprite_size)
image enji smiling down = im.Scale("sprites/enji/enji smiling down.png", *enji_sprite_size)
image enji smiling evil = im.Scale("sprites/enji/enji smiling evil.png", *enji_sprite_size)
image enji angry = im.Scale("sprites/enji/enji angry.png", *enji_sprite_size)
image enji angry speaking = im.Scale("sprites/enji/enji angry speaking.png", *enji_sprite_size)
image enji angry siding = im.Scale("sprites/enji/enji angry siding.png", *enji_sprite_size)

## Phil

define phil_color = "#F0FFFF"

define phil = Character(_("Фил"), color=phil_color)

define phil_sprite_size = [400, 873]

image phil usual = im.Scale("sprites/phil/phil usual.png", *phil_sprite_size)
image phil bittersweet = im.Scale("sprites/phil/phil bittersweet.png", *phil_sprite_size)
image phil speaking kindly = im.Scale("sprites/phil/phil speaking kindly.png", *phil_sprite_size)
image phil smiling = im.Scale("sprites/phil/phil smiling.png", *phil_sprite_size)
image phil nervous = im.Scale("sprites/phil/phil nervous.png", *phil_sprite_size)
image phil casual = im.Scale("sprites/phil/phil casual.png", *phil_sprite_size)
image phil casual speaking = im.Scale("sprites/phil/phil casual speaking.png", *phil_sprite_size)
image phil casual smiling = im.Scale("sprites/phil/phil casual smiling.png", *phil_sprite_size)
image phil casual relief = im.Scale("sprites/phil/phil casual relief.png", *phil_sprite_size)
image phil casual relief closed_eyes = im.Scale("sprites/phil/phil casual relief closed_eyes.png", *phil_sprite_size)

## Key

define key_color = "#8B008B"

define key = Character(_("Кей"), color=key_color)

define key_sprite_size = [400, 992]

image key usual = im.Scale("sprites/key/key usual.png", *key_sprite_size)
image key usual smiles = im.Scale("sprites/key/key usual smiles.png", *key_sprite_size)
image key usual speaking = im.Scale("sprites/key/key usual speaking.png", *key_sprite_size)
image key usual speaking kindly = im.Scale("sprites/key/key usual speaking kindly.png", *key_sprite_size)
image key usual worried = im.Scale("sprites/key/key usual worried.png", *key_sprite_size)


## Natali

define natali_color = "#B0E0E6"
define natali = Character(_("Натали"), color=natali_color)

define natali_sprite_size = [400, 1013]

image natali usual = im.Scale("sprites/natali/natali usual.png", *natali_sprite_size)
image natali upset = im.Scale("sprites/natali/natali upset.png", *natali_sprite_size)
image natali smiling = im.Scale("sprites/natali/natali smiling.png", *natali_sprite_size)
image natali concerned = im.Scale("sprites/natali/natali concerned.png", *natali_sprite_size)
image natali concerned closed_eyes = im.Scale("sprites/natali/natali concerned closed_eyes.png", *natali_sprite_size)

## Sae

define sae_color = "#B0E0E6"
define sae = Character(_("Сая"), color=sae_color)

define sae_sprite_size = [350, 993]

image sae badly surprised = im.Scale("sprites/sae/sae badly surprised.png", *sae_sprite_size)
image sae confused = im.Scale("sprites/sae/sae confused.png", *sae_sprite_size)
image sae speaking confused = im.Scale("sprites/sae/sae speaking confused.png", *sae_sprite_size)
image sae uniform badly surprised = im.Scale("sprites/sae/sae uniform badly surprised.png", *sae_sprite_size)
image sae uniform confused = im.Scale("sprites/sae/sae uniform confused.png", *sae_sprite_size)
image sae uniform speaking confused = im.Scale("sprites/sae/sae uniform speaking confused.png", *sae_sprite_size)

## Vox

define vox = Character(_("Голос"), color="#ffffff")

define speaker = Character(
    _("Диктор"), image="speaker", color="#c8ffc8"
)

## Официант в кафе во время преследования Энджи

define waiter = Character(_("Официант"), image="waiter", color="#c8ffc8")

## Unknown character

define character_name = "?"
define current_color = "#ffffff"

define unknown = Character(_(character_name), image="unknown", color=current_color)

image side unknown key = "sprites/unknown/side key.png"
image side unknown natali = "sprites/unknown/side natali.png"
image side unknown phil = "sprites/unknown/side phil.png"
image side unknown sae = "sprites/unknown/side sae.png"

define system = Character(_("system"), color="#B0E0E6")


## Определяет плавное появление и исчезновение новых side-изображений.
## Dissolve работает некорректно, без плавного перехода
transform change_transform(old, new):
    ## При исчезновении со сцены
    contains:
        old
        yalign 1.0
        alpha 1.0
        linear 0.25 alpha 0.0
    ## При появлении на сцене
    contains:
        new
        yalign 1.0
        alpha 0.0
        linear 0.25 alpha 1.0

define config.side_image_change_transform = change_transform

## По мере необходимости: отвечает за переход между side-изображениями одного и
## того же персонажа. В `same_transform` нужно будет расписать `old` и `new`.
# define config.side_image_same_transform = same_transform
