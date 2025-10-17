
**🐎 Jeu de Course de Chevaux (Terminal)**
  
  Ce projet est un jeu de course de chevaux écrit en Python.
  Il se joue entièrement dans le terminal.
***
**📦 Fonctionnalités**
 - Génération de 12 à 20 chevaux
 - Chaque cheval avance en fonction d’un dé (1 à 6)
 - Gestion de la vitesse, distance, et disqualification
 - Affichage d’un podium final (Tiercé, Quarté, Quinté)
 - Représentation de la course avec une barre de progression
 - Interaction en temps simulé (tours de 10 secondes)
 ***
**🚀 Lancer le jeu**
 - Avoir Python 3 installé sur votre machine
 - Ouvrir un terminal
 - Lancer le fichier Python avec cette commande: ***python main.py***
***
**🎮 Instructions**
 - Le jeu vous demandera deux choses au début :
 - La quantité de chevaux (entre 12 et 20)
 - Le type de sortie :
       - tiercé → les 3 premiers
       - quarté → les 4 premiers
       - quinté → les 5 premiers
 - Ensuite, à chaque tour, appuyez sur Entrée pour continuer la course.
***
**🎲 Règles du jeu**
 - Chaque cheval commence avec vitesse de *0*
 - À chaque tour :
 - Un dé est lancé pour chaque cheval
 - Le résultat modifie la vitesse
 - La vitesse détermine combien de mètres le cheval avance
 - Si un cheval atteint 2500 mètres, il est arrivé
 - Si un cheval à haute vitesse tire un 6, il est disqualifié (DQ)
 - La course continue jusqu’à ce que tous les chevaux soient arrivés ou disqualifiés
***
**📺 Affichage**
 ***Pendant la course, le jeu montre :***
 - Le numéro de chaque cheval
 - Sa vitesse
 - Sa distance actuelle
 - Son statut :
	- playing → en course
	- finished → arrivé
	- DQ → disqualifié
	- Une barre de progression illustre la distance parcourue :
	- Vert → cheval arrivé
	- Rouge → cheval disqualifié
	- Gris → cheval en course
***
**📁 Fichier**

main.py : contient tout le code
***
**🔧 Dépendances**
*Aucune. Le script utilise uniquement les bibliothèques standards suivantes :*
 - random
 - copy (deepcopy)
***
**👨‍💻 Auteur**

Développé par Rafael DA SILVA.
Projet pour apprendre Python en créant un jeu simple et interactif.
Projet fait comme exercice pour FMS dans le cadre de la formation Python.
***
**📄 Licence**

Ce jeu peut être utilisé, modifié et partagé librement.
