@namespace
class SpriteKind:
    Monk1 = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f c c c c f f . . 
                        . f f f c c c c c c f f . 
                        f f c c c c c c c c c f f 
                        f c c c c f c c c c c c f 
                        . f f f f c c c c f c c f 
                        . f f f f c c f c c c f f 
                        . f f f f f f f f f f f f 
                        . f f f f f f f f f f f f 
                        . . f f f f f f f f f f . 
                        . . e f f f f f f f f f . 
                        . . e f f f f f f f f e f 
                        . . 4 c 7 7 7 7 7 e 4 4 e 
                        . . e f f f f f f f e e . 
                        . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f c c c c f f . . 
                        . . f f c c c c c c f f . 
                        . f f f c c c c c c c f f 
                        f f f c c c c c c c c c f 
                        f f c c c f c c c c c c f 
                        . f f f f f c c c f c f f 
                        . f f f f c c f f c f f f 
                        . . f f f f f f f f f f f 
                        . . f f f f f f f f f f . 
                        . . f f f f f f f f f e . 
                        . f e f f f f f f f f e . 
                        . e 4 4 e 7 7 7 7 7 c 4 . 
                        . . e e f f f f f f f e . 
                        . . . . . . . . f f f . .
            """),
            img("""
                . . . . f f f f . . . . . 
                        . . f f c c c c f f . . . 
                        . f f c c c c c c f f . . 
                        f f c c c c c c c c f f . 
                        f f c c f c c c c c c f . 
                        f f f f f c c c f c c f . 
                        f f f f c c c f c c f f . 
                        f f f f f f f f f f f f . 
                        f f f f f f f f f f f f . 
                        . f f f f f f f f f f . . 
                        . f f f f f f f f f f . . 
                        f e f f f f f f f f e f . 
                        e 4 f 7 7 7 7 7 7 c 4 e . 
                        e e f 6 6 6 6 6 6 f e e . 
                        . . . f f f f f f . . . . 
                        . . . f f . . f f . . . .
            """)],
        100,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    if mySprite.tile_kind_at(TileDirection.LEFT, assets.tile("""
        transparency16
    """)) or mySprite.tile_kind_at(TileDirection.RIGHT, assets.tile("""
        transparency16
    """)) or (mySprite.tile_kind_at(TileDirection.TOP, assets.tile("""
        transparency16
    """)) or mySprite.tile_kind_at(TileDirection.BOTTOM,
        assets.tile("""
            transparency16
        """))):
        pass
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    if controller.B.is_pressed():
        game.show_long_text("My name is Gwan the monk and this is the air bending temple.",
            DialogLayout.TOP)
        game.show_long_text("Do you see that tile on the floor?", DialogLayout.TOP)
        game.show_long_text("That tile holds the secret to air bending!",
            DialogLayout.TOP)
sprites.on_overlap(SpriteKind.player, SpriteKind.Monk1, on_on_overlap)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . f f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . . f f e e f b f e e f f 
                        . . f f 4 4 f 1 e 4 e f . 
                        . . . f 4 4 4 e e f f f . 
                        . . . f f e e 4 4 e f . . 
                        . . . f 7 7 e 4 4 e f . . 
                        . . f f 6 6 f e e f f f . 
                        . . f f f f f f f f f f . 
                        . . . f f f . . . f f . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . f f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . f f f e e f b f e e f f 
                        . . f f 4 4 f 1 e 4 e f f 
                        . . . f 4 4 4 4 e f f f . 
                        . . . f f e e e e 4 4 4 . 
                        . . . f 7 7 7 7 e 4 4 e . 
                        . . f f 6 6 6 6 f e e f . 
                        . . f f f f f f f f f f . 
                        . . . f f f . . . f f . .
            """),
            img("""
                . . . . . f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . . f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . . f f e e f b f e e f f 
                        . . . f 4 4 f 1 e 4 e f . 
                        . . . f 4 4 4 4 e f f f . 
                        . . . f f e e e e e f . . 
                        . . . f 7 7 7 e 4 4 e . . 
                        . . . f 7 7 7 e 4 4 e . . 
                        . . . f 6 6 6 f e e f . . 
                        . . . . f f f f f f . . . 
                        . . . . . . f f f . . . .
            """)],
        100,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite2, location):
    global Bending_Type
    if controller.B.is_pressed():
        game.show_long_text("You learned air bending!", DialogLayout.TOP)
        Bending_Type = "air"
        music.play(music.melody_playable(music.power_up),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile21
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite3, location2):
    if controller.B.is_pressed():
        tiles.set_tile_at(location2, assets.tile("""
            myTile17
        """))
        info.change_score_by(3)
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile16
    """),
    on_overlap_tile2)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . 
                        . . . f f f f f f . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f f . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f f . 
                        f f e 4 e 1 f 4 4 f f . . 
                        . f f f e 4 4 4 4 f . . . 
                        . 4 4 4 e e e e f f . . . 
                        . e 4 4 e 7 7 7 7 f . . . 
                        . f e e f 6 6 6 6 f f . . 
                        . f f f f f f f f f f . . 
                        . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . f f f f f f . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f f . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f . . 
                        . f e 4 e 1 f 4 4 f f . . 
                        . f f f e e 4 4 4 f . . . 
                        . . f e 4 4 e e f f . . . 
                        . . f e 4 4 e 7 7 f . . . 
                        . f f f e e f 6 6 f f . . 
                        . f f f f f f f f f f . . 
                        . . f f . . . f f f . . .
            """),
            img("""
                . . . f f f f f . . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f . . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f . . 
                        . f e 4 e 1 f 4 4 f . . . 
                        . f f f e 4 4 4 4 f . . . 
                        . . f e e e e e f f . . . 
                        . . e 4 4 e 7 7 7 f . . . 
                        . . e 4 4 e 7 7 7 f . . . 
                        . . f e e f 6 6 6 f . . . 
                        . . . f f f f f f . . . . 
                        . . . . f f f . . . . . .
            """)],
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f f f f f f f . . 
                        . . f f f f f f c f f f . 
                        f f f f f f f c c f f f c 
                        f f f f c f f f f f f f c 
                        . c c c f f f e e f f c c 
                        . f f f f f e e f f c c f 
                        . f f f b f e e f b f f f 
                        . f f 4 1 f 4 4 f 1 4 f f 
                        . . f e 4 4 4 4 4 e e f e 
                        . f e f b 7 7 7 e 4 4 4 e 
                        . e 4 f 7 7 7 7 e 4 4 e . 
                        . . . f 6 6 6 6 6 e e . . 
                        . . . f f f f f f f . . . 
                        . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f . . . . . 
                        . . f f f f f f f f . . . 
                        . f f f c f f f f f f . . 
                        c f f f c c f f f f f f f 
                        c f f f f f f f c f f f f 
                        c c f f e e f f f c c c . 
                        f c c f f e e f f f f f . 
                        f f f b f e e f b f f f . 
                        f f 4 1 f 4 4 f 1 4 f f . 
                        e f e e 4 4 4 4 4 e f . . 
                        e 4 4 4 e 7 7 7 b f e f . 
                        . e 4 4 e 7 7 7 7 f 4 e . 
                        . . e e 6 6 6 6 6 f . . . 
                        . . . f f f f f f f . . . 
                        . . . . . . . f f f . . .
            """),
            img("""
                . . . . f f f f . . . . . 
                        . . f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f f f c c f f f c . 
                        f f f c f f f f f f f c . 
                        c c c f f f e e f f c c . 
                        f f f f f e e f f c c f . 
                        f f f b f e e f b f f f . 
                        . f 4 1 f 4 4 f 1 4 f . . 
                        . f e 4 4 4 4 4 4 e f . . 
                        . f f f e e e e f f f . . 
                        f e f b 7 7 7 7 b f e f . 
                        e 4 f 7 7 7 7 7 7 f 4 e . 
                        e e f 6 6 6 6 6 6 f e e . 
                        . . . f f f f f f . . . . 
                        . . . f f . . f f . . . .
            """)],
        100,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

Bending_Type = ""
mySprite: Sprite = None
info.set_life(3)
info.set_score(0)
mySprite = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f e f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(149, 97))
mySprite2 = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f d d d d f f . . 
            . f d d d d d d d d f . 
            f d d d 4 d d d d d d f 
            f d d 4 4 4 d d d d d f 
            f d d 4 4 4 4 d d d d f 
            f 4 d 4 4 4 4 4 4 d 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f d 4 d d d d d d 4 d f 
            . f d d d b b d d d f . 
            . f f e d d d d e f f . 
            e 4 f 5 4 d d 4 5 f 4 e 
            4 d f 4 4 d d 4 4 f d 4 
            4 4 f 5 5 5 5 5 5 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.Monk1)
tiles.place_on_tile(mySprite2, tiles.get_tile_location(169, 105))