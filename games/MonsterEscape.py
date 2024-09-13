# README

### Name: Monster Escape

### How to play: 
# There is one player Robot who needs to collect a number of coins and avoid the monsters. 
# A billboard is indicating how many coins the player has collected.
# If the robot travels through the door which will bring it to the opposite side of the ground.

### How to win: 
# The robot collects 10 coins and avoid the monsters.

### How to lose:
# If the robot meets the monster, game is over.

# features:
# constantly moving: monsters(horizontal)
# controled by keyboard: robot(all directions)
# immediate updates: billborad (count coins), coin's position
# static: doors

import pygame
from random import randint

class MonsterEscape:
    def __init__(self):
        pygame.init()
        
        # set the width and height of the window
        self.width = 640
        self.height = 480

        # track the game state
        self.game_over = False

        # load the images
        self.load_images()

        # launch a new game
        self.new_game()

        # set window
        self.window = pygame.display.set_mode((self.width, self.height))

        # set the font for all the text
        self.font = pygame.font.SysFont("Arial", 24)

        # window's title
        pygame.display.set_caption("Monster Escape")

        # initialize game elements
        self.robot_pos = self.robot()  # store robot's position
        self.monsters_list = self.init_monsters()  # initialize monsters
        self.coins = 0  # track collected coins
        self.coin_pos = self.generate_coin_position()  # generate initial coin position

        # execute the game
        self.main_loop()

    def load_images(self):
        # load all images
        self.robot_img = pygame.image.load("robot.png")
        self.monster_img = pygame.image.load("monster.png")
        self.coin_img = pygame.image.load("coin.png")
        self.door_img = pygame.image.load("door.png")

    def new_game(self):
        self.coins = 0  # reset coins at the start of the game

    def init_monsters(self):
        # create a list of monsters with different speeds
        monsters = []
        for i in range(3):
            monster = {
                "x": randint(0, self.width - self.monster_img.get_width()),
                "y": (i + 1) * 100,  # Each monster in a different row
                "speed": (i + 1)  # Each monster has a different speed
            }
            monsters.append(monster)
        return monsters

    def move_monsters(self):
        # update monster positions
        for monster in self.monsters_list:
            monster["x"] += monster["speed"]
            if monster["x"] > self.width:
                monster["x"] = -self.monster_img.get_width()  # wrap around

    def robot(self):
        # initial robot position at the bottom
        robot_width = self.robot_img.get_width()
        robot_height = self.robot_img.get_height()
        # return a dictionary for later updates
        return {"x": self.width // 2 - robot_width // 2, "y": self.height - robot_height}

    def move_robot(self, move_x, move_y):
        # move robot based on keyboard input
        self.robot_pos["x"] += move_x
        self.robot_pos["y"] += move_y

        # ensure the robot stays within bounds
        if self.robot_pos["x"] < 0:
            self.robot_pos["x"] = 0
        elif self.robot_pos["x"] > self.width - self.robot_img.get_width():
            self.robot_pos["x"] = self.width - self.robot_img.get_width()

        if self.robot_pos["y"] < 0:
            self.robot_pos["y"] = 0
        elif self.robot_pos["y"] > self.height - self.robot_img.get_height():
            self.robot_pos["y"] = self.height - self.robot_img.get_height()
    
    def meet_monster(self):
    # get the robot's dimensions
        robot_width = self.robot_img.get_width()
        robot_height = self.robot_img.get_height()

        # loop through all monsters and check if the robot touches any of them
        for monster in self.monsters_list:
            if (self.robot_pos["x"] < monster["x"] + self.monster_img.get_width() and
                self.robot_pos["x"] + robot_width > monster["x"] and
                self.robot_pos["y"] < monster["y"] + self.monster_img.get_height() and
                self.robot_pos["y"] + robot_height > monster["y"]):
                
                # if the robot touches a monster, set game_over to True
                self.game_over = True

    def meet_door(self):
        # get the robot's dimensions
        robot_width = self.robot_img.get_width()
        robot_height = self.robot_img.get_height()

        # get the door's dimensions
        door_width = self.door_img.get_width()
        door_height = self.door_img.get_height()

        door_x = (self.width // 2) - (door_width // 2)
        door_y = 0

        # check if the robot's position overlaps with the door's position
        if (self.robot_pos["x"] < door_x + door_width and
            self.robot_pos["x"] + robot_width > door_x and
            self.robot_pos["y"] < door_y + door_height and
            self.robot_pos["y"] + robot_height > door_y):
            # when meet the door, move to the opposite side
            # invert the y-coordinate
            self.robot_pos["y"] = self.height - robot_height

    def check_coin_collection(self):
        # check if robot is collecting coins
        if (self.robot_pos["x"] < self.coin_pos[0] + self.coin_img.get_width() and
        self.robot_pos["x"] + self.robot_img.get_width() > self.coin_pos[0] and
        self.robot_pos["y"] < self.coin_pos[1] + self.coin_img.get_height() and
        self.robot_pos["y"] + self.robot_img.get_height() > self.coin_pos[1]):
            self.coins += 1  # add up coins count
            self.coin_pos = self.generate_coin_position()  # generate a new coin position after collection

    def generate_coin_position(self):
        # randomize the coin's position
        c_x = randint(0, self.width - self.coin_img.get_width())
        c_y = randint(0, self.height - self.coin_img.get_height())
        return c_x, c_y

    def draw_window(self):
        # fill the screen with a background color
        self.window.fill((20, 190, 20))

        # draw the robot
        self.window.blit(self.robot_img, (self.robot_pos["x"], self.robot_pos["y"]))

        # draw monsters
        for monster in self.monsters_list:
            self.window.blit(self.monster_img, (monster["x"], monster["y"]))

        # draw the coin
        self.window.blit(self.coin_img, self.coin_pos)

        # draw the door
        # initialize a position to the door
        door_x = (self.width // 2) - (self.door_img.get_width() // 2)
        door_y = 0
        self.window.blit(self.door_img, (door_x, door_y))
        
        # display the collected coin count
        coin_text = self.font.render(f"Coins (10 to win): {self.coins}", True, (255, 255, 255))
        self.window.blit(coin_text, (10, 10))

        # display the hint
        game_text = self.font.render("Esc = Exit game", True, (255, 255, 255))
        self.window.blit(game_text, (self.width - game_text.get_width(), 10))            
        
        pygame.display.update()

    def main_loop(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(30)  # limit the frame rate to 30 FPS

            # handle events (allow restarting or quitting even when game over)
            self.check_events()

            # only move the monsters and check collisions if the game is not over
            if not self.game_over:
                # move monsters
                self.move_monsters()

                # check for coin collection
                self.check_coin_collection()

                # check if the robot meets a monster
                self.meet_monster()

                # check if the robot meets the door
                self.meet_door()

                # check if the player has collected 10 coins
                if self.coins == 10:
                    self.game_over = True
                    self.display_game_win_text()  # display win message

            # draw everything, including game over or win message if needed
            self.draw_window()

            if self.game_over:
                if self.coins == 10:
                    self.display_game_win_text()  # show win text
                else:
                    self.display_game_over_text()  # show game over text

    def display_game_win_text(self):
        win_text = ["Congratulations!", "You win!", "F2 --> restart", "Esc --> quit"]
        interval = 10
        for text in win_text:
            interval += 30
            dis_text = self.font.render(text, True, (0, 0, 200))
            self.window.blit(dis_text, (self.width / 2 - dis_text.get_width() / 2, self.height / 4 + interval))

        pygame.display.update()

    def display_game_over_text(self):
        lose_text = ["---Game Over---", "F2 --> restart", "Esc --> quit"]
        interval = 10
        for text in lose_text:
            interval += 30
            dis_text = self.font.render(text, True, (200, 0, 0))
            self.window.blit(dis_text, (self.width / 2 - dis_text.get_width() / 2, self.height / 4 + interval))
        
        pygame.display.update()  # Ensure the "Game Over" text is shown on screen

    def new_game(self):
        self.coins = 0
        self.robot_pos = self.robot()
        self.monsters_list = self.init_monsters()  # re-initialize monsters
        self.coin_pos = self.generate_coin_position()  # re-position coin
        self.game_over = False  # make sure the game isn't in a game over state

    def check_events(self):
        # handle keyboard and window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_robot(-20, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_robot(20, 0)
                elif event.key == pygame.K_UP:
                    self.move_robot(0, -20)
                elif event.key == pygame.K_DOWN:
                    self.move_robot(0, 20)
                elif event.key == pygame.K_F2 and self.game_over:
                    self.new_game()  # restart the game
                    self.game_over = False  # reset the game over flag
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    MonsterEscape()
