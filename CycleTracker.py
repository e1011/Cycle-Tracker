from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import cv2 as cv

def CycleTracker():
    cardNames=["unknown", "arrows", "babyDragon", "balloon", "bats", "bowler", "cannonCart", "dartGoblin", "elixirGolem",
            "evoArchers", "evoGoblinGiant", "evoRecruits", "evoSkeletons", "evoZap", "goblinBarrel", "goblinCage",
            "goblinDemolisher", "goblinGang", "goblins", "hogRider", "iceGolem", "iceSpirit", "lightning", "littlePrince", 
            "megaMinion", "minions", "monk", "poison", "prince", "skeletonArmy", "spearGoblins", "tombstone", "tornado",
            "wizard", "zap", "witch", "evoValkyrie", "witch", "freeze", "miniPekka", "fireCracker", "battleRam", "skeletonKing",
            "evoMortar", "fireSpirit", "barbarianBarrel", "xbow", "tesla", "cannon", "goblinHut", "barbarianHut", 
            "goblinDrill", "furnace", "hunter", "electroDragon", "electroGiant", "pekka", "golem", "archerQueen", "executioner",
            "giantSkeleton", "darkPrince", "guards", "clone", "wallbreakers", "mirror", "elixirCollector", "void", "threeMusketeers",            
            "fireball", "goblinGiant", "evoBats", "skeletons", "bomber", "electroSpirit", "giantSnowball", "knight", "archers",
            "evoKnight", "evoFirecracker", "skeletonBarrel", "royalDelivery", "skeletonDragons", "mortar", "barbarians",
            "minionHorde", "royalRecruits", "healSpirit", "royalGiant", "rascals", "evoIceSpirit", "evoBomber", "rage",
            "goblinCurse", "rocket", "goldenKnight", "evoWallbreakers", "evoGoblinBarrel", "evoBattleRam", "evoTesla", 
            "mightyMiner", "evoWizard", "evoBarbarians", "evoRoyalGiant", "ramRider", "nightWitch", "lumberjack",
            "magicArcher", "lavaHound", "megaKnight", "sparky", "goblinMachine", "graveyard", "fisherman", "bandit",
            "royalGhost", "electroWizard", "infernoDragon", "phoenix", "motherWitch", "iceWizard", "miner", "princess", 
            "log", "graveyard", "eliteBarbarians"
        ]

    # [what card, is it placed currently]
    cardSlots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    cycle = ["unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown"]

    def processImg(img):

        # match screenshot
        for i in range(0, 8):
            bestCard=0
            bestValue=0
            for j in range(0, len(cardNames)):
                needle_img = cv.imread("./match/"+cardNames[j]+".jpg", cv.IMREAD_REDUCED_COLOR_2)
                result = cv.matchTemplate(img[i], needle_img, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

                if max_val > bestValue:
                    bestCard = j
                    bestValue = max_val

            if cardSlots[i][1] == 0 and bestValue < 0.85:
                cardSlots[i][1] = 1
            elif cardSlots[i][1] == 1 and bestValue >= 0.85:
                cardSlots[i][0] = bestCard
                cardSlots[i][1] = 0

                if bestCard != 0:
                    cycle.append(cardNames[bestCard])
                    for j in range(0, 4):
                        if cycle[j] == cardNames[bestCard]:
                            cycle.pop(j)
                            break
                    else:
                        cycle.pop(0)
                print(cycle)
                print(cardNames[bestCard] + " placed with confidence: " + str(bestValue))

    def getCycle():
        return cycle
    
    return {"processImg": processImg, "getCycle": getCycle}


    #loop_time = time()


