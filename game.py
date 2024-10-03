import pygame
from snake import Snake
from food import Food

YELLOW = (255, 255, 102)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.snake_head = self.snake.body[0]
        self.food = Food()
        pygame.init()
        self.score_font = pygame.font.SysFont("comicsansms", 30)
        self.font_style = pygame.font.SysFont("bahnschrift", 20)
        self.snake_speed = 15  # frame speed
        self.block_size = 10  # size of every block
        self.x_change = self.block_size
        self.y_change = 0
        self.score = 0
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))  # create screen
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_is_on = True
        self.game_is_over = False
        self.draw_snake()

    def run(self):
        self.reset_game()
        while self.running:
            # -------------Listen for Keys-----------
            for event in pygame.event.get():  # loop through events
                if event.type == pygame.QUIT:  # listen for close button on window
                    self.running = False  # stop the loop
                    return
                elif event.type == pygame.KEYDOWN:  # key is pressed down
                    if event.key == pygame.K_LEFT and self.x_change == 0:  # turn left
                        self.x_change = -self.block_size
                        self.y_change = 0
                    elif event.key == pygame.K_RIGHT and self.x_change == 0:  # turn right
                        self.x_change = self.block_size
                        self.y_change = 0
                    elif event.key == pygame.K_UP and self.y_change == 0:  # turn up
                        self.x_change = 0
                        self.y_change = -self.block_size
                    elif event.key == pygame.K_DOWN and self.y_change == 0:  # turn down
                        self.x_change = 0
                        self.y_change = self.block_size
                # ---------------------------------------------------------------------
            self.screen.fill('black')
            self.draw_snake()
            self.draw_food()
            self.show_score()
            self.snake.move([self.x_change, self.y_change])  # move snake
            self.snake_head = self.snake.body[0]
            if self.food.position == self.snake_head:  # snake eats food
                self.score += 1
                self.snake.grow()
                while self.food.position in self.snake.body:  # generate new location if food pos is on snake body
                    self.food.regenerate(self.width, self.height, self.block_size)  # regenerate food

            if self.snake_head in self.snake.body[1:]:  # snake hit itself
                self.game_is_over = True
                break

            if (self.snake_head[0] >= self.width or self.snake_head[0] < 0 or
                    self.snake_head[1] >= self.height or self.snake_head[1] < 0):  # snake hits the wall
                self.game_is_over = True
                break

            pygame.display.update()  # update screen
            self.clock.tick(self.snake_speed)  # adjust the frames per second

        # Once the loop breaks, call the game over screen if necessary
        if self.game_is_over:
            self.end_game()

    def draw_snake(self):
        for body in self.snake.body:  # draw snake on the screen based on snake's position
            pygame.draw.rect(self.screen, "green", [body[0], body[1], self.block_size, self.block_size])

    def draw_food(self):  # draw food on screen
        pygame.draw.rect(self.screen, "red", [self.food.position[0], self.food.position[1],
                                              self.block_size, self.block_size])

    def show_score(self):
        value = self.score_font.render(f"Score: {self.score}", True, YELLOW)
        self.screen.blit(value, [0, 0])

    def game_on(self):
        while self.game_is_on:
            self.run()
            if not self.running:  # If the player has chosen to quit, stop the game loop
                self.game_is_on = False

    def end_game(self):
        value = self.font_style.render("Game Over. Press Enter to play again, Q to quit.", False, YELLOW)
        self.screen.fill('blue')  # fill screen with blue for game over
        self.screen.blit(value, [self.width / 6, self.height / 2])
        pygame.display.update()

        while self.game_is_over:
            for event in pygame.event.get():  # loop through events
                if event.type == pygame.QUIT:  # listen for close button on window
                    self.running = False
                    self.game_is_over = False
                    return  # Exit game loop
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:  # close the game if q key pressed
                        self.running = False
                        self.game_is_over = False
                        return  # Exit game loop
                    elif event.key == pygame.K_RETURN:  # rerun game if enter key pressed
                        self.game_is_over = False
                        self.run()  # Restart the game

    def reset_game(self):  # reset game values
        self.snake.reset()
        self.x_change = self.block_size
        self.y_change = 0
        self.score = 0
