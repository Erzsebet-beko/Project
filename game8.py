from random import randint
import easygui_gui as gui

life = 3        #life, ertek: 3, tipus: int
round = 0
arany = 0
targy_lista = ["kard", "pajzs", "pancel", "kotel", "ko"]
targy_dict = {  targy_lista[0]: 5,
                targy_lista[1]: 3,
                targy_lista[2]: 10,
                targy_lista[3]: 2,
                targy_lista[4]: 2
            }

filename_="nev.txt"

#fuggveny definialas
def aranyat_talal(arany, arany_min, arany_max):
    talalt_arany = randint(arany_min, arany_max)
    arany += talalt_arany
    print("Talalkoztal egy torpevel es adott neked: " \
          + str(talalt_arany) + " aranyat")
    print("Osszesen " + str(arany) + " aranyad van")
    return arany

def the_end(round, arany, talalttargyak, targy_dict, _file_name_):
    print("Sajnos vége a játéknak...")
    print(str(round) + " kort eltel tul.")
    targy_arany = targy_to_szam(targy_dict, talalttargyak)
    arany += targy_arany
    print("Osszesen " + str(arany) + " aranyad van")
    print("Talalt targyak: " + str(talalttargyak))
    print("Játsszunk legközelebb is!")

def ut_valasztas(max_ut):
    # Ellenorzott ut bekeres ciklussal
    valasztott_ut_szammal = 255
    while valasztott_ut_szammal > max_ut or valasztott_ut_szammal < 1:
        print("Merre indulsz?")
        valasztott_ut = input("Valassz utat 1 es " + str(max_ut) + " kozott!")
        try:
            valasztott_ut_szammal = int(valasztott_ut)
        except ValueError:
            valasztott_ut_szammal = 255
        if valasztott_ut_szammal > max_ut or valasztott_ut_szammal < 1:
            print("\t[!!!!]Ervenytelen valasztas!")
    return valasztott_ut_szammal


def nevvalasztas(filename):
    nev = input("Add meg a neved!")
    with open(filename, 'w') as f:
        f.write(nev)
    return nev

def targy_talalas(lista):
    index = randint(0, len(lista)-1)
    targy = lista[index]
    return targy

def targy_to_szam(_dict, _lista):
    sum = 0
    for value in _lista:
        #targy_ertek = _dict[value]
        #sum = targy_ertek + sum
        sum += _dict[value]
    print("Osszesen aranyad van targyakbol: " + str(sum))
    return sum

def game(_arany, _round, _life, _targy_lista, _targy_dict):
    talalt_targyak = []

    jatekos_neve = gui.nevvalasztas(_file_name)
    msg = """Kerüld el a csapdát()!
    Útelágazáshoz érkeztél.Három""".format(jatekos_neve)
    gui.uzenet.msg

    _arany = aranyat_talal(_arany, 10, 50)

    while _life > 0:

        max_valaszthato_ut = 4
        valasztott_ut_szammal = ut_valasztas(max_valaszthato_ut)
        rajzolj(valasztott_ut_szammal)

        # csapda ut generalas
        csapda_ut = randint(1, max_valaszthato_ut)

        response = ""
        if valasztott_ut_szammal == csapda_ut:
            print("\tCsapda!")
            _life = _life - 1
            print(str(_life) + " eleted maradt")
            _round += 1
        else:
            print("\tBiztonságos út. Most tovább mehetsz.")
            _arany = aranyat_talal(_arany, 0, 20)
            talalt_targyak.append(targy_talalas(_targy_lista))
            _round += 1
    the_end(_round, _arany, talalt_targyak, _targy_dict)

if __name__ == "__main__":
    #call main program function
    game(arany, round, life, targy_lista, targy_dict)
    input("Exit? Press any key and/or enter.")