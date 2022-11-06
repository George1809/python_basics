import unittest

from Teme_curs.Tema_curs8.functii_si_clase import text, comparare, par_impar




class ExampleUnittests(unittest.TestCase):


    def test_in(self):
        un_text = 'Asa si asa'
        self.assertIn(text('a'),un_text)
        self.assertIn(text('A'), un_text)

    def test_mai_mare(self):
        self.assertGreater(comparare(4), 2)
        self.assertGreater(comparare(8), (2+1))

    def test_par(self):
        self.assertEqual(par_impar(10),True)
        self.assertNotEqual(par_impar(2), False)


if __name__ == "__main__":
    unittest.main()


