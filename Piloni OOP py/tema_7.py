from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    @abstractmethod
    def descriere(self):
        pass

class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura = latura

    def descriere(self):
        print('Cel mai probabil am colturi.')

    def get_latura(self):
        return self.__latura

    def set_latura(self,latura_noua):
        self.__latura = latura_noua

    def aria(self):
        arie_patrat = self.__latura ** 2
        print(f'Aria patratului este {arie_patrat}.')


class Cerc(FormaGeometrica):

    def __init__(self,raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self,raza_noua):
        self.__raza = raza_noua

    def aria(self):
        arie_cerc = (self.__raza ** 2) * self.pi
        print(f'Aria cercului cu raza {self.__raza} este {arie_cerc}.')

    def descriere(self):
        print('Eu nu am colturi.')

if __name__ == "__main__":


    #patrat
    print('')
    print('* Metode clasa patrat.')
    print('')

    arie_patrat = Patrat(4)
    descr_p = Patrat(4)
    descr_p.descriere()
    print(f'Latura patratului este {arie_patrat.get_latura()}')
    arie_patrat.aria()

    arie_patrat.set_latura(5)
    print(f'Schimbam latura patratului in {arie_patrat.get_latura()}')
    arie_patrat.aria()


    print('')

    # cerc
    print('* Metode clasa cerc.')
    print('')

    arie_cerc = Cerc(10)
    descr_c = Cerc(1)
    descr_c.descriere()
    print(f'Raza cercului este {arie_patrat.get_latura()}.')
    arie_cerc.aria()

    arie_cerc.set_raza(100)
    print(f'Schimbam raza cercului in {arie_cerc.get_raza()}.')
    arie_cerc.aria()

