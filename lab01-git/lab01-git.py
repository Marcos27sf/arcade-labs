import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "ejempliño")

arcade.start_render()
arcade.draw_text("Hello, world", 350, 300, arcade.color.WHITE)
arcade.finish_render()

print("Modificación")

arcade.run()
