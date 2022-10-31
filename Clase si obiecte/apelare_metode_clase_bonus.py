from Teme_curs.Tema_curs6.Clasa_Factura import Factura
from Teme_curs.Tema_curs6.Clasa_Masina import Masina
from Teme_curs.Tema_curs6.Clasa_TodoList import TodoList

print('')
print(' -----------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Factura <- |')
print(' -----------------------------------------------')



valoare_1_factura = Factura(1, 'Tableta Samsung', 2, 750)

print('')
print('Afisam detaliile facturii 1:')
print('')

valoare_1_factura.genereaza_factura()

print('')
print('Afisam detaliile facturii cu valori modificate:')
print('')

print('Factura 2:')
print('')
valoare_1_factura.schimba_nume_produs('Laptop Lenovo i7')
valoare_1_factura.schimba_cantitatea(3)
valoare_1_factura.schimba_pretul(4500)


valoare_1_factura.genereaza_factura()

print('')
print('Factura 3:')
print('')
valoare_1_factura.schimba_nume_produs('Samsung Galaxy S22')
valoare_1_factura.schimba_cantitatea(2)
valoare_1_factura.schimba_pretul(5500)

valoare_1_factura.genereaza_factura()

print('')
print(' -----------------------------------------------')
print('| ● Metode aplicate pentru clasa -> Masina <-  |')
print(' -----------------------------------------------')

valoare_masina = Masina('911 Carrera 4', 310)

print('')
print('Afisam descrierea masinii:')
print('')

valoare_masina.descriere_masina()

print('')
print('Afisam "True" pentru inmatricularea masinii:')
print('')

valoare_masina.inmatriculare_masina()

print('')
print('Schimbam culoarea masinii:')
print('')

valoare_masina.vopsire_masina('Turcoaz')

print('')
print('Afisam viteza masinii:')
print('')

valoare_masina.accelerare_masina(311)

print('')
print('Franam masina, revenim la viteza 0:')
print('')

valoare_masina.franare()


print('')
print(' -------------------------------------------------')
print('| ● Metode aplicate pentru clasa -> TodoList <-  |')
print(' -------------------------------------------------')


to_do_list = TodoList()


print('')
print('Adaugam si afisam task-urile:')
print('')

to_do_list.adaugare_task('Client 1','De sunat pentru confirmare release.')
to_do_list.adaugare_task('Client 2','Eroare accesare aplicatie, de investigat.')
to_do_list.adaugare_task('Client 3','De trimis mail pentru pasi de instalare aplicatie')
to_do_list.adaugare_task('Client 4','Conectare remote pentru verificare problema client mail.')
to_do_list.adaugare_task('Client 5','Debugging eroare generata consola browser.')

print('')
print('Stergem task:')
print('')

to_do_list.finalizeaza_task('Client 1')

print('')
print('Afisam chei task-uri definite.')
print('')

to_do_list.to_do_list_chei()


print('')
print('Verifica task.')
print('')

to_do_list.afiseaza_detalii_suplimentare('Client 1')