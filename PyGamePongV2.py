import pygame

# User-defined functions
score = 0
score2 = 0

def interact(paddle,ball):
    if ball.center[0] > paddle.x and ball.center[0] < (paddle.x + paddle.length):
        if ball.center[1] > paddle.y - 30 and ball.center[1] < paddle.y + paddle.width + 20:
            return True


def main():
    pygame.init()
    pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Pong')
    w_surface = pygame.display.get_surface()
    game = Game(w_surface)
    game.play(score,score2)
    pygame.quit()

# User-defined classes

class Game:
    # An object in this class represents a complete game.
    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object
        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        # === game specific objects
        self.small_dot = Ball('white', 8, [150, 80], [5,5], self.surface)
        self.left_paddle = Paddle('white',50,150,20,80,self.surface)
        self.right_paddle = Paddle('white',420,150,20,80,self.surface)
        self.contact_paddle_left = Paddle('white', 65, 150, 10, 80, self.surface)
        self.contact_paddle_right = Paddle('white', 420, 150, 10, 80, self.surface)
        #self.max_frames = 150
        #self.frame_counter = 0

    def play(self,score,score2):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()

            if interact(self.contact_paddle_right,self.small_dot):
                if self.small_dot.velocity[0] > 0:
                    self.small_dot.hit()

            if interact(self.contact_paddle_left,self.small_dot):
                if self.small_dot.velocity[0] < 0:
                    self.small_dot.hit()

            score,score2 = self.small_dot.ScoreUp(score,score2)
            self.draw(score,score2)
            if self.continue_game:
                self.update()
                #self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self,score,score2):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        font = pygame.font.SysFont("arial", 25, True)
        text = font.render('Score:' + str(score2), 1, (245, 56, 78))
        self.surface.blit(text, (390, 10))
        font = pygame.font.SysFont("arial", 25, True)
        text = font.render('Score:' + str(score), 1, (245, 56, 78))
        self.surface.blit(text, (50, 10))
        self.small_dot.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.contact_paddle_left.draw()
        self.contact_paddle_right.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        self.small_dot.move()
        self.small_dot.change_vel()
        #self.frame_counter = self.frame_counter + 1

    #def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

     #   if self.frame_counter > self.max_frames:
      #      self.continue_game = False


class Ball:
    # An object in this class represents a Dot that moves

    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
        self.color = pygame.Color(dot_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface

    def move(self):
        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def change_vel(self):
        if self.center[0] > 490 or self.center[0] < 0:
            self.velocity[0] = self.velocity[0] * -1

        if self.center[1] > 390 or self.center[1] < 0:
            self.velocity[1] = self.velocity[1] * -1

    def hit(self):
        self.velocity[0] = self.velocity[0] * -1

    def ScoreUp(self,score,score2):
        if self.center[0] > 490:
            score = score+1

        if self.center[0] < 0:
            score2 = score2+1

        return score,score2
class Paddle:
    def __init__(self,colour,x,y,length,width,surface):
        self.color = pygame.Color(colour)
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.pos = [x,y]
        self.dim = [length,width]
        self.surface = surface
        self.Rect = [self.surface,self.color,(self.pos,self.dim)]

    def draw(self):
        pygame.draw.rect(self.surface,self.color,(self.pos,self.dim))


main()
