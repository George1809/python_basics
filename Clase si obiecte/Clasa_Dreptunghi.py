class Dreptunghi:

    # definim constructor - lungime, latime si culoare.
    def __init__(self, lungime, latime, culoare):
        # atribute
        self.lungime_dreptunghi = lungime
        self.latime_dreptunghi = latime
        self.culoare_dreptunghi = culoare

    # metode
    def descriere_dreptunghi(self):
        print(f' Dreptunghiul este {self.culoare_dreptunghi}, are lungimea de {self.lungime_dreptunghi} si latimea de {self.latime_dreptunghi}.')

    def arie_dreptunghi(self):
        aria_dreptunghiului = self.lungime_dreptunghi * self.latime_dreptunghi
        print(f' Aria dreptunghiului cu lungimea de {self.lungime_dreptunghi} si latimea de {self.latime_dreptunghi} este de {aria_dreptunghiului}.')

    def perimetru_dreptunghi(self):
        perimetrul_dreptunghiului = 2 * (self.lungime_dreptunghi + self.latime_dreptunghi)
        print(f' Perimetrul dreptunghiului cu lungimea de {self.lungime_dreptunghi} si latimea de {self.latime_dreptunghi} este de {perimetrul_dreptunghiului}.')

    def culoare_noua_dreptunghi(self,culoare_noua):
        self.culoare_dreptunghi = culoare_noua