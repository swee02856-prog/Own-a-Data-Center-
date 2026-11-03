import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Build a Data Center!")

RegularFont = pygame.font.Font(("Kalam-Regular.ttf"), 80)

Background = pygame.surface.Surface((800, 600))
Background.fill((255, 255, 255))

MoneySprite = pygame.image.load("imgs/Money.png").convert_alpha()
MoneySprite = pygame.transform.scale(MoneySprite, (100, 50))

TestButton = pygame.surface.Surface((200, 100))
TestButton.fill((0, 0, 0))

TestButtonRect = pygame.Rect(50, 300, 200, 100)

CurrentIncome = 0
CurrentMoney = 0

GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePosition = pygame.mouse.get_pos()
            if TestButtonRect.collidepoint(MousePosition):
                CurrentIncome += 2


    Money = str(CurrentMoney)
    Income = str(CurrentIncome)
    window.blit(Background, (0, 0))

    window.blit(MoneySprite, (50, 20))
    MoneyText = RegularFont.render(Money, True, (0, 0, 0))
    window.blit(MoneyText, (150, 10))

    IncomeText = RegularFont.render(f"{Income} /s", True, (0, 0, 0))
    window.blit(IncomeText, (50, 100))

    window.blit(TestButton, (50, 300))

    pygame.display.flip()