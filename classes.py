import pygame

white = (255, 255, 255)
c_circle = (120, 0, 255)
c_wall = (255, 100, 0)
r_apple = 15
r_circle = 20


class Board:
    def __init__(self, cells):
        self.x = cells
        self.y = cells
        self.board = [[0] * cells for _ in range(cells)]
        self.left = 10
        self.top = 10
        self.size = 10
        self.long = cells * self.size + self.left * 2
        self.walls = list()
        for j in range(self.x):
            for i in range(self.y):
                self.board[i][j] = [self.left + self.size * j, self.top + self.size * i, (127, 255, 0), 0]

    def set_view(self, left, top, size):
        self.left = left
        self.top = top
        self.size = size

    def render(self, screen):
        for j in range(self.x):
            for i in range(self.y):
                pygame.draw.rect(screen, white,
                                 (self.left + self.size * j, self.top + self.size * i,
                                  self.size, self.size), 1)

    def get_coord(self, pos):
        for i in range(self.y):
            for j in range(self.x):
                if self.board[i][j][0] <= pos[0] <= self.board[i][j][0] + self.size and \
                        self.board[i][j][1] <= pos[1] <= self.board[i][j][1] + self.size:
                    return j, i
        return None


class Apple:
    def __init__(self, coords):
        self.coords = coords
        self.left_up_x = coords[0] - r_apple
        self.left_up_y = coords[1] - r_apple


class Status:
    def __init__(self, screen):
        self.font_name = pygame.font.match_font('arial')
        self.screen = screen
        self.pause = False
        self.game = 0

    def draw_score(self, score):
        font = pygame.font.Font(self.font_name, 40)
        text_surface = font.render("Score: " + str(score), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (360, 20)
        self.screen.blit(text_surface, text_rect)

    def draw_pause(self):
        if self.pause:
            font = pygame.font.Font(self.font_name, 60)
            text_surface = font.render("PAUSE", True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (360, 300)
            self.screen.blit(text_surface, text_rect)

    def draw_game_over(self):
        if self.game == 2:
            font = pygame.font.Font(self.font_name, 60)
            text_surface = font.render("GAME OVER", True, (0, 0, 0))
            text_surface_1 = font.render("Press Esc to exit the game", True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect_1 = text_surface_1.get_rect()
            text_rect.midtop = (360, 300)
            text_rect_1.midtop = (360, 400)
            self.screen.blit(text_surface, text_rect)
            self.screen.blit(text_surface_1, text_rect_1)

    def draw_start(self):
        if self.game == 0:
            font = pygame.font.Font(self.font_name, 40)
            text_surface_1 = font.render("Press Backspace to start", True, (0, 0, 0))
            text_surface_2 = font.render("Press Esc to pause", True, (0, 0, 0))
            text_surface_3 = font.render("Press R to play again", True, (0, 0, 0))
            text_rect_1 = text_surface_1.get_rect()
            text_rect_2 = text_surface_2.get_rect()
            text_rect_3 = text_surface_3.get_rect()
            text_rect_1.midtop = (360, 100)
            text_rect_2.midtop = (360, 200)
            text_rect_3.midtop = (360, 300)
            self.screen.blit(text_surface_1, text_rect_1)
            self.screen.blit(text_surface_2, text_rect_2)
            self.screen.blit(text_surface_3, text_rect_3)