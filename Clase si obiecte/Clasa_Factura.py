from datetime import date
from tabulate import tabulate

class Factura:

    #constructor - numar, nume_produs, cantitate, pret_buc
    def __init__(self, numar, nume_produs, cantitatea, pret_buc):
        #atribute
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitatea
        self.pret_buc = pret_buc
        self.seria = 'ABC'

    # metode

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, schimb_pret):
        self.pret_buc = schimb_pret

    def schimba_nume_produs(self, schimb_nume):
        self.numar +=  1
        self.nume_produs = schimb_nume

    def genereaza_factura(self):

        azi = date.today()
        total = self.cantitate * self.pret_buc

        cap_tabel = ['Produs                   ','Cantitate','Pret bucata(Lei)','Total(Lei)']
        valori_tabel = [(self.nume_produs,self.cantitate,self.pret_buc,total)]

        print('----------------------------------')
        print(f'| Factura {self.seria}, numarul {self.numar}         |')
        print(f'| Data facturii este: {azi} |')
        print('---------------------------------------------------------------------------------')
        print(tabulate(valori_tabel,headers=cap_tabel,tablefmt="github"))
        print('---------------------------------------------------------------------------------')

