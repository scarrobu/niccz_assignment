class Gepard:
    MAX_ZIVOTU = 9

    def __init__(self):
        self.pocet_zivotu = self.MAX_ZIVOTU

    def __str__(self):
        return f"Geapard má {self.pocet_zivotu} životov."
    
    def over_zivot(self):
        return self.pocet_zivotu <= 0

    def uber_zivot(self):
        if self.over_zivot():
            print("Nemuzes zabit uz mrtve zvire!")
        else:
            self.pocet_zivotu -= 1

    def obnov_zivot(self):
        if self.over_zivot():
            print("Nemuzes liečiť mrtve zvire!")
        else:
            self.pocet_zivotu += 1

    def snez(self, jidlo):
        if self.over_zivot():
            print("Je zbytecne krmit mrtve zvire!")
            return
        if jidlo == "ryba" and self.pocet_zivotu < self.MAX_ZIVOTU:
            self.obnov_zivot()
        else:
            print("Gepard se krmi.")

    def behej(self):
        if self.over_zivot():
            print("Mrtve zvire uz nikam nedobehne!")
        else:
            print("Gepard bezi.")

    def napapej_se(self, jidlo):
        if self.over_zivot():
            print("Tomuto zvieratku už žiadne jedlo mu už nepomôže.")
        elif jidlo == "ryba" and not self.over_zivot():
            for _ in range(self.MAX_ZIVOTU - self.pocet_zivotu):
                self.obnov_zivot()
                print(f"Aktuálne ich má {self.pocet_zivotu} životov.")
            print("Tento gepard už viac životov nezíska, netreba ho kŕmiť ďalšími rybami")
        else:
            print("gepard to spapal, ale nezískal žiadny benefit")

g = Gepard()
print(g)