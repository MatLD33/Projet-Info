# Projet-Info
Création du meilleur projet d'info

### TO-DO list :
* Lecture du fichier d’entrée (csv ou excel), avec la librairie pandas de python (FAIT)

* Représentation graphique des données, avec la librairie matplotlib de python (FAIT)

* Définition de la maquette de l’interface graphique et de ses fonctionnalités. Si les élèves en sont capables, une application Web serait intéressante

* Réalisation de l’interface graphique basique

* Ajout des fonctionnalités avancés d’affichage

* Ajout des fonctions de traitement de donnés automatique (voir ci-dessous) avec, par exemple, la librairie numpy de python

* Mise en place d’une version autonome du logiciel (qui soit utilisable sur les ordinateurs des opérateurs)
  
* Réfléchir à fusionner les fichiers d'acquisition des données de ref et à étalonner (A FAIRE ABSOLUMENT)

* Faire l'interpolation entre les données de ref et les données à étalonner (obtenir une réalisation) (FAIT - au sein d'un fichier)

* Choisir la sonde à afficher (FAIT)

* Récupérer les dates/temps de début et de fin de chaque palier (EN COURS) + début acquisition

### Fonctions possibles :
* détection du nombre et du nom des capteurs à traiter (???)

* détection automatique des paliers de stabilité de température/pression selon un critère de stabilité défini (par exemple, erreur type) (FAIT)

* calcul de la déviation standard d’un palier pour pouvoir comparer la stabilité des différents paliers (FAIT)

* calcul de la vitesse de chauffe/refroidissement (°C/min) des rampes (faisabale quand on aura l'approximation linéaire par morceaux)

* filtre du bruit des données (Voir si c'est vraiment utile)

* interpolation linéaire/polynomiale pour obtenir une courbe de calibration (FAIT à peu près) ==> manque la linéarisation par morceaux (FAIT)

* autres…

### Problèmes rencontrés
* les plots s'ajustent bizarrement à la fenêtre de l'interface

* formats de temps trop différents entre les fichiers