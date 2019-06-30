"""
Source code (v0.1) for Foodie the Snake,
a snake game developed with Python 3.7 and the Arcade library.
"""

import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FOODIE_COLOR = arcade.color.BRIGHT_GREEN


class Snake:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw_snake(self):
        arcade.draw_lrtb_rectangle_filled(self.x, (self.x + 10),
                                          self.y, (self.y - 10),
                                          self.color)

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def update(self):
        """Update the head’s position."""
        self.mv_right()


class TheApp(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class’s init function
        super().__init__(width, height, title)

        arcade.set_background_color((102, 51, 0))

        # Create Foodie
        self.foodie = Snake(0, SCREEN_HEIGHT, FOODIE_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.foodie.draw_snake()

    def update_position(self, delta_time):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.foodie.update()


def app():
    window = TheApp(SCREEN_WIDTH, SCREEN_HEIGHT, "Foodie")

    # arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    the_app = app()
