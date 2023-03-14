
def functie(tabel,stare_actuala,litera_actuala):
    for posibilitate in tabel:
        if stare_actuala==posibilitate[0] and litera_actuala==posibilitate[1]:
            return posibilitate[2]

print("AUTOMAT FINIT DETERMINIST- PARAMETRII")

with open("ex2.txt","r") as f:
    stari=[str(x) for x in f.readline().strip().split()]
    alfabet=[str(x) for x in f.readline().strip().split()]
    tabel=[]
    for stare in stari:
        for litera in alfabet:
            stare_echivalenta = str(f.readline().strip())
            tabel.append((stare,litera,stare_echivalenta))
    stare_initiala=str(f.readline().strip())
    stare_finala=[str(x) for x in f.readline().strip().split()]
print("CUVANT")
cuvant=str(input("Cuvant= "))


stare_actuala=stare_initiala
traseu=[stare_actuala]
for index in range(len(cuvant)):
    stare_actuala=functie(tabel,stare_actuala,cuvant[index])
    traseu.append(stare_actuala)


if stare_actuala not in stare_finala:
    print("neacceptabil")
else:
    print("acceptabil")
    for stare in traseu:
        print(f"{stare} -> ",end="")
    print("IESIRE",end="")