import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    KeyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(keyName))
    if KeyInput[mykey]:
        ans = True
        pygame.display.update()
        return ans

def main():
    if getkey("LEFT"):
        print("Vänster Knapp Tryckt")
    if getkey("RIGHT"):
        print("Höger Knapp Tryckt")


if __name__ == '__main__':
    init()
    while True:
        main()
