import arcade
import math
from lab02Draw import dibujarCubo

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 800


class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.RED)

        self.coordsX = 50
        self.coordsY = 250
    
    def on_draw(self):
        self.clear()

        arcade.draw_lrbt_rectangle_filled(0, 1900, 0, 200, arcade.color.PURPLE)

        
        dibujarCubo(math.sin(self.coordsX) * 1600, self.coordsY)

        self.coordsX += .005
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
