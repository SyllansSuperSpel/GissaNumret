"""
Hänga gubbe
"""
import sys

# Nån voodoo grej, some eric skrev
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Hämta ett ord
page = urlopen('https://svenska.se/tre/?sok=&pz=1')
soup = BeautifulSoup(page, 'html.parser')
ordet = soup.find('a', attrs={'class': 'slump'}).text.strip()
gissningar = set()


def skriv_ut():
    # Skriv ut hur det går
    print('Ordet:' + ''.join(map(lambda x: x if x in gissningar else '_',ordet)))
    print('Du har gissat:{}'.format(gissningar))
    print('')

print('Ordet har {} bokstäver'.format(len(ordet)))

# Mitt spel
while True:
    # Ta in gissning
    gissning = input('Gissa en bokstav: ')
    # lägg till i gissningar
    gissningar.add(gissning)
    # Skriv ut hur det går
    skriv_ut()


print("Nu var det slutspelat!")
