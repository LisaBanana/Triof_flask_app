README

# PROJET TRIOF
La société Triof met à disposition des entreprises une machine permettant de trier certains déchets plastiques afin de générer des filaments plastiques pour les imprimantes 3D. 
Jusqu'a présent, l'utilisateur devait lui même labelliser le déchet déposé dans la machine. 
Ceci entrainit un problème de la labéllisation  car parfois l'utilisateur se trompait. 
A cause d'erreurs de classification, les filaments crées étaient de moins bonne qualité.

Pour remédier a ce problème, il est d'utiliser un modèle de vision par ordinateur ou computer vision afin d'automatiser la classification des déchets. 
L'utilisateur n'a qu'a confirmer la prédiction faite par le modèle. 
Si la classification effectuée n'est pas correcte, l'utilisateur peut la modifier et confirmer son changement.

# Fonctionnement
Dans un premier temps la machine nous propose de déposer un déchet. Par la suite celle ci nous demande de confirmer le dépot du déchet. L'algorithme de vision par ordinateur effectue sa prédiction concernant la nature du déchet. L'utilisateur valide ou corrige cette classification. Un message de remerciement apparait.

Afin d'utiliser l'application : Installer les dépendances nécessaires. 
/!\ : problèmes de compatibilité scipy.misc lib imread pour des versions supérieures à scipy==1.1.0

pip install -r requirement.txt

Usage
Pour utiliser l'aplication :

python triof_app.py

/!\ Si vous souahitez modifier des éléments de l'app, pensez bien a set l'environnement FLASK_ENV = development afin de pouvoir bénéficier du debug_mode

# Arborescence du dossier 
voir l'image arborescence_triof

En détail :
- camera : (photos des déchets)
- src : -pycache -utils.py : contient les fonctions utilisées pour monitorer la machine, prendre des photos des déchets et effectuer les prédictions.
- static :
	- index.html
	- css, webfronts, images, assets relative files + Licence.txt & Readme.txt
- templates :
	- confirm_type.html (page de confirmation)
	- confirmation.html
	- insert.html
	- home.html
	- type.html
- triof_app.py : fichier de lancement de la webapp Flask
- requirements.txt : fichier contenant la liste des packages utilisés
- index.html : structure html du site