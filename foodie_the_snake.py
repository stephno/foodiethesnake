"""
Source code (v0.1) for Foodie the Snake,
a snake game developed with Python 3.7 and the Arcade library.
"""

import arcade


SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
RIGHT_SW_LIMIT =  SCREEN_WIDTH - 10
BOTTOM_SH_LIMIT = SCREEN_HEIGHT + 10
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

    def update_position(self):
        """Update the head’s position."""
        if (self.x <= RIGHT_SW_LIMIT) and (self.y == SCREEN_HEIGHT):
            self.move_right()

        if (self.x >= RIGHT_SW_LIMIT) and (self.y <= SCREEN_HEIGHT):
            self.move_down()

        # if (self.x > RIGHT_SW_LIMIT) and (self.y <= BOTTOM_SH_LIMIT):
        #     self.move_left()

        # if (self.x <= RIGHT_SW_LIMIT) and (self.y <= SCREEN_HEIGHT):
        #     self.move_up()


        # if self.y <= SCREEN_HEIGHT :
        #     self.move_up()


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

    def update(self, delta_time):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.foodie.update_position()


def app():
    window = TheApp(SCREEN_WIDTH, SCREEN_HEIGHT, "Foodie")

    # arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    the_app = app()
