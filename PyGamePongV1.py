import pygame

# User-defined functions

def main():
    pygame.init()
    pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Pong')
    w_surface = pygame.display.get_surface()
    game = Game(w_surface)
    game.play()
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
        self.small_dot = Ball('white', 8, [50, 50], [1, 2], self.surface)
        self.left_paddle = paddle('white',50,150,20,80,self.surface)
        self.right_paddle = paddle('white',420,150,20,80,self.surface)
        #self.max_frames = 150
        #self.frame_counter = 0

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
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

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        self.small_dot.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
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


class paddle():
    def __init__(self,colour,x,y,length,width,surface):
        self.color = pygame.Color(colour)
        self.pos = [x,y]
        self.dim = [length,width]
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface,self.color,(self.pos,self.dim))



main()
