#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

# Les exceptions interompent le programme et signalent que quelque chose 
# d'anormal est en train de se passer : division par 0, accès à un 
# élément d'une liste ...

### Lever une exception ###
# Il est possible de lever (lancer, activer) une action
#raise NomDeLException("EREUUUR !!")

def votre_super_fonction(param):
    if param not in (1, 2, 3):
        raise ValueError("'param' can only be either 1, 2 or 3")
    print("param :", param)
        

#votre_super_fonction(1) # Ok
#votre_super_fonction(5) # Lèvera une exception

### Attraper une exception ###
# Au lieu de laisse une exception stopper le programme il est possible de les
# Attraper et de traiter le cas spécial qui vient d'être levé.

try:
    # lignes qui peuvent
    # lever une exception
    votre_super_fonction(5)
except ValueError:
   # faire un truc si l'exception se déclenche
   print("erreur attrapée")
   
print()
   
# Si le type de l'erreur n'est pas attraper le programme s'arrètera.
# Il est possible d'avoir plusieurs blocs 'except' qui se suivent.
# Les Exceptions sont hiérarchisées il est donc possible, en attrapant
# une classe, d'attraper ces sous classes.
# Toutes les erreures algorithmique héritent de 'Exception'. Attention
# Ne pas utiliser une classe trop haute dans la hiérarchhie car cela peut
# masquer un bogue, mieux vaut arrêter les différentes erreures nominativement.
# Il est aussi possible de tout attraper en ne méttant pas de nom d'exception.

# Il est possible de créer ses propres exceptions en héritant des exceptions
# existantes
class SuperError(Exception):
    pass
 
class PBPrecisError(SuperError):
    pass
    
# Le choix du parent pour hériter des excpetion est important, il vaut mieux
# qu'il y ait un lien logique avec l'erreur
"""Les exceptions sont une forme d’expression :

* Celui qui lève l’exception dit explicitement ce qui peut merder : 
quand on lit son code, on comprend les cas d’erreurs.
* Celui qui l’attrape dit explicitement ce qu’il veut gérer : 
quand on lit son code, on comprend l’objectif.
* Python dit explicitement ce qui a foiré. Quand on lit la stack trace,
on comprend ce qui a merdé.

Vous communiquez en utilisant des exceptions entre développeurs et
 utilisateurs du code."""
 
# À try et except peuevnt s'ajouter deux autres mots clefs.
## else
# le bloc sera exécuté si aucune exception n'est lancé
## finaly
# Le bloc sera exécuté de toutes façon même si le programme s'arrète.
# (sauf si gros porblème qui stope totalement l'éxecution du process)

tab = [1, 2, 3]
i = 100

try:
    tab[100 // i]
except (IndexError, ZeroDivisionError):
    pass
except KeyError:
    print("Liste modifiee")
else:
    print("Bon en fait tout va bien")
finally:
    print("Coucou, finally")

print()  
### Quand utiliser les try/catch ? ###
# La première raison est de les utiliser quand une erreure peut venir de
# exterieur du programme, accès fichier, internet ...
# Dans l'except pour être placé le log de l'erreur (fichier, module login ...)

# Permet de donner un comportement par défaut
# par exemple, si accés à quelque chose qui n'existe pas, renvoyer valeur
# par defaut
# deplus permet de traiter plusieurs cas d'un coup et de traiter rapidement
# le problème, quel que soit le problème.
# exemple :
try:
    fichier = open('/tmp/fichier', 'w')
except (IOError, OSError):
    # gérer l'erreur
    pass
"""Si je devais faire ça avec des if, il faudrait :

* Vérifier que le fichier existe.
* Vérifier que le fichier est un fichier et non un dossier.
* Vérifier que j’ai les permissions d’écrire sur le fichier.
* Vérifier que j’ai les permissions de traverser les dossiers parents.
* Vérifier que personne n’a ouvert le fichier en écriture avant."""

#finaly est utile pour faire du nettoyage :  
try:
    fichier = open('/tmp/fichier', 'w')
except (IOError, OSError):
    # gérer l'erreur
    pass
# on essaye toujours de fermer notre fichier
finally:
    try:
        fichier.close() 
    # le fichier n'a jamais été ouvert et
    # la variable n'existe pas
    except NameError:
        pass
        
### with ###
# permet de fermer automitiquement (si ouvert) un fichier.
# Même exemple qu'au dessus :
try:
    with open('/tmp/fichier', 'w') as fichier:
        pass # faire un truc avec le fichier
except (IOError, OSError):
    # gérer l'erreur
    pass
    
### Bubbling ###
# Fait d'avoir les erreurs qui remontent jusqu'à la racine.
# Le mieux et d'avoir exactement le comportement que l'on veut pour que 
# l'erreur soit traitée de façon optimale.

### Manipulation des erreurs ###
# Il est possible de récupérer des informations des erreurs avec le mot
# clef 'as':
try:
    f = open("nawak")
except IOError as e:
    print(e)
    print("args: ", e.args)
    print("errno: ", e.errno)
    print("filename: ", e.filename)
    print("strerror: ", e.strerror)
    
# Il est aussi possible de les relancer, pour qu'elles soit traitées plus haut
try:
    f = open("nawak")
except IOError as e:
    #raise e # renvoie l'erreur
    #raise PBPrecisError("N'importe quoi !") # renvoie un aurte type d'erreur
    pass
print()   

### Catch global ###

# Il est possible d’attraper n’importe quelle exception non gérée juste avant
# qu’elle fasse crasher le programme, sans avoir à mettre tout son code dans
# un gros try/except.

# Il faut définir une fonction qui accepte 3 arguments que sont la classe de 
# l’exception, l’instance de l’exception et l’objet traceback :

def attrapez_les_tous(type, value, traceback):
    print("Pokemon !")
    print(type)
    print(value)
    print(traceback)

#Ensuite il faut l’attacher au module sys avec le bon nom :

import sys
sys.excepthook = attrapez_les_tous

#Et hop :

a = 1 / 0


# Alors, c’est certain que si vous faites ça, vous avez intérêt à savoir ce
# que vous branlez car vous pouver tuer le debuggage. Ou alors créer un super
# moyen de logger toute erreur sur un process séparé qui vous le présente dans
# une belle interface Web. Au choix.
    
### Notes ###
# Les exception peuvent être utilisés dans d'autre cas que pour signaler une
# erreur.
# Pour les itération quan un itérateur à finit d'itérer

### ###

