from Teme_curs.Tema_curs6.Clasa_Cerc import Cerc
from Teme_curs.Tema_curs6.Clasa_Dreptunghi import Dreptunghi
from Teme_curs.Tema_curs6.Clasa_Angajat import Angajat
from Teme_curs.Tema_curs6.Clasa_Cont import Cont


print('')
print(' -------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Cerc <- |')
print(' -------------------------------------------')

valori_1_cerc = Cerc(10,'Galben')
valori_2_cerc = Cerc(20,'Albastru')
valori_3_cerc = Cerc(15,'Verde')

print('')
print('Afisam descrierea cercului, raza si culoarea, cu 3 valori diferite:')
print('')

valori_1_cerc.descriere_cerc()
valori_2_cerc.descriere_cerc()
valori_3_cerc.descriere_cerc()

print('')
print('Afisam aria cercului pe baza celor 3 valori introduse pentru raza:')
print('')

valori_1_cerc.arie_cerc()
valori_2_cerc.arie_cerc()
valori_3_cerc.arie_cerc()

print('')
print('Afisam diametrul cercului pe baza celor 3 valori introduse pentru raza:')
print('')

valori_1_cerc.diametru_cerc()
valori_2_cerc.diametru_cerc()
valori_3_cerc.diametru_cerc()

print('')
print('Afisam circumferinta cercului pe baza celor 3 valori introduse pentru raza:')
print('')

valori_1_cerc.circumferinta_cerc()
valori_2_cerc.circumferinta_cerc()
valori_3_cerc.circumferinta_cerc()

print('')
print(' -------------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Dreptunghi <- |')
print(' -------------------------------------------------')

valori_1_dreptunghi = Dreptunghi(15, 10,'Roz')
valori_2_dreptunghi = Dreptunghi(100,22, 'Portocaliu')
valori_3_dreptunghi = Dreptunghi(8, 4, 'Rosu')

print('')
print('Afisam descrierea dreptunghiului, lungime, latime si culoarea, cu 3 valori diferite:')
print('')

valori_1_dreptunghi.descriere_dreptunghi()
valori_2_dreptunghi.descriere_dreptunghi()
valori_3_dreptunghi.descriere_dreptunghi()

print('')
print('Afisam aria dreptunghiului pe baza celor 3 valori introduse pentru lungime si latime:')
print('')

valori_1_dreptunghi.arie_dreptunghi()
valori_2_dreptunghi.arie_dreptunghi()
valori_3_dreptunghi.arie_dreptunghi()

print('')
print('Afisam perimetrul dreptunghiului pe baza celor 3 valori introduse pentru lungime si latime:')
print('')

valori_1_dreptunghi.perimetru_dreptunghi()
valori_2_dreptunghi.perimetru_dreptunghi()
valori_3_dreptunghi.perimetru_dreptunghi()

print('')
print('Afisam culori actualizate pentru dreptunghi:')
print('')

valori_1_dreptunghi.culoare_noua_dreptunghi('Violet')
valori_2_dreptunghi.culoare_noua_dreptunghi('Antracit')
valori_3_dreptunghi.culoare_noua_dreptunghi('Aramiu')

valori_1_dreptunghi.descriere_dreptunghi()
valori_2_dreptunghi.descriere_dreptunghi()
valori_2_dreptunghi.descriere_dreptunghi()

print('')
print(' ----------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Angajat <- |')
print(' ----------------------------------------------')

print('')
print('Afisam descrierea angajatilor:')
print('')

valori_angajat_1 = Angajat('Jan', 'Ion', 3000)
valori_angajat_2 = Angajat('John', 'Michael', 4000)
valori_angajat_3 = Angajat('Robert', 'Tester', 5000)

valori_angajat_1.functie_vechime('Endava', 'Programator', 5)
valori_angajat_2.functie_vechime('Microsoft', 'Suport Tehnic', 2)
valori_angajat_3.functie_vechime('Dell', 'Vanzari', 8)

valori_angajat_1.descriere_angajat()

print('------------------------------------------------')

valori_angajat_2.descriere_angajat()

print('------------------------------------------------')

valori_angajat_3.descriere_angajat()

print('')
print('Afisam doar numele complet al unui angajat:')
print('')

valori_angajat_1.nume_complet_angajat()
valori_angajat_2.nume_complet_angajat()
valori_angajat_3.nume_complet_angajat()

print('')
print('Afisam doar salariul lunar al unui angajat:')
print('')

valori_angajat_1.salariu_lunar_angajat()
valori_angajat_2.salariu_lunar_angajat()
valori_angajat_3.salariu_lunar_angajat()

print('')
print('Afisam salariul anual al unui angajat:')
print('')

valori_angajat_1.salariul_anual_angajat()
valori_angajat_2.salariul_anual_angajat()
valori_angajat_3.salariul_anual_angajat()

print('')
print('Afisam salariul marit pentru fiecare angajat, in functie de procentul introdus:')

procent_angajat_1 = valori_angajat_1.marire_salariu(15)
procent_angajat_2 = valori_angajat_2.marire_salariu(20)
procent_angajat_3 = valori_angajat_3.marire_salariu(30)

print(f' Procentele sunt: {procent_angajat_1}%, {procent_angajat_2}% si {procent_angajat_3}%.')
print('')
valori_angajat_1.salariu_lunar_angajat()
valori_angajat_2.salariu_lunar_angajat()
valori_angajat_3.salariu_lunar_angajat()

print('')
print(' -------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Cont <- |')
print(' -------------------------------------------')

print('')
print('Afisam titularul contului si soldul din cont:')
print('')

valori_1_cont = Cont('George Alex', 'RO10INGB1002033212', 10000)
valori_2_cont = Cont('Ioana Scarlate', 'RO40INGB1002044111', 20000)
valori_3_cont = Cont('Ion Ion', 'RO70INGB1002033223', 30000)

valori_1_cont.sold_actual_disppnibil()
valori_2_cont.sold_actual_disppnibil()
valori_3_cont.sold_actual_disppnibil()

print('')
print('Debitam un cont si afisam soldul actualizat in urma debitarii:')
print('')

valori_1_cont.debitare_cont(11000)

print('------------------------------------------------')

valori_2_cont.debitare_cont(3000)

print('------------------------------------------------')

valori_3_cont.debitare_cont(1500)


print('')
print('Creditam un cont si afisam soldul actualizat in urma creditarii:')
print('')

valori_1_cont.credidare_cont(1000)

print('------------------------------------------------')

valori_2_cont.credidare_cont(1800)

print('------------------------------------------------')

valori_3_cont.credidare_cont(10100)