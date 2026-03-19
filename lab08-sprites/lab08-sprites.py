import arcade
from pathlib import Path
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class GameView(arcade.View):

    def __init__ (self):

        super().__init__()

        self.background_color = arcade.color.SKY_BLUE

        self.gato_sprite_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\img\\gato.png")
        self.coin_sprite_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\img\\coin.png")
        self.uah_sprite_path = Path("C:\\Users\\PC\\Desktop\\Laboratorio\\Tecnología de Videojuegos\\img\\uah.png")

        self.main_sprite_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        self.gato_sprite = arcade.Sprite(self.gato_sprite_path, scale=0.07, center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2)

        self.main_sprite_list.append(self.gato_sprite)

        self.keys_pressed = {
            "Up": False,
            "Down": False,
            "Right": False,
            "Left": False
        }

        self.score = 0
    

    def on_draw(self):
        self.clear()
        
        self.main_sprite_list.draw()
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()

        arcade.draw_text(f"Score: {self.score}", 20, 20, arcade.color.BLACK_BEAN)


    def on_update(self, delta_time):
        if self.keys_pressed["Up"] and not sobresale_W(self.gato_sprite): self.gato_sprite.center_y += 20
        if self.keys_pressed["Down"] and not sobresale_S(self.gato_sprite): self.gato_sprite.center_y -= 20
        if self.keys_pressed["Right"] and not sobresale_D(self.gato_sprite): self.gato_sprite.center_x += 20
        if self.keys_pressed["Left"] and not sobresale_A(self.gato_sprite): self.gato_sprite.center_x -= 20

        good_hit_list = arcade.check_for_collision_with_list(self.gato_sprite, self.good_sprite_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.gato_sprite, self.bad_sprite_list)

        if len(self.bad_sprite_list) == 0 or len(bad_hit_list) != 0:
            generar_sprites(self.good_sprite_list, self.bad_sprite_list, self.coin_sprite_path, self.uah_sprite_path)
            self.gato_sprite.center_x = SCREEN_WIDTH / 2
            self.gato_sprite.center_y = SCREEN_HEIGHT / 2
            self.score = 0
        
        for good_sprite_hitted in good_hit_list:
            good_sprite_hitted.kill()
            self.score += 1


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W: self.keys_pressed["Up"] = True
        elif key == arcade.key.S: self.keys_pressed["Down"] = True
        elif key == arcade.key.D: self.keys_pressed["Right"] = True
        elif key == arcade.key.A: self.keys_pressed["Left"] = True


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W: self.keys_pressed["Up"] = False
        elif key == arcade.key.S: self.keys_pressed["Down"] = False
        elif key == arcade.key.D: self.keys_pressed["Right"] = False
        elif key == arcade.key.A: self.keys_pressed["Left"] = False


def sobresale_A(sprite):
    return sprite.center_x < (0 + sprite.width / 2)

def sobresale_D(sprite):
    return sprite.center_x > (SCREEN_WIDTH - sprite.width / 2)

def sobresale_W(sprite):
    return sprite.center_y > (SCREEN_HEIGHT - sprite.height / 2)

def sobresale_S(sprite):
    return sprite.center_y < (0 + sprite.height / 2)

def generar_sprites(good_sprite_list, bad_sprite_list, good_sprite_path, bad_sprite_path):
    good_sprite_list.clear()
    bad_sprite_list.clear()

    for _i in range(7):
        new_sprite = arcade.Sprite(good_sprite_path, scale=0.3, center_x=randint(0, SCREEN_WIDTH), center_y=randint(0, SCREEN_HEIGHT))
        good_sprite_list.append(new_sprite)

    for _i in range(7):
        new_sprite = arcade.Sprite(bad_sprite_path, scale=0.03, center_x=randint(0, SCREEN_WIDTH), center_y=randint(0, SCREEN_HEIGHT))
        bad_sprite_list.append(new_sprite)
        

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Juego de colisiones")
    start_view = GameView()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()