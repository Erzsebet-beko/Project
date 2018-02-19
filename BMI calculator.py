
név = input (" Add meg a neved: ")
print (" Üdvözöllek " + név )
testmagasság = input (" Add meg a magasságod tizedes pontosággal pl:1.70: ")
kg = input (" Most pedig add meg hány kg-m vagy : ")
BMI = 0
BMI = float(kg) /float(testmagasság) ** 2
print (" A Te BMI értéked: " + str(BMI) )
print("Add meg mit ettél ma, és hány kalóriát! pl: kifli = 300")
étel = input (" Név:   ")
kalória = input(" Kalória: ")
étel2 = input (" Név:   ")
kalória2 = input(" Kalória: ")
étel3 = input (" Név:   ")
kalória3 = input(" Kalória: ")

kalória_össz = int(kalória)+ int(kalória2) + int(kalória3)
print("Össz kalória : " + str(kalória_össz))

print("Remek most egy gyors egészsségügyi vizsgálatnak vetünk alá :)")
print(" Egy...kettő...három...és most akkor jön a varázslat")
if kalória_össz > 2000:
    print("Hát szó szó...")
else:
    print("Egészséges vagy")









