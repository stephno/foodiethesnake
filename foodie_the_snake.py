"""
Source code (v0.1) for Foodie the Snake,
a snake game developed with Python 3.7 and the Arcade library.
"""

import arcade
import random

FOODIE_HEAD_SIZE = 50
FOODIE_COLOR = arcade.color.BRIGHT_GREEN
APPLE_SIZE = 50
APPLE_COLOR = arcade.color.DARK_CANDY_APPLE_RED

UP = 0
RIGHT = 3
DOWN = 6
LEFT = 9
DEFAULT_DIRECTION = UP
SPEED = 3

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
RIGHT_SW_LIMIT = SCREEN_WIDTH - FOODIE_HEAD_SIZE
BOTTOM_SH_LIMIT = FOODIE_HEAD_SIZE


class Apple:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw_apple(self):
        arcade.draw_lrtb_rectangle_filled(self.x, (self.x + APPLE_SIZE),
                                          self.y, (self.y - APPLE_SIZE),
                                          self.color)


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
        self.x += SPEED

    def move_left(self):
        self.x -= SPEED

    def move_up(self):
        self.y += SPEED

    def move_down(self):
        self.y -= SPEED

    def update_position(self, game_state):
        """Update the head’s position."""
        self.game_state = game_state
        if not self.game_state:
            if self.direction == UP:
                self.move_up()

            if self.direction == RIGHT:
                self.move_right()

            if self.direction == DOWN:
                self.move_down()

            if self.direction == LEFT:
                self.move_left()

    def check_collision(self, apple_x, apple_y):
        """Check whether a window border, an apple or the tail is hit."""

        # Border Collision
        if (self.x < 0) or (self.x > RIGHT_SW_LIMIT) \
                        or (self.y > SCREEN_HEIGHT) \
                        or (self.y < BOTTOM_SH_LIMIT):
            game_over = True
            
            return game_over

        # Apple Collision
        self.apple_x = apple_x
        self.apple_y = apple_y

        # if self.x in range(self.apple_x, (self.apple_x + 10)) and \
        #    self.y in range(self.apple_y, (self.apple_y - 10)):
        if (self.x == self.apple_x) and (self.y == self.apple_y):
            game_over = True

            return game_over


class TheApp(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class’s init function
        super().__init__(width, height, title)

        arcade.set_background_color((102, 51, 0))

        # Create Apple
        self.apple = Apple(random.randrange(SCREEN_WIDTH - APPLE_SIZE),
                           random.randrange(APPLE_SIZE, SCREEN_HEIGHT),
                           APPLE_COLOR)

        # Create Foodie
        self.foodie = Snake((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),
                            DEFAULT_DIRECTION, FOODIE_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.apple.draw_apple()
        self.foodie.draw_snake()

    def update(self, delta_time):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        game_over = False
        game_state = self.foodie.check_collision(self.apple.x, self.apple.y)
        self.foodie.update_position(game_state)

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
