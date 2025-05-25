import pygame as pg
import input
import  function

pg.init()
screen = pg.display.set_mode((720, 720))
clock = pg.time.Clock()
running = True
font = pg.font.SysFont('Arial', 150)

cercles = []  # stocke les positions des cercles à dessiner
croix = []  # stocke les positions des croix à dessiner

def draw_cross(center, width=50):
    size = 100
    half_size = size // 2
    x, y = center

    # Ligne de haut gauche à bas droite
    pg.draw.line(screen, pg.Color("blue"), (x - half_size, y - half_size), (x + half_size, y + half_size), width)

    # Ligne de bas gauche à haut droite
    pg.draw.line(screen, pg.Color("blue"), (x - half_size, y + half_size), (x + half_size, y - half_size), width)

def grilles():
    screen.fill("white")
    # Grille verticale
    pg.draw.line(screen, pg.Color("black"), (240, 0), (240, 720))
    pg.draw.line(screen, pg.Color("black"), (480, 0), (480, 720))
    # Grille horizontale
    pg.draw.line(screen, pg.Color("black"), (0, 240), (720, 240))
    pg.draw.line(screen, pg.Color("black"), (0, 480), (720, 480))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            joueur = function.joueur
            x, y = pg.mouse.get_pos()
            pos = input.DetectClicked(x, y)
            if button_rect.collidepoint(x, y):
                function.ResetGame()
                cercles = []
                croix = []
            elif pos:
                if joueur == 1:
                    cercles.append(pos)
                else:
                    croix.append(pos)




    grilles()

    # dessiner les cercles
    for pos in cercles:
        pg.draw.circle(screen, pg.Color("red"), pos, 100)

    for pos in croix:
        draw_cross(pos)

    if function.win != 0:
        screen.fill("white")
        if function.win == 1:
            font = pg.font.SysFont('Arial', 100)
            text = font.render("Player 1 wins!", True, pg.Color("blue"))
            text_rect = text.get_rect(center=(360, 360))
            screen.blit(text, text_rect)
        elif function.win == 4:
            font = pg.font.SysFont('Arial', 100)
            text = font.render("Player 2 wins!", True, pg.Color("red"))
            text_rect = text.get_rect(center=(360, 360))
            screen.blit(text, text_rect)

    # --- Dessiner le bouton REJOUER ---
    button_rect = pg.Rect(260, 660, 200, 40)
    pg.draw.rect(screen, (200, 200, 200), button_rect)
    font_button = pg.font.SysFont(None, 40)
    text_button = font_button.render("Rejouer", True, (0, 0, 0))
    text_button_rect = text_button.get_rect(center=button_rect.center)
    screen.blit(text_button, text_button_rect)

    pg.display.flip()
    clock.tick(60)

pg.quit()