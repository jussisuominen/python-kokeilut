import os

# Pythonissa kommentit alkavat risuaitamerkillä (#).

# Konsolisovellus, joka kysyy päivämäärää käyttäjältä suomalaisessa muodossa (1.8.2022).
# Päivämäärä annetaan yhdellä rivillä. Sitten päivä, kuukausi ja vuosi tallennetaan omiin muuttujiinsa.
# Lopuksi päivä, kuukausi ja vuosi tulostetaan jokainen erikseen.

# Tyhjennetään terminaali
os.system('clear');

päivämäärä = input("Anna päivämäärä: ")

# Pilkotaan merkkijono osiin (erottimena käytettään pistettä).
# Metodi split pilkkoo merkkijonon osiin, luo listan niistä ja tallentaa
# ne muuttujaan (tässä tapauksessa "päivämäärä_osat")
päivämäärä_osat = päivämäärä.split(".")

# Muuttuja "päivämäärä_osat" sisältää nyt listan, jossa ensimmäinen alkio
# on päivä, toinen kuukausi ja kolmas vuosi. Nyt meidän tarvitsee vain tallentaa nämä
# muuttujiin "päivä", "kuukausi" ja "vuosi" ja sitten tulostaa ne. Huom. listan
# ensimmäinen alkio on 0 eikä 1.
päivä = päivämäärä_osat[0]
kuukausi = päivämäärä_osat[1]
vuosi = päivämäärä_osat[2]

print(f"Päivä: {päivä}")
print(f"Kuukausi: {kuukausi}")
print(f"Vuosi: {vuosi}")