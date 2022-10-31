class Masina:
    # definim constructor - iban, titular_cont si sold
    def __init__(self, model, viteza_maxima):
        #atribute
        self.model_masina = model
        self.viteza_maxima_masina = viteza_maxima
        self.marca_masina = 'Porsche'
        self.culoare_masina = 'Gri' #culoare default din frabrica
        self.viteza_actuala_masina = 0
        self.culori_disponibila_masina = {'Rosu', 'Verde', 'Albastru','Turcoaz', 'Galben'}
        self.inmatriculata = False

    #metode

    def descriere_masina(self):
        print(f'Va prezentam masina:')
        print('')
        print(f'- {self.marca_masina}, modelul {self.model_masina}.')
        print(f'- Culoarea din fabrica este {self.culoare_masina}.')
        print(f'- Poate atinge viteza maxima de {self.viteza_maxima_masina} Km/h.')


        if self.inmatriculata == False:
            print('- Momentan masina nu este inmatriculata.')
        else:
            print('- Masina este inmatriculata.')

    def inmatriculare_masina(self):
        self.inmatriculata = True
        print(f' {self.inmatriculata}')

    def vopsire_masina(self,vopsea):

        if vopsea in self.culori_disponibila_masina:
            self.culoare_masina = vopsea
            print(f' Masina va fi vanduta pe culoarea {self.culoare_masina}.')
        else:
            print(' Culoarea aleasa nu este diponibila.')

    def accelerare_masina(self,viteza):

        if viteza < 0:
            print(' Viteza invalida, reintrodu valoarea.')
        elif viteza > 310:
            print(f' Viteza de {viteza} Km/h este prea mare, masina nu poate atinge viteza introdusa, viteza maxima este de {self.viteza_maxima_masina} Km/h.')
        else:
            print(f' Viteza este {viteza} Km/h.')

    def franare(self):

        print(f' Masina s-a oprit, are viteza {self.viteza_actuala_masina} Km/h.')