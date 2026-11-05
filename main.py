import pygame
import math
pygame.init()

'''
Day 1
Add money text and income text
Add test button
Make it round to nearest whole number
Add a sin wave to make it look cool

Day 2
Add GPU clicking system
Make it add income once clicked
Replace test button with gpu
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

GPU1Sprite = pygame.image.load("imgs/GPU1.png").convert_alpha()
GPU1Sprite = pygame.transform.scale(GPU1Sprite, (220, 200))

BigGPU1Sprite = pygame.image.load("imgs/GPU1.png").convert_alpha()
BigGPU1Sprite = pygame.transform.scale(BigGPU1Sprite, (330, 300))

GPURect = pygame.Rect(450, 20, 220, 200)

CurrentGPU = "GPU1"
CurrentGPUSPRITE = GPU1Sprite
CURRENTINCOME = 1
CURRENTMONEY = 0

ANGLE = 0
ROTATIONSPEED = 0.3

LastIncomeTime = pygame.time.get_ticks()

GameRunning = True
while GameRunning:
    # Income text 
    CurrentDisplayedMoney = round(CURRENTMONEY)
    CurrentDisplayedIncome = round(CURRENTINCOME)
    CurrentTime = pygame.time.get_ticks()

    # Sin wave stuff 
    MoneyFloat = math.sin(CurrentTime * 0.003) * 6
    IncomeFloat = math.sin(CurrentTime * 0.005) * 5

    # Gpu Rotation
    ANGLE += ROTATIONSPEED

    if CurrentTime - LastIncomeTime >= 1000:
        CURRENTMONEY += CURRENTINCOME
        LastIncomeTime = CurrentTime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePosition = pygame.mouse.get_pos()
            if GPURect.collidepoint(MousePosition):
                CURRENTINCOME += 1
                if CurrentGPU == GPU1Sprite:
                    CurrentGPU = BigGPU1Sprite
        else:
            if CurrentGPU == BigGPU1Sprite:
                CurrentGPU = GPU1Sprite

    if CurrentGPU == "GPU1":
        CurrentGPU = GPU1Sprite

    Money = str(CurrentDisplayedMoney)
    Income = str(CurrentDisplayedIncome)
    window.blit(Background, (0, 0))

    # Money stuff
    window.blit(MoneySprite, (50, 20 + MoneyFloat))
    MoneyText = RegularFont.render(Money, True, (0, 0, 0))
    window.blit(MoneyText, (150, 10 + MoneyFloat))

    IncomeText = RegularFont.render(f"{Income} /s", True, (0, 0, 0))
    window.blit(IncomeText, (50, 100 + IncomeFloat))

    GPURotated = pygame.transform.rotate(CurrentGPU, ANGLE)

    UpdatedGpuRect = GPURotated.get_rect(center=GPURect.center)
    window.blit(GPURotated, UpdatedGpuRect.topleft)

    clock.tick(60)
    pygame.display.flip()