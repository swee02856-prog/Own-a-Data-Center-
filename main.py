import pygame
import math
pygame.init()

'''Day 1
Add money text and income text
Add test button
Make it round to nearest whole number
Add a sin wave to make it look cool
'''

clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Build a Data Center!")

RegularFont = pygame.font.Font(("Kalam-Regular.ttf"), 80)
SmallerFont = pygame.font.Font(("Kalam-Regular.ttf"), 40)

Background = pygame.surface.Surface((800, 600))
Background.fill((255, 255, 255))

MoneySprite = pygame.image.load("imgs/Money.png").convert_alpha()
MoneySprite = pygame.transform.scale(MoneySprite, (100, 50))

TestButton = pygame.surface.Surface((200, 100))
TestButton.fill((0, 0, 0))

TestButtonRect = pygame.Rect(50, 250, 200, 100)

CurrentIncome = 1
CurrentMoney = 0

LastIncomeTime = pygame.time.get_ticks()

GameRunning = True
while GameRunning:
    # Income text 
    CurrentDisplayedMoney = round(CurrentMoney)
    CurrentDisplayedIncome = round(CurrentIncome)
    CurrentTime = pygame.time.get_ticks()

    # Sin wave stuff 
    MoneyFloat = math.sin(CurrentTime * 0.003) * 6
    IncomeFloat = math.sin(CurrentTime * 0.005) * 5
    if CurrentTime - LastIncomeTime >= 1000:
        CurrentMoney += CurrentIncome
        LastIncomeTime = CurrentTime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePosition = pygame.mouse.get_pos()
            if TestButtonRect.collidepoint(MousePosition):
                CurrentIncome += 0.1

    Money = str(CurrentDisplayedMoney)
    Income = str(CurrentDisplayedIncome)
    window.blit(Background, (0, 0))

    window.blit(MoneySprite, (50, 20 + MoneyFloat))
    MoneyText = RegularFont.render(Money, True, (0, 0, 0))
    window.blit(MoneyText, (150, 10 + MoneyFloat))

    IncomeText = RegularFont.render(f"{Income} /s", True, (0, 0, 0))
    window.blit(IncomeText, (50, 100 + IncomeFloat))

    window.blit(TestButton, TestButtonRect)

    clock.tick(60)
    pygame.display.flip()