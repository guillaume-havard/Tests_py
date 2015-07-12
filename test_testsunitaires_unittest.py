import unittest
 
# Le code à tester doit être importable. On
# verra dans une autre partie comment organiser
# son projet pour cela.
from testsunitaires import get
 
# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class TestFonctionGet(unittest.TestCase):
 
    # Cette méthode sera appelée avant chaque test.
    def setUp(self):
        self.simple_comme_bonjour = ('pomme', 'banane')
 
    # Cette méthode sera appelée après chaque test même en as d'erreur.
    def tearDown(self):
        pass
 
    # Chaque méthode dont le nom commence par 'test_'
    # est un test.
    def test_get_element(self):
 
        element = get(simple_comme_bonjour, 0)
 
        # Le test le plus simple est un test d'égalité. On se
        # sert de la méthode assertEqual pour dire que l'on
        # s'attend à ce que les deux éléments soient égaux. Sinon
        # le test échoue.
        self.assertEqual(element, 'pomme')
     
    # Il faut choisir un nom explicite pour chaque méthode de test
    # car ça aide à débugger.
    def test_element_manquant(self):
        element = get(simple_comme_bonjour, 1000, 'Je laisse la main')
        self.assertEqual(element, 'Je laisse la main')
 
# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()
