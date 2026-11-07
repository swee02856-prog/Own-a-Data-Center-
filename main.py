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
moneysound = pygame.mixer.Sound("sounds/money.mp3")

BuyButton = pygame.image.load("imgs/BuyButton.png").convert_alpha()
SmallBuyButton = pygame.transform.scale(BuyButton, (200, 180))
BigBuyButton = pygame.transform.scale(BuyButton, (250, 230))

BuyButtonRect = BuyButton.get_rect(topleft=(50, 450))

PriceBackground = pygame.image.load("imgs/PriceBackground.png").convert_alpha()
PriceBackground = pygame.transform.scale(PriceBackground, (200, 140))

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

GPU2Sprite = pygame.image.load("imgs/GPU2.png").convert_alpha()
GPU2Sprite = pygame.transform.scale(GPU2Sprite, (240, 220))

BigGPU2Sprite = pygame.image.load("imgs/GPU2.png").convert_alpha()
BigGPU2Sprite = pygame.transform.scale(BigGPU2Sprite, (295, 270))

GPU3Sprite = pygame.image.load("imgs/GPU3.png").convert_alpha()
GPU3Sprite = pygame.transform.scale(GPU3Sprite, (260, 240))

BigGPU3Sprite = pygame.image.load("imgs/GPU3.png").convert_alpha()
BigGPU3Sprite = pygame.transform.scale(BigGPU3Sprite, (315, 290))

GPU4Sprite = pygame.image.load("imgs/GPU4.png").convert_alpha()
GPU4Sprite = pygame.transform.scale(GPU4Sprite, (270, 250))

BigGPU4Sprite = pygame.image.load("imgs/GPU4.png").convert_alpha()
BigGPU4Sprite = pygame.transform.scale(BigGPU4Sprite, (325, 300))

GPU2ExampleSprite = pygame.image.load("imgs/Rtx5060.png").convert_alpha()
GPU2ExampleSprite = pygame.transform.scale(GPU2ExampleSprite, (200, 200))

GPU3ExampleSprite = pygame.image.load("imgs/Rtx5090.png").convert_alpha()
GPU3ExampleSprite = pygame.transform.scale(GPU3ExampleSprite, (200, 200))

GPU4ExampleSprite = pygame.image.load("imgs/RtxServer6000.png").convert_alpha()
GPU4ExampleSprite = pygame.transform.scale(GPU4ExampleSprite, (200, 200))

GPURect = pygame.Rect(450, 20, 220, 200)

StartingGPU = GPU1Sprite

CurrentGPU = StartingGPU
CurrentGPUSPRITE = StartingGPU

IncomeMultiplier = 1
CURRENTINCOME = 0
CURRENTMONEY = 0

ANGLE = 0
ROTATIONSPEED = 0.3

LastIncomeTime = pygame.time.get_ticks()
GPUUPGRADE1PRICE = 600
GPUUPGRADE2PRICE = 5000
GPUUPGRADE3PRICE = 45000
CurrentGpuUpgradePrice = GPUUPGRADE1PRICE
CurrentUpgradedGPU = GPU2Sprite

GPU1ClickMultiplier = 1
GPU2ClickMultiplier = 2
GPU3ClickMultiplier = 3
GPU4ClickMultiplier = 4

CurrentMoneyMultiplier = GPU1ClickMultiplier
CurrentIncomeMultiplier = 1

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
                CURRENTMONEY += 1 * CurrentMoneyMultiplier
                # Gpu Big click effect
                if CurrentGPU == GPU1Sprite:
                    CurrentGPU = BigGPU1Sprite
                if CurrentGPU == GPU2Sprite:
                    CurrentGPU = BigGPU2Sprite
                if CurrentGPU == GPU3Sprite:
                    CurrentGPU = BigGPU3Sprite
                if CurrentGPU == GPU4Sprite:
                    CurrentGPU = BigGPU4Sprite
            
            if BuyButtonRect.collidepoint(MousePosition):
                if CURRENTMONEY >= CurrentGpuUpgradePrice:
                    CurrentGPU = CurrentUpgradedGPU
                    CURRENTMONEY -= CurrentGpuUpgradePrice
                    BuyButton = BigBuyButton
                    IncomeMultiplier = CurrentIncomeMultiplier
                    CURRENTINCOME = CURRENTINCOME * IncomeMultiplier
                    moneysound.play()
        else:
            # Gpu big click effect return
            if CurrentGPU == BigGPU1Sprite:
                CurrentGPU = GPU1Sprite
            if CurrentGPU == BigGPU2Sprite:
                CurrentGPU = GPU2Sprite
            if CurrentGPU == BigGPU3Sprite:
                CurrentGPU = GPU3Sprite
            if CurrentGPU == BigGPU4Sprite:
                CurrentGPU = GPU4Sprite
            BuyButton = SmallBuyButton

    window.blit(Background, (0, 0))
    # Draw or print stuff after this

    if CurrentGPU == GPU1Sprite:
        CurrentGpuUpgradePrice = GPUUPGRADE1PRICE
        window.blit(GPU2ExampleSprite, (30, 250))

    if CurrentGPU == GPU2Sprite:
        window.blit(GPU3ExampleSprite, (50, 250))
        CurrentGpuUpgradePrice = GPUUPGRADE2PRICE
        CurrentUpgradedGPU = GPU3Sprite
        CurrentMoneyMultiplier = GPU2ClickMultiplier

    if CurrentGPU == GPU3Sprite:
        window.blit(GPU4ExampleSprite, (50, 250))
        CurrentGpuUpgradePrice = GPUUPGRADE3PRICE
        CurrentMoneyMultiplier = GPU3ClickMultiplier
        CurrentUpgradedGPU = GPU4Sprite
    
    if CurrentGPU == GPU4Sprite:
        CurrentMoneyMultiplier = GPU4ClickMultiplier
        GPUMAXED = True
    
    BuyButtonRect = BuyButton.get_rect(topleft=(50, 450))
    
    Money = str(CurrentDisplayedMoney)
    Income = str(CurrentDisplayedIncome)

    window.blit(BuyButton, (50, 450))

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

    window.blit(PriceBackground, (50, 400))

    clock.tick(60)
    pygame.display.flip()