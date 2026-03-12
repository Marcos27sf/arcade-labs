import arcade
from pathlib import Path

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
FLOOR_HEIGHT = 100

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AERO_BLUE

        self.gd_sprite_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\img\\gd.png")
        self.coin_sprite_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\img\\coin.png")
        self.coin_sound_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\sound\\coin_sound.mp3")

        self.sprite_list = arcade.SpriteList()

        self.gd_sprite = arcade.Sprite(self.gd_sprite_path)
        self.coin_sprite = arcade.Sprite(self.coin_sprite_path, scale=0.3)

        self.sprite_list.append(self.gd_sprite)
        self.sprite_list.append(self.coin_sprite)

        self.coin_sound = arcade.Sound(self.coin_sound_path)

        self.gd_sprite.left = self.gd_sprite.width
        self.gd_sprite.bottom = FLOOR_HEIGHT
        self.gd_sprite_speed = 800

        self.coin_sprite.right = SCREEN_WIDTH - self.coin_sprite.width / 2
        self.coin_sprite.top = SCREEN_HEIGHT - self.coin_sprite.height / 2

        self.pressed_key = {
            "left": False,
            "right": False
        }

        self.gravity = 0.5
        self.jump_force = 12
        self.is_jumping = False
        self.angular_speed = 0
    

    def on_draw(self):
        self.clear()

        arcade.draw_lrbt_rectangle_filled(0, 1000, 0, 100, arcade.color.BLUEBERRY)

        self.sprite_list.draw()

        

    def on_update(self, delta_time):
        if self.pressed_key["left"]: self.gd_sprite.center_x -= self.gd_sprite_speed * delta_time
        if self.pressed_key["right"]: self.gd_sprite.center_x += self.gd_sprite_speed * delta_time

        if self.gd_sprite.center_x > SCREEN_WIDTH + self.gd_sprite.width / 2: self.gd_sprite.center_x = - self.gd_sprite.width / 2
        if self.gd_sprite.center_x < - self.gd_sprite.width / 2: self.gd_sprite.center_x = SCREEN_WIDTH + self.gd_sprite.width / 2

        if self.is_jumping:
            self.gd_sprite.change_y -= self.gravity
            self.gd_sprite.angle += self.angular_speed
        
        self.gd_sprite.center_y += self.gd_sprite.change_y

        if self.gd_sprite.bottom < FLOOR_HEIGHT:
            self.gd_sprite.bottom = FLOOR_HEIGHT - 6
            self.gd_sprite.change_y = 0
            self.is_jumping = False
            self.gd_sprite.angle = 0
            self.angular_speed = 0


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.coin_sprite.collides_with_point((x,y)):
            self.coin_sound.play()


    
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.D: self.pressed_key["right"] = True
        elif key == arcade.key.A: self.pressed_key["left"] = True

        if key == arcade.key.SPACE and not self.is_jumping:
            self.gd_sprite.change_y = self.jump_force
            self.is_jumping = True
            self.angular_speed = 6


    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.D: self.pressed_key["right"] = False
        elif key == arcade.key.A: self.pressed_key["left"] = False


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "GD")
    start_view = GameView()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()