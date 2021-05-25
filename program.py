# Basic arcade program
# Tutorial at https://realpython.com/arcade-python-game-framework/#basic-arcade-program

# Imports
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Player Two has entered the game"
RADIUS = 150
SCALING = 2.0


# Classes
class Multiplayer(arcade.Window):
    def __init__(self, width, height, title):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(width, height, title)
        self.paused = False

        # Set up the empty sprite lists
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

        # Set up the player
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png", 0.7)
        self.player.center_y = self.height / 2
        self.player.left = 310
        self.all_sprites.append(self.player)

        self.player2 = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_walk0.png", 0.7)
        self.player2.center_y = self.height / 2
        self.player2.right = 450
        self.all_sprites.append(self.player2)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W:
            self.player.change_y = 5

        if symbol == arcade.key.S:
            self.player.change_y = -5

        if symbol == arcade.key.A:
            self.player.change_x = -5

        if symbol == arcade.key.D:
            self.player.change_x = 5

        if symbol == arcade.key.UP:
            self.player2.change_y = 5

        if symbol == arcade.key.DOWN:
            self.player2.change_y = -5

        if symbol == arcade.key.LEFT:
            self.player2.change_x = -5

        if symbol == arcade.key.RIGHT:
            self.player2.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0

        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player2.change_y = 0
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player2.change_x = 0

    def on_update(self, delta_time):
        if self.paused:
            return

        self.all_sprites.update()

        # Keep the player on the screen
        if self.player.top > self.height:
            self.player.top = self.height

        if self.player.right > self.width:
            self.player.right = self.width

        if self.player.bottom < 0:
            self.player.bottom = 0

        if self.player.left < 0:
            self.player.left = 0

        if self.player2.top > self.height:
            self.player2.top = self.height

        if self.player2.right > self.width:
            self.player2.right = self.width

        if self.player2.bottom < 0:
            self.player2.bottom = 0

        if self.player2.left < 0:
            self.player2.left = 0

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        self.all_sprites.draw()

        text_x = 150
        text_y = 350
        arcade.draw_text("Use W-A-S-D and Arrow Keys.", text_x, text_y, arcade.color.BLACK, font_size=30, font_name="LiberationSans-Regular")


# main code entry point
if __name__ == "__main__":
    app = Multiplayer(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
    app.setup()
    arcade.run()
