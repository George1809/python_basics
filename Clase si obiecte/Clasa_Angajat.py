class Angajat:
    #definim constructor - nume, prenume si salariu
    def __init__(self, nume, prenume, salariu):
        # atribute
        self.nume_angajat = nume
        self.prenume_angajat = prenume
        self.salariu_angajat = salariu

    # metode
    def functie_vechime(self, companie, functie, vechime):
        self.functie_angajat = functie
        self.vechime_angajat = vechime
        self.companie_angajat = companie

    def descriere_angajat(self):
        print(f' Numele angajatului este {self.nume_angajat} {self.prenume_angajat}.')
        print(f' In acest moment are un salariu net de {self.salariu_angajat} RON.')
        print(f' Lucreaza la compania {self.companie_angajat}, pe postul {self.functie_angajat}.')
        print(f' Vechimea in companie este de {self.vechime_angajat} ani.')

    def nume_complet_angajat(self):
        print(f' Nume si prenume angajat:{self.nume_angajat} {self.prenume_angajat}')

    def salariu_lunar_angajat(self):
        nume_prenume_angajat = self.nume_angajat + ' ' + self.prenume_angajat
        print(f' Salariul lunar al angajatului {nume_prenume_angajat} este {self.salariu_angajat}.')

    def salariul_anual_angajat(self):
        nume_prenume_angajat = self.nume_angajat + ' ' + self.prenume_angajat
        salariu_anual = self.salariu_angajat * 12
        print(f' Salariul anual al angajatului {nume_prenume_angajat} este {salariu_anual}.')

    def marire_salariu(self,procent):
        self.salariu_angajat = self.salariu_angajat  + self.salariu_angajat * (procent/100)

        return procent

