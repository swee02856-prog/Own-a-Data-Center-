import pygame
import math
import os
import sys
pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

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

Day 4
Add Sam altman character (make him change how he looks 
poor -> rich -> godly)
Add text just like from cookie clicker that moves across
the screen slowly highlighting the current state of the center
Start on the other upgrades
Add Worker shop
'''
clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Build a Data Center!")

popsound = pygame.mixer.Sound(resource_path("sounds/pop.mp3"))
moneysound = pygame.mixer.Sound(resource_path("sounds/money.mp3"))

debtimage = pygame.image.load(resource_path("imgs/debt.png")).convert_alpha()
debtimage = pygame.transform.scale(debtimage, (200, 200))

GpuBuyButton = pygame.image.load(resource_path("imgs/BuyButton.png")).convert_alpha()
SmallGpuBuyButton = pygame.transform.scale(GpuBuyButton, (200, 180))
BigGpuBuyButton = pygame.transform.scale(GpuBuyButton, (250, 230))

WorkerBuyButton = pygame.image.load(resource_path("imgs/BuyButton.png")).convert_alpha()
SmallWorkerBuyButton = pygame.transform.scale(WorkerBuyButton, (200, 180))
BigWorkerBuyButton = pygame.transform.scale(WorkerBuyButton, (250, 230))

DebtBuyButton = pygame.image.load(resource_path("imgs/BuyButton.png")).convert_alpha()
SmallDebtBuyButton = pygame.transform.scale(DebtBuyButton, (200, 180))
BigDebtBuyButton = pygame.transform.scale(DebtBuyButton, (250, 230))

RegularFont = pygame.font.Font(resource_path("Kalam-Regular.ttf"), 80)
SmallerFont = pygame.font.Font(resource_path("Kalam-Regular.ttf"), 60)
EvenSmallerFont = pygame.font.Font(resource_path("Kalam-Regular.ttf"), 30)
LargeFont = pygame.font.Font(resource_path("Kalam-Regular.ttf"), 110)

Background = pygame.surface.Surface((800, 600))
Background.fill((255, 255, 255))

FirstWorker = pygame.image.load(resource_path("imgs/Intern.png")).convert_alpha()
FirstWorker = pygame.transform.scale(FirstWorker, (200, 200))

SecondWorker = pygame.image.load(resource_path("imgs/LeetcodeTryhard.png")).convert_alpha()
SecondWorker = pygame.transform.scale(SecondWorker, (200, 200))

ThirdWorker = pygame.image.load(resource_path("imgs/LinusTechTips.png")).convert_alpha()
ThirdWorker = pygame.transform.scale(ThirdWorker, (200, 200))

FourthWorker = pygame.image.load(resource_path("imgs/LinusTorwalds.png")).convert_alpha()
FourthWorker = pygame.transform.scale(FourthWorker, (200, 200))

CurrentWorker = "None"

MoneySprite = pygame.image.load(resource_path("imgs/Money.png")).convert_alpha()
MoneySprite = pygame.transform.scale(MoneySprite, (100, 50))

GPU1Sprite = pygame.image.load(resource_path("imgs/GPU1.png")).convert_alpha()
GPU1Sprite = pygame.transform.scale(GPU1Sprite, (220, 200))

BigGPU1Sprite = pygame.image.load(resource_path("imgs/GPU1.png")).convert_alpha()
BigGPU1Sprite = pygame.transform.scale(BigGPU1Sprite, (275, 250))

GPU2Sprite = pygame.image.load(resource_path("imgs/GPU2.png")).convert_alpha()
GPU2Sprite = pygame.transform.scale(GPU2Sprite, (240, 220))

BigGPU2Sprite = pygame.image.load(resource_path("imgs/GPU2.png")).convert_alpha()
BigGPU2Sprite = pygame.transform.scale(BigGPU2Sprite, (295, 270))

GPU3Sprite = pygame.image.load(resource_path("imgs/GPU3.png")).convert_alpha()
GPU3Sprite = pygame.transform.scale(GPU3Sprite, (260, 240))

BigGPU3Sprite = pygame.image.load(resource_path("imgs/GPU3.png")).convert_alpha()
BigGPU3Sprite = pygame.transform.scale(BigGPU3Sprite, (315, 290))

GPU4Sprite = pygame.image.load(resource_path("imgs/GPU4.png")).convert_alpha()
GPU4Sprite = pygame.transform.scale(GPU4Sprite, (270, 250))

BigGPU4Sprite = pygame.image.load(resource_path("imgs/GPU4.png")).convert_alpha()
BigGPU4Sprite = pygame.transform.scale(BigGPU4Sprite, (325, 300))

GPU2ExampleSprite = pygame.image.load(resource_path("imgs/Rtx5060.png")).convert_alpha()
GPU2ExampleSprite = pygame.transform.scale(GPU2ExampleSprite, (200, 200))

GPU3ExampleSprite = pygame.image.load(resource_path("imgs/Rtx5090.png")).convert_alpha()
GPU3ExampleSprite = pygame.transform.scale(GPU3ExampleSprite, (200, 200))

GPU4ExampleSprite = pygame.image.load(resource_path("imgs/RtxServer6000.png")).convert_alpha()
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
GPUUPGRADE1PRICE = 300
GPUUPGRADE2PRICE = 1000
GPUUPGRADE3PRICE = 30000
CurrentGpuUpgradePrice = GPUUPGRADE1PRICE
CurrentUpgradedGPU = GPU2Sprite

WORKER1PRICE = 50
WORKER2PRICE = 300
WORKER3PRICE = 1500
WORKER4PRICE = 10000

CurrentWorkerUpgradePrice = WORKER1PRICE

GPU1ClickMultiplier = 1
GPU2ClickMultiplier = 2
GPU3ClickMultiplier = 3
GPU4ClickMultiplier = 4

CurrentMoneyMultiplier = GPU1ClickMultiplier
CurrentIncomeMultiplier = 1

NewsX = 0
NewsVelocityX = 2

CurrentMessage = "Your Services are like a ghost"

GPURotated = pygame.transform.rotate(CurrentGPU, ANGLE)
UpdatedGpuRect = GPURotated.get_rect(center=GPURect.center)

DebtCost = 50000

WORKERMAXED = False
GPUMAXED = False
GameFinished = False
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
            
            if GpuBuyButtonRect.collidepoint(MousePosition):
                if CURRENTMONEY >= CurrentGpuUpgradePrice:
                    CurrentGPU = CurrentUpgradedGPU
                    CURRENTMONEY -= CurrentGpuUpgradePrice
                    GpuBuyButton = BigGpuBuyButton
                    IncomeMultiplier = CurrentIncomeMultiplier
                    CURRENTINCOME = CURRENTINCOME * IncomeMultiplier
                    moneysound.play()
            if WorkerBuyButtonRect.collidepoint(MousePosition):
                if CURRENTMONEY >= CurrentWorkerUpgradePrice:
                    CURRENTMONEY -= CurrentWorkerUpgradePrice
                    WorkerBuyButton = BigWorkerBuyButton
                    CurrentWorker = UpgradedWorker
                    moneysound.play()
            if DebtBuyButtonRect.collidepoint(MousePosition):
                if CURRENTMONEY >= DebtCost:
                    CURRENTMONEY -= DebtCost
                    DebtBuyButton = BigDebtBuyButton
                    GameFinished = True
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
            GpuBuyButton = SmallGpuBuyButton
            WorkerBuyButton = SmallWorkerBuyButton
            DebtBuyButton = SmallDebtBuyButton

    window.blit(Background, (0, 0))
    # Draw or print stuff after this

    if CurrentGPU == GPU1Sprite or CurrentGPU == BigGPU1Sprite:
        CurrentGpuUpgradePrice = GPUUPGRADE1PRICE
        window.blit(GPU2ExampleSprite, (30, 250))
        GPUPriceText = SmallerFont.render(f"${CurrentGpuUpgradePrice}", True, (0, 0, 0))
        window.blit(GPUPriceText, (80, 430))

    if CurrentGPU == GPU2Sprite or CurrentGPU == BigGPU2Sprite:
        window.blit(GPU3ExampleSprite, (50, 250))
        CurrentGpuUpgradePrice = GPUUPGRADE2PRICE
        CurrentUpgradedGPU = GPU3Sprite
        CurrentMoneyMultiplier = GPU2ClickMultiplier
        GPUPriceText = SmallerFont.render(f"${CurrentGpuUpgradePrice}", True, (0, 0, 0))
        window.blit(GPUPriceText, (70, 430))

    if CurrentGPU == GPU3Sprite or CurrentGPU == BigGPU3Sprite:
        window.blit(GPU4ExampleSprite, (50, 250))
        CurrentGpuUpgradePrice = GPUUPGRADE3PRICE
        CurrentMoneyMultiplier = GPU3ClickMultiplier
        CurrentUpgradedGPU = GPU4Sprite
        GPUPriceText = SmallerFont.render(f"${CurrentGpuUpgradePrice}", True, (0, 0, 0))
        window.blit(GPUPriceText, (60, 430))

    if CurrentWorker == "None":
        CurrentWorkerUpgradePrice = WORKER1PRICE
        window.blit(FirstWorker, (300, 230))
        UpgradedWorker = FirstWorker
        WorkerPriceText = SmallerFont.render(f"${CurrentWorkerUpgradePrice}", True, (0, 0, 0))
        window.blit(WorkerPriceText, (300, 430))
    if CurrentWorker == FirstWorker:
        CurrentWorkerUpgradePrice = WORKER2PRICE
        window.blit(SecondWorker, (300, 230))
        UpgradedWorker = SecondWorker
        CURRENTINCOME = 5 * CurrentMoneyMultiplier
        WorkerPriceText = SmallerFont.render(f"${CurrentWorkerUpgradePrice}", True, (0, 0, 0))
        window.blit(WorkerPriceText, (300, 430))
    if CurrentWorker == SecondWorker:
        CurrentWorkerUpgradePrice = WORKER3PRICE
        window.blit(ThirdWorker, (300, 230))
        UpgradedWorker = ThirdWorker
        CURRENTINCOME = 30 * CurrentMoneyMultiplier
        WorkerPriceText = SmallerFont.render(f"${CurrentWorkerUpgradePrice}", True, (0, 0, 0))
        window.blit(WorkerPriceText, (300, 430))
    if CurrentWorker == ThirdWorker:
        CurrentWorkerUpgradePrice = WORKER4PRICE
        window.blit(FourthWorker, (300, 230))
        UpgradedWorker = FourthWorker
        CURRENTINCOME = 150 * CurrentMoneyMultiplier
        WorkerPriceText = SmallerFont.render(f"${CurrentWorkerUpgradePrice}", True, (0, 0, 0))
        window.blit(WorkerPriceText, (300, 430))
    if CurrentWorker == FourthWorker:        
        WorkerBuyButtonRect = WorkerBuyButton.get_rect(topleft=(-100, 900))
        CURRENTINCOME = 1000 * CurrentMoneyMultiplier
        WORKERMAXED = True
        # End of workers section
    if CurrentGPU == GPU4Sprite or CurrentGPU == BigGPU4Sprite:
        CurrentMoneyMultiplier = GPU4ClickMultiplier
        GPUMAXED = True
          
    GpuBuyButtonRect = GpuBuyButton.get_rect(topleft=(50, 450))
    WorkerBuyButtonRect = WorkerBuyButton.get_rect(topleft=(300, 450))
    DebtBuyButtonRect = WorkerBuyButton.get_rect(topleft=(560, 450))
    
    NewsText = EvenSmallerFont.render(f"{CurrentMessage}", True, (0, 0, 0))
    NewsX += NewsVelocityX

    window.blit(NewsText, (NewsX, 10))

    if NewsX > 2000:
        NewsX = -700
    
    if CURRENTMONEY >= 500:
        CurrentMessage = "Your Center is getting some attention"

    if CURRENTMONEY >= 2000:
        CurrentMessage = "People are paying hundreds just for your GPU's"

    if CURRENTMONEY >= 10000:
        CurrentMessage = "Your GPU's are desired by the best cloud services!"

    if CURRENTMONEY >= 20000:
        CurrentMessage = "OpenAI and Anthropic are fighting for your GPU services!"

    if CURRENTMONEY >= 50000:
        CurrentMessage = "Microsoft says: The AI uprising is upon us.."

    if GPUMAXED == True:
        GpuBuyButtonRect = GpuBuyButton.get_rect(topleft=(-100, 900))

    if WORKERMAXED == True:
        WorkerBuyButtonRect = WorkerBuyButton.get_rect(topleft=(-100, 900))
    Money = str(CurrentDisplayedMoney)
    Income = str(CurrentDisplayedIncome)

    window.blit(GpuBuyButton, GpuBuyButtonRect)
    window.blit(WorkerBuyButton, WorkerBuyButtonRect)

    if GameFinished == False:
        DebtPriceText = SmallerFont.render(f"${DebtCost}", True, (0, 0, 0))
        window.blit(DebtPriceText, (560, 430))
        window.blit(debtimage, (550, 230))
        window.blit(DebtBuyButton, DebtBuyButtonRect)

    if GameFinished == True:
        WinText = RegularFont.render("You saved the AI Bubble!", True, (0, 0, 0))
        QuoteText = SmallerFont.render("Humanity is cooked..", True, (0, 0, 0))
        window.blit(WinText, (0, 300 + IncomeFloat))
        window.blit(QuoteText, (100, 410 + IncomeFloat))

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

    clock.tick(60)
    pygame.display.flip()