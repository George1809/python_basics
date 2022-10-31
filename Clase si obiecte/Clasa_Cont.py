class Cont:
    # definim constructor - iban, titular_cont si sold
    def __init__(self, titular_cont, iban, sold):
        #atribute
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = sold

    #metode
    def sold_actual_disppnibil(self):
        print(f' Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} Lei.')

    def credidare_cont(self, suma):
        print(f' Salut {self.titular_cont}!')
        self.sold += suma
        print(f' Ai alimentat contul cu suma de {suma} Lei.')
        print(f' Acum in cont ai disponibila suma de {self.sold} Lei.')

    def debitare_cont(self, suma):
        print(f' Salut {self.titular_cont}!')
        if suma <= self.sold:
            self.sold -= suma
            print(f' Ai cheltuit suma de {suma} Lei')
            print(f' Mai ai disponibila in cont suma de {self.sold} Lei.')
        else:
            print(' Fonduri insuficiente pentru suma pe care vrei sa o cheltui.')
            print(f' In cont ai disponibila suma de {self.sold} Lei dar vrei sa cheltui suma de {suma} Lei.')