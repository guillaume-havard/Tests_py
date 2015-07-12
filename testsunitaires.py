#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

##### Tets Unitaires #####

# Quest-ce que c'est ?
# Tester une unité du code.
# une unité ? : bout de code le plus petit possible (pour bien tout tester)
# Mais pas trop pour ne pas faire que ça.
# Tester ? : donnée les entrées et sorties attendues du code et voir si le
# code les calculs bien.

# Principal but : vérifier que l'on ne régresse pas quand on modifie
# le code.
# particulièrement intéressant quand il y aplusieurs participant qui ne
# peuvent que difficilement voir l'impact de leurs actions sur le reste
# du programme.


# Exemple avec fonction qui retourne un élément d'une liste ou un 
# choix par défaut si l'index n'existe pas :
def get(lst, index, default=None):
    """
        Retourne l'élément de `lst` situé à `index`.
 
        Si aucun élément ne se trouve à `index`,
        retourne la valeur par défaut.
    """
    try:
        return lst[index]
    except IndexError:
        return default

simple_comme_bonjour = ('pomme', 'banane')
print(get(simple_comme_bonjour, 0, "je laisse la main"))
print(get(simple_comme_bonjour, 1000, "je laisse la main"))

## unittest ##
# Module de tests intégré dans python

# Les tests avec unittest vont se faire dans une classe spécifique
# ici dans test_testsunitaire.py.
# S'il y aune erreur dans le code de test Un 'E' apparaitra
# Si un test n'est pas passé il y aura un 'F' (fail) dans le compte rendu.
# Et des information utile pour retrouvé le problème sont données
# Assert utiles (beaucoup plus en vrai, regarder la doc) :
# * assertAlmostEqual
# Va vérifier qu’un nombre est presque égal à un autre, à un arrondi près.
# * assertDictContainsSubset
# Va vérifier que toutes les paires clé/valeur d’un dico sont contenues dans un
#  autre.
# * assertRaises
# Va vérifier que la fonction va lever une exception.
# * assertRegex
# Va vérifier que la chaîne est validée par la regex donnée.

# Pour certaines parties de tests qui vont se répéter il est possible
# d'utiliser les fonction setUp et tearDown qui vont s'exécuter
# avant et après chaque fonction

# Quand vous allez avoir plein de tests, vous n’allez pas tout mettre dans une
# classe, mais faire plein de fichiers avec des tests par sujet. Parfois
# vous ne lancerez qu’un fichier de test. Parfois vous voudrez tout lancer
# d’un coup.

# Pour ce faire, assurez vous que vos modules de tests sont importables depuis 
# le dossier où vous êtes. Tout doit être dans le PYTHON_PATH et les 
# dossiers doivent contenir des fichiers __init__.py.

# Ensuit, il suffit de lancer la commande :

# python -m unittest discover

# Python trouvera tous les fichiers de tests pour vous automatiquement, 
# pourvu qu’ils soient nommés test_quelquechose.py.

### pytest ###
# plus simple que unittest
# (ne pas mélanger les deux)
# Pas besoin d'importer de module ni de créer des classe.
# Les fonctions de tests comme les fichiers contenant ces fonctions
# doivent être précedé de "test_".
# les comparaison se font avec 'assert foo == bar'
# dirfférent type d'assert :
# * assertDictEqual => assert a == b
# * assertFalse => assert not a
# * assertGreater => assert a > b
# * assertIn => assert a in b
# * assertIs => assert a is b

# Il existe des fixtures pour avoir l'équivalent de setUp et tearDown
# Si nous voulons que les fixture soient lancées de base : 
# '@pytest.fixture(autouse=True)'

# Pour lancer le test 'py.test', -s pour voir les affichages de sortie.

# Pour voir les option de pytest 'py.test --help'
# Quelques exemples :
# * -k EXPRESSION : lance uniquement les tests qui contiennent cette chaîne.
# Pratique quand on a beaucoup de tests longs et qu’on travaille sur un en
# particulier.
# * -x : s’arrêter à la première erreur. Pour le debug, ça évite de se taper tous 
# les # tests après ce qu’on veut explorer.
# * --doctest-modules: lance les doctests de tous les fichiers *.py trouvés 
# récursivement dans le dossier.
# * --ignore=PATH: ignore un chemin. Je l’utilise souvent pour éviter que pytest 
# n’aille lancer les tests des libs de mon virtualenv.

### doctest ###
# Faire des doctests n’est pas bien compliqué car c’est du copier coller. 
# On fait une session shell avec ce qu’on veut tester, et on copie-colle le 
# tout dans la docstring. Fastoche.

# on copie juste la session de shell tel quel
def ajouter(a, b):
    """
        >>> ajouter(1, 2)
        3
    """
    return a + b
 
# et on demande à Python de parser les doctests. Directement dans votre fichier
# de code. Si, si. Pas de fichier de tests à part.

import doctest
doctest.testmod()

# On lance ensuite directement notre fichier de code :

# python mon_module.py
# Et ça n’affiche absolument rien. C’est parce qu’il n’y a pas d’erreur. On peut
# avoir le topo en demandant un peu de verbosité avec -v

# Tous les test vont se baser sur les chevrons ">>>" et le résultat attendu qui
# les suit

# L'avantage et que ces test peuvent facilement s'intégrer à la doc
""" Additionne deux elements.
 
    Exemple :

        >>> # on peut mettre des commentaires ici
        >>> ajouter(1, 2) # ou là
        3
        >>> ajouter(2., 2) # fonctionne sur tous les types de nombre
        4.0

    La fonction fonctionne en duck typing, et accepte donc tout objet
    qui possède la méthode magique __add__ :

        >>> ajouter('a', 'b')
        'ab'
        >>> ajouter([1], [2])
        [1, 2]
"""
# ou
""" Implémente l'équivalent de dict.get() pour les indexables.
 
    Example :

        >>> simple_comme_bonjour = ('pomme', 'banane')
        >>> get(simple_comme_bonjour, 0)
        'pomme'
        >>> get(simple_comme_bonjour, 1000, 'Je laisse la main')
        'Je laisse la main'
"""
# Par contre un peu plus limité que les autre module de tests
# Penser à bien tester les exemples en console avant.

# S'utilisent en complément de tests (pytest par exemple).
# tant que la fonctionnalité est simple les doctestssont utile sinon utiliser
# d'autre modules plus développés.

print()
### Les Mocks ###
# Les outils que nous avons vu jusqu'à présent atteindront leur limite s'il
# Faut faire des tests réels (connection, internet, BdD, appel à un autre
# programme ...).
# Pour cela il y a les mock : 
"""Un objet mock, c’est un objet basé sur le null object pattern qui sert à 
faire semblant. Quand on l’instancie avec n’importe quoi, ça marche, quand on 
appelle n’importe quelle méthode, ça marche et ça renvoie un mock"""
import unittest.mock

# Un objet mock peut être appeler comme une classe ou une fonction
# et retouren toujours un mock. Il est possible d'appeler n'importe quel
# méthode et retournera toujors un mock
from unittest.mock import MagicMock # ou from mock import MagicMock
mock = MagicMock()
print(mock)
print(mock())
print(mock(1, True, [Exception, {}]))
print(mock.foo())
print(mock.nimporte().nawak().je().te().dis())
print(mock + mock - 10000)

# Il est possible de faire en sorte qu'ils aient un comportement spécifique.
mock.you = MagicMock(side_effect=ValueError('mofo !')) # un callable marche aussi
#mock.you() # Provoque une ValueError
mock.mock = MagicMock(return_value="moooooooooock")
print(mock.mock())

# Il est possible de combiner de vrai objets avec des mock

class maClasse:
    def func1(self):
        print("coucou")
    def func2(self):
        print("COCORICO")
        
oo = maClasse()
oo.func1 = MagicMock()

print(oo.func1("POKEMON !!").split() + 33)
print(oo.func2())

# Il est possible d'avoir un historique de ce qui a été utilisé avec les mocks.
print(oo.func1.mock_calls)

# Il est possible de vérifier si un appel a bien été fait :
oo.func1.assert_called_with("POKEMON !!")
# oo.func1.assert_called_with("Mario !") Provoquera une erreur.

# Patch
# permet de modifier le comportement de ce qui existe pour les tests.
from unittest.mock import patch
"""
with patch.object(builtins, "open", mock_open(read_data="wololo") as mock:
#with patch('__main__.open', mock_open(read_data='wololo'), create=True) as mock:
    with open('zefile') as h:
        result = h.read()

mock.assert_called_once_with('zefile')
assert result == 'wololo'
""" ### Ne fonctionne pas

# Il est possible de patcher un bout de module :
@patch('os.listdir')
def ah(mock):
    import os
    print(os.listdir('.'))
    # l'objet mock initial est aussi passé en param automatiquement
    print(mock)

ah()

# Cela permet de recérer un environement de test complet.
# exemple :
# Exemple prit d’une base de code IRL, avec une fonction pytest qui teste un 
# objet response représentant une réponse HTTP. Si on appelle write() sur cet 
# objet sous-jacent elle doit faire des appels à deux méthodes privées et une 
# méthode d’un objet Twisted.

# Problème, ces méthodes :
# * Supposent qu’une event loop est lancée.
# * Ecrivent sur le réseau.
# * Sont potentiellement appelées de manière asynchrone, en dehors de notre
# contrôle.
# * Ont des side effects donc on veut être certains qu’elles sont appelées, et 
# avec les bons paramètres.
# Du coup, on les remplace par des objets mocks, et yala :

def test_write(response):
    assert response.write != response._req.write
    response._disable_rendering = MagicMock(name='_disable_rendering')
    response._set_twisted_headers = MagicMock(name='_set_twisted_headers')
    response.write(b'test')
    response._set_twisted_headers.assert_called_once_with()
    response._disable_rendering.assert_called_once_with()
    assert response.write == response._req.write
    response._req.write.assert_called_once_with(b'test')



print("fin")

