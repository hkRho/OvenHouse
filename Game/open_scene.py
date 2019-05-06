import pygame
import show_text as st
import choose_char as cc
import instructions as ins

def start():
    return cc.main()
def instructions():
    return ins.main()

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    window = pygame.display.set_mode((screen_width, screen_height))
    running = True
    line_space = 32
    basicfont = pygame.font.Font('8bitoperator.ttf', 20)
    Rectplace = pygame.draw.rect(window, (0, 0, 0),(100, 200, 100, 100))
    Rectplace2 = pygame.draw.rect(window, (0, 0, 0),(250, 200, 200, 100))

    st.text_ani('Ovenhouse', (0, 1), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Start', (-100, 3), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('instructions', (100, 3), line_space,basicfont,window,screen_width, screen_height)

    pygame.display.update()
    while running:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        if Rectplace.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("Start")
            return start()

        if Rectplace2.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("Instructions")
            running = False
            return instructions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
