class TodoList:
    # definim constructor
    def __init__(self):
        #atribute
        self.to_do_list = {}

    #metode
    def adaugare_task(self, nume, descriere):
        self.to_do_list[nume] = descriere
        print(f' - {self.to_do_list}' )



    def finalizeaza_task(self,nume):

        if nume in self.to_do_list:
            self.to_do_list.pop(nume)
            print(f' Task-ul {nume} s-a finalizat, se sterge din lista.')
            print( self.to_do_list)
        else:
            print(' Task-ul nu se afla in lista, inseamna ca este finalizat sau nu a fost adaugat. ')

    def to_do_list_chei(self):

        print(f' Key dictionar {self.to_do_list.keys()}')


    def afiseaza_detalii_suplimentare(self,nume_task):

        raspuns_pozitiv = 'Da'
        raspuns_negativ = 'Nu'
        nr_incercari = 0

        if nume_task in self.to_do_list:
            print(f' Task-ul {nume_task} se trateaza cu prioritate.')
        else:
            while nr_incercari < 5:
                nr_incercari +=1
                intrebare = input(' Taskul nu este in lista, doriti sa il adaugam?')
                if nr_incercari == 5:
                    print(' Ati raspuns gresit de 5 ori, incercati din nou peste 10 minute')
                elif intrebare == raspuns_pozitiv:
                    detalii_task = input(' Va rugam sa ne oferiti detalii despre task:')
                    self.to_do_list[nume_task] = detalii_task
                    print(f' Task: {self.to_do_list}.')
                    break
                elif intrebare == raspuns_negativ:
                    print(' Va multumim, la revedere!')
                    break
                else:
                    print(' Raspuns invalid, raspundeti cu Da sau Nu.')
