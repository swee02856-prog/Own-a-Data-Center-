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

Day 3
Fully implement all Gpus into GPU shop
Make the Money multiplier fully work
Start on the other upgrades
'''
clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Build a Data Center!")

popsound = pygame.mixer.Sound("sounds/pop.mp3")

BuyButton = pygame.image.load("imgs/BuyButton.png").convert_alpha()
BuyButton = pygame.transform.scale(BuyButton, (200, 180))

BuyButtonRect = BuyButton.get_rect(topleft=(50, 400))

PriceBackground = pygame.image.load("imgs/PriceBackground.png").convert_alpha()
PriceBackground = pygame.transform.scale(PriceBackground, (200, 140))

TestImage = pygame.image.load("imgs/cat.png").convert_alpha()
BigTestImage = pygame.transform.scale(TestImage, (180, 180))
SmallTestImage = pygame.transform.scale(TestImage, (150, 150))

TestImageRect = TestImage.get_rect(topleft=(75, 220))

RegularFont = pygame.font.Font(("Kalam-Regular.ttf"), 80)
SmallerFont = pygame.font.Font(("Kalam-Regular.ttf"), 40)

Background = pygame.surface.Surface((800, 600))
Background.fill((255, 255, 255))

MoneySprite = pygame.image.load("imgs/Money.png").convert_alpha()
MoneySprite = pygame.transform.scale(MoneySprite, (100, 50))

GPU1Sprite = pygame.image.load("imgs/GPU1.png").convert_alpha()
GPU1Sprite = pygame.transform.scale(GPU1Sprite, (220, 200))

BigGPU1Sprite = pygame.image.load("imgs/GPU1.png").convert_alpha()
BigGPU1Sprite = pygame.transform.scale(BigGPU1Sprite, (275, 250))

GPURect = pygame.Rect(450, 20, 220, 200)

StartingGPU = GPU1Sprite

CurrentGPU = StartingGPU
CurrentGPUSPRITE = StartingGPU

IncomeMultiplier = 1
CURRENTINCOME = 1
CURRENTMONEY = 0

ANGLE = 0
ROTATIONSPEED = 0.3

LastIncomeTime = pygame.time.get_ticks()

GameRunning = True
while GameRunning:
    MousePosition = pygame.mouse.get_pos()
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
            if UpdatedGpuRect.collidepoint(MousePosition):
                popsound.play()
                CURRENTINCOME += 1
                if CurrentGPU == GPU1Sprite:
                    CurrentGPU = BigGPU1Sprite
            
            if BuyButtonRect.collidepoint(MousePosition):
                IncomeMultiplier = 2
                CURRENTINCOME = CURRENTINCOME * IncomeMultiplier

        else:
            if CurrentGPU == BigGPU1Sprite:
                CurrentGPU = GPU1Sprite


    if TestImageRect.collidepoint(MousePosition):
        TestImage = BigTestImage
    else:
        TestImage = SmallTestImage
    Money = str(CurrentDisplayedMoney)
    Income = str(CurrentDisplayedIncome)
    window.blit(Background, (0, 0))

    # Money stuff
    window.blit(MoneySprite, (50, 20 + MoneyFloat))
    MoneyText = RegularFont.render(Money, True, (0, 0, 0))
    window.blit(MoneyText, (150, 10 + MoneyFloat))

    IncomeText = RegularFont.render(f"{Income} /s", True, (0, 0, 0))
    window.blit(IncomeText, (50, 100 + IncomeFloat))

    # Gpu stuff & Buy stuff
    GPURotated = pygame.transform.rotate(CurrentGPU, ANGLE)
    UpdatedGpuRect = GPURotated.get_rect(center=GPURect.center)
    window.blit(GPURotated, UpdatedGpuRect.topleft)

    window.blit(BuyButton, (50, 400))
    window.blit(PriceBackground, (50, 350))

    # Test image
    window.blit(TestImage, (TestImageRect))

    clock.tick(60)
    pygame.display.flip()