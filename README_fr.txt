/**************************************************************************************************/
/                                                                                                  / 
/                                         R'N'GAME                                                 /
/                                                                                                  /
/**************************************************************************************************/

Version 1.0b.

Développé par Loïs Aubrée <lois.aubree@gmail.com> (Etudiant ingénieur en informatique à l'UTBM (Université de
Technologie de Belfort-Montbéliard). 

Le développement et l'avancement des recherches sont réalisés sous la responsabilité 
de Mathieu Triclot <mathieu.triclot@gmail.com> (Professeur en philosophie à l'Université de Technologie de Belfort-Montbéliard, 
Auteur de la Philosophie des jeux vidéo). 

Les sources sont entièrement libres: vous êtes autorisés à toutes mofications et réutilisations du code.
Je serais simplement reconnaissant d'être cité dans vos sources si vous réutilisez une partie de mon code.

--------------------------------- CODE REVIEW et BUG REPORT -----------------------------------------------

L'application étant en cours de développement, je vous serais reconnaissant d'envoyer un e-mail à <lois.aubree@gmail.com> pour 
signaler quelconque bug rencontré au cours de l'utilisation.

Pour tous apports de fonctionnalité à l'application R'n'GAME, veuillez aussi prendre contact avec moi en envoyant un e-mail à 
<lois.aubree@gmail.com>. Pour tout ajout accepté vous serez cité dans les sources du code, dans le readme ainsi que sur le site 
de l'application. 


Ce logiciel est développé en python et utilise les bibliothèques :
 - PyQT4 pour l'interface.
 - PyHook pour la capture d'inputs sur win32 ainsi que pyWin32.
 - pyxHook pour Linux ( inclue dans le dossier de l'application : pas besoin d'installer).
 - Matplotib pour le dessin des graphes des inputs.


INTALLATION SOUS WINDOWS 32bit ou 64bit :

-------------------------------- PYTHON ------------------------------------------------------------

La version actuelle du logiciel nécessite l'installation de python 2.7.X :
Vous pouvez télécharger les binaires de python 2.7.X à cet emplacement :

http://www.python.org/getit/

ATTENTION : La version actuelle du logiciel n'est pas compatible avec python 3.X.

Pour l'installation de greffons python sous Windows, il faut télécharger les executables correspondants aux plug-ins
que l'on veut installer lancer l'executable.
Une détection du répertoire python où les greffons doivent être installer est alors lancée.

Si aucun répertoire est trouvé, il peut y avoir deux problèmes :
- L'executable téléchargé ne correspond pas à la version du système : Veuillez bien vérifier la version des executables téléchargés.
- L'executable téléchargé ne correspond pas à la version de pyton installé : Veuillez bien vérifier pour quelle version de python les executables ont été crées.

-------------------------------- PYHOOK -------------------------------------------------------------

L'application nécessite l'installation du greffon pyHook pour l'enregistrement des inputs sous Windows.
Mais avant cela il faut installer pyWin32 pour que pyHook fonctionne.

PyWin32 est souvent mis à jour, vous pouvez télécharger consulter les différents builds à cette addresse :

http://sourceforge.net/projects/pywin32/files/pywin32/

Je développe avec la version build 218 en ce moment.

Veuillez choisir dans ce dossier l'executable correspondant à votre système (32 ou 64 bit) et surtout n'oubliez pas 
qu'il s'agit de la version 2.7 de python.

Dans le build 218, vous choisirez alors :
- pywin32-218.win-amd64-py2.7.exe pour un système 64 bit
- pywin32-218.win32-py2.7.exe

Remarquez que ce sont les deux executables les plus téléchargés.

Ensuite vous trouverez PyHook à cette adresse : 

http://sourceforge.net/projects/pyhook/files/


-------------------------------- MATPLOTLIB ---------------------------------------------------------

Vous pouvez télécharger matplotlib à cette adresse :

https://github.com/matplotlib/matplotlib/downloads


/********************************************************************************************************************************************************/

INSTALLATION SOUS LINUX :

 arrive bientôt ! 
