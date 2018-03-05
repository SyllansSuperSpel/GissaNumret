"""
Gissa numret
"""

# Nån voodoo grej, some eric skrev
import random
numret = random.randint(1, 100)

# Mitt spel
while True:
    gissning = int(input('Gissa ett nummer: '))

    if gissning == numret:
        print("Yay!")
        break

    elif gissning > numret:
        print("Lägre")

    else: 
        print("Högre")


print("Nu var det slutspelat!")
