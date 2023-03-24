# Pythonissa kommentit alkavat risuaitamerkillä (#).

# Tämän koodin tarkoituksena on esitellä Pythonin perusjuttuja ja tulee koodissa esille vähän 
# edistyneempiäkin asioita. Koodissa luodaan konsolisovellus, joka kysyy 
# päivämäärää käyttäjältä suomalaisessa muodossa (esim. 23.3.2023). Sovellus tarkistaa sitten, onko päivämäärä
# oikeassa muodossa ja jos on, tulostaa sovellus päivämäärän päivän, kuukauden ja vuoden.
# Jos päivämäärä on väärässä muodossa, ilmoitetaan siitä käyttäjälle ja sovelluksen suoritus keskeytetään.

# Koodissa tulee esille Pythonin perusasioita, joita ovat:
# - kommentit, joita luet juuri nyt ;)
# - muuttujan määrittely ja arvon asettaminen muuttujaan
# - syötteen pyytäminen käyttäjältä (input-funktio)
# - merkkijonon pilkkominen osiin (split-funktio)
# - if-lause
# - sovelluksen suorittamisen keskeyttäminen exit-funktion avulla
# - for... in-silmukka
# - isnumeric-funktio, jolla voidaan tarkistaa, sisältääkö merkkijonomuuttuja luvun.
# - lista
# - muotoiltu tulostus ja muuttujan arvon sijoittaminen merkkijonoon f-merkkijonon avulla

# Koodissa tulee esille myös virheentarkistusta, mikä on erityisen 
# tärkeä ominaisuus missä tahansa sovelluksessa.

# Pyydä käyttäjältä syöte input-funktion avulla ja tallenna se "päivämäärä"-muuttujaan.
# input-funktiolle annetaan parametriksi kehote, joka käyttäjälle näytetään, kun häneltä
# pyydetään syötettä.

# Pythonissa muuttujaa ei tarvitse esitellä erikseen ennen kuin sitä voidaan käyttää toisin
# kuin esimerkiksi C:ssä. Myöskään muuttujan tyyppiä ei tarvitse erikseen määritellä,
# vaan se määräytyy sen mukaan, mikä arvo siihen asetetaan. Tässä tapauksessa muuttujaan
# "päivämäärä" asetetaan merkkijonoarvo, koska käyttäjän antama syöte on merkkijono.
päivämäärä = input("Anna päivämäärä: ")

# Pilkotaan merkkijono osiin (erottimena käytetään pistettä).
# Metodi split pilkkoo merkkijonon osiin, luo listan niistä ja tallentaa
# ne muuttujaan (tässä tapauksessa "päivämäärä_osat"). Ensimmäinen listan
# alkio on päivä, toinen kuukausi ja kolmas vuosi.
päivämäärän_osat = päivämäärä.split(".")

# Virheentarkistusta. Tarkistetaan, onko käyttäjä syöttänyt päivämäärän
# oikeassa muodossa.

# Tarkista, että päivämäärässä on kolme osaa. 
# len-funktio kertoo listan sisältämien alkioiden määrän.
if len(päivämäärän_osat) < 3:
    # Päivämäärässä on vähemmän kuin kolme osaa. Ilmoita käyttäjälle, että
    # hän antoi päivämäärän väärässä muodossa ja lopeta sovellus.
    print('Virhe! Annoit päivämäärän väärässä muodossa.')
    exit(1) # Poistu sovelluksesta. Argumentti 1 tarkoittaa, että tapahtui virhe.

# Tarkista, onko jokin päivämäärän osista jokin muu kuin luku
# Käy läpi jokainen päivämäärän osa.
for päivämäärän_osa in päivämäärän_osat:
    # isnumeric-funktio tarkistaa, onko merkkijonon arvo luku.
    if not päivämäärän_osa.isnumeric():
        # Päivämäärän osa ei ole luku. Ilmoita käyttäjälle, että
        # hän antoi päivämäärän väärässä muodossa ja lopeta sovellus.
        print('Virhe! Annoit päivämäärän väärässä muodossa.')
        exit(1)

# Jippii! Päästiin ensimmäisestä virheentarkistuksesta läpi. Nyt tiedämme, että käyttäjän syöttämässä
# päivämäärässä on kolme osaa eli päivä, kuukausi ja vuosi. Tiedämme myös sen, että käyttäjä on
# käyttänyt pistettä erottimena. Meidän täytyy vielä tehdä muutama lisätarkistus, mutta tallennetaan
# sitä ennen päivämäärän päivä, kuukausi ja vuosi saman nimisiin muuttujiin. Tämä helpottaa
# ja selkeyttää lisätarkistusten tekemistä sekä myös päivämäärän, kuukauden ja vuoden tulostamista.

# Muuttuja "päivämäärän_osat" sisältää listan, jossa ensimmäinen alkio on päivä, toinen kuukausi
# ja kolmas vuosi.
päivä = päivämäärän_osat[0]
kuukausi = päivämäärän_osat[1]
vuosi = päivämäärän_osat[2]

# Ja sitten taas lisää virheentarkistusta.

# Tarkista, onko päivä 0 tai suurempi kuin 31. Jos on, tulosta virhe ja lopeta sovellus.
# Muuttujan "päivä" tyyppi on merkkijono, koska sille annettiin merkkijonoarvo.
# Muuttujan tyyppi pitää muuttaa kokonaisluvuksi ennen kuin sitä voidaan verrata
# kokonaislukuarvoon. Muuntaminen kokonaisluvuksi tapahtuu int-funktion avulla.
if int(päivä) == 0 or int(päivä) > 31:
    print('Virhe! Syöttämässäsi päivämäärässä on virheellinen päivä.')
    exit(1)

# Tarkista, onko kuukausi 0 tai suurempi kuin 12.
# Muuttujan "kuukausi" tyyppi on merkkijono, koska sille annettiin merkkijonoarvo.
# Muuttujan tyyppi pitää muuttaa kokonaisluvuksi ennen kuin sitä voidaan verrata
# kokonaislukuarvoon. Muuntaminen kokonaisluvuksi tapahtuu int-funktion avulla.
if int(kuukausi) == 0 or int(kuukausi) > 12:
    print('Virhe! Syöttämässäsi päivämäärässä on virheellinen kuukausi.')
    exit(1)

# Kaikki tarkistukset menivät läpi eli vihdoinkin päästään tulostamaan päivämäärän
# päivä, kuukausi ja vuosi.
print(f"Päivä: {päivä}")
print(f"Kuukausi: {kuukausi}")
print(f"Vuosi: {vuosi}")