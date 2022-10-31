class Cerc:

    # definim constructor - raza si culoare.
    def __init__(self,raza,culoare):
        #atribute
        self.raza_cerc = raza
        self.culoare_cerc = culoare


    #metode
    def descriere_cerc(self):
        print(f' Cercul este {self.culoare_cerc} si are raza {self.raza_cerc}.')

    def arie_cerc(self):
        rezultat_arie = 3.14 * (self.raza_cerc ** 2)
        print(f' Avand in vedere raza introdusa, {self.raza_cerc}, aria cercului este {rezultat_arie}.')

    def diametru_cerc(self):
        rezultat_diametru = self.raza_cerc * 2
        print(f' Conform razei, {self.raza_cerc}, diametrul cercului este {rezultat_diametru}.')

    def circumferinta_cerc(self):
        rezultat_circumferinta = 3.14 * (self.raza_cerc * 2)
        print(f' Conform razei, {self.raza_cerc}, circumferinta cercului este {round(rezultat_circumferinta,2)}.')