import pytest # Pour les fixtures

from testsunitaires import get

# Je déclare une fixture, qui peut (ce n'est pas obligatoire), retourner
# quelque chose
@pytest.fixture()
def simple_comme_bonjour():
    return ('pomme', 'banane')
    
# On passe de pytest.fixture() a pytest.yield_fixture()
@pytest.yield_fixture()
def simple_comme_bonjour_2():
    # tout ce qui est setup() va au dessus du yield. Ca peut etre vide.
    print('Avant !')
 
    # Ce qu'on yield sera le contenu du parametre. Ca peut etre None.
    yield ('pomme', 'banane')
 
    # Ce qu'il y a apres le yield est l'equivalent du tear down et peut être
    # vide aussi
    print('Apres !')
 
# Pour chaque test où je déclare le nom de la fixture en paramètre, pytest
# va appeler la fonction juste avant le test et passer son résultat
# (fut-il None), en argument de ce test
def test_get(simple_comme_bonjour):
    element = get(simple_comme_bonjour, 0)
    assert element == 'pomme'
 
# il est possible de ne pas utiliser de fixture.
def test_element_manquant(simple_comme_bonjour_2):
    element = get(simple_comme_bonjour_2, 1000, 'Je laisse la main')
    assert element == 'Je laisse la main'
