"""
Source code (v0.1) for Foodie the Snake,
a snake game developed with Python 3.7 and the Arcade library.
"""

import arcade

FOODIE_HEAD_SIZE = 10
FOODIE_COLOR = arcade.color.BRIGHT_GREEN

UP = 0
RIGHT = 3
DOWN = 6
LEFT = 9
DEFAULT_DIRECTION = UP

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
RIGHT_SW_LIMIT = SCREEN_WIDTH - 10
BOTTOM_SH_LIMIT = FOODIE_HEAD_SIZE


class Snake:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction

    def draw_snake(self):
        arcade.draw_lrtb_rectangle_filled(self.x, (self.x + FOODIE_HEAD_SIZE),
                                          self.y, (self.y - FOODIE_HEAD_SIZE),
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
        if self.direction == UP:
            self.move_up()

        if self.direction == RIGHT:
            self.move_right()

        if self.direction == DOWN:
            self.move_down()

        if self.direction == LEFT:
            self.move_left()


class TheApp(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class’s init function
        super().__init__(width, height, title)

        arcade.set_background_color((102, 51, 0))

        # Create Foodie
        self.foodie = Snake((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),
                            DEFAULT_DIRECTION, FOODIE_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.foodie.draw_snake()

    def update(self, delta_time):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.foodie.update_position()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP:
            self.foodie.direction = UP
        if key == arcade.key.RIGHT:
            self.foodie.direction = RIGHT
        if key == arcade.key.DOWN:
            self.foodie.direction = DOWN
        if key == arcade.key.LEFT:
            self.foodie.direction = LEFT


def app():
    window = TheApp(SCREEN_WIDTH, SCREEN_HEIGHT, "Foodie")

    # arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    the_app = app()
