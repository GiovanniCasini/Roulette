import random

rouletteNumber = None
playerNumber = None

nullSession = 0
topBalance = 0

betsArray = []
winsArray = []
maxBalanceArray = []

nRuns = 100

for i in range(nRuns):
    startBalance = 200
    balance = startBalance
    bet = 0.2
    bets = 0
    wins = 0
    maxBalance = 0
    timeMax = 0
    betMax = 0
    while balance > 0:
        print(balance)
        bets += 1
        balance -= bet
        playerNumber = random.randint(0, 36)
        playerNumber = 0
        rouletteNumber = random.randint(0, 36)
        if playerNumber == rouletteNumber:
            print(playerNumber, rouletteNumber)
            wins += 1
            balance += bet * 36
            if betMax < bet:
                betMax = bet
            bet = 1
            if balance > maxBalance:
                maxBalance = balance
                timeMax = bets
        else:
            bet += 0.1

    if maxBalance == 0:
        nullSession += 1
    betsArray.append(bets)
    winsArray.append(wins)
    maxBalanceArray.append(maxBalance)
    if maxBalance > topBalance:
        topBalance = maxBalance

sumBets = 0
sumWins = 0
sumMaxBalance = 0
for i in range(nRuns):
    sumBets += betsArray[i]
    sumWins += winsArray[i]
    sumMaxBalance += maxBalanceArray[i]

print("Bets:", sumBets/nRuns, " Wins:", sumWins/nRuns, " MaxBalance:", sumMaxBalance/nRuns, "NullSessions:", nullSession, "TopBalance:", topBalance)
"""

startBalance = 1000
balance = startBalance
bet = 1
bets = 0
wins = 0
maxBalance = 0
timeMax = 0
betMax = 0
while balance > 0:
    print(balance)
    bets += 1
    balance -= bet
    # playerNumber = random.randint(0, 36)
    playerNumber = 0
    rouletteNumber = random.randint(0, 36)
    if playerNumber == rouletteNumber:
        print(playerNumber, rouletteNumber)
        wins += 1
        balance += bet * 36
        if betMax < bet:
            betMax = bet
        bet = 1
        if balance > maxBalance:
            maxBalance = balance
            timeMax = bets
    else:
        bet += 0.5

print("Bets:", bets, " Wins:", wins, " MaxBalance:", maxBalance, "TimeMax:", timeMax, "BetMax:", betMax)
"""
