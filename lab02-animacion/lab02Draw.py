import arcade

def dibujarCubo(x, y):
    arcade.draw_rect_filled(arcade.XYWH(x, y, 100, 100), arcade.color.YELLOW)
    arcade.draw_rect_filled(arcade.XYWH(x - 20, y + 20, 20, 20), arcade.color.BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x + 20, y + 20, 20, 20), arcade.color.BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x - 23, y + 20, 10, 15), arcade.color.WHITE)
    arcade.draw_rect_filled(arcade.XYWH(x + 24, y + 20, 10, 15), arcade.color.WHITE)
    arcade.draw_rect_filled(arcade.XYWH(x, y - 20, 70, 15), arcade.color.BLUE)