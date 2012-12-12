/**************************************************************************************************/
/                                                                                                  / 
/                                         R'N'GAME                                                 /
/                                                                                                  /
/**************************************************************************************************/

Version 1.0b.

D�velopp� par Lo�s Aubr�e <lois.aubree@gmail.com> (Etudiant ing�nieur en informatique � l'UTBM (Universit� de
Technologie de Belfort-Montb�liard). 

Le d�veloppement et l'avancement des recherches sont r�alis�s sous la responsabilit� 
de Mathieu Triclot <mathieu.triclot@gmail.com> (Professeur en philosophie � l'Universit� de Technologie de Belfort-Montb�liard, 
Auteur de la Philosophie des jeux vid�o). 

Les sources sont enti�rement libres: vous �tes autoris�s � toutes modifications et r�utilisations du code.
Je serais simplement reconnaissant d'�tre cit� dans vos sources si vous r�utilisez une partie de mon code.

--------------------------------- CODE REVIEW et BUG REPORT -----------------------------------------------

L'application �tant en cours de d�veloppement, je vous serais reconnaissant d'envoyer un e-mail � <lois.aubree@gmail.com> pour 
signaler quelconque bug rencontr� au cours de l'utilisation.

Pour tout apport de fonctionnalit� � l'application R'n'GAME, veuillez aussi prendre contact avec moi en envoyant un e-mail � 
<lois.aubree@gmail.com>. Pour tout ajout accept� vous serez cit� dans les sources du code, dans le readme ainsi que sur le site 
de l'application. 


Ce logiciel est d�velopp� en python et utilise les biblioth�ques :
 - PyQt4 pour l'interface.
 - PyHook pour la capture d'inputs sur win32 ainsi que pyWin32.
 - pyxHook pour Linux ( inclue dans le dossier de l'application : pas besoin d'installer).
 - Matplotib pour le dessin des graphes des inputs.


******* INTALLATION SOUS WINDOWS 32bit ou 64bit :

-------------------------------- PYTHON ------------------------------------------------------------

La version actuelle du logiciel n�cessite l'installation de python 2.7.X :
Vous pouvez t�l�charger les binaires de python 2.7.X � cet emplacement :

http://www.python.org/getit/

ATTENTION : La version actuelle du logiciel n'est pas compatible avec python 3.X.

Pour l'installation de greffons python sous Windows, il faut t�l�charger les executables correspondants aux plug-ins
que l'on veut installer et lancer l'executable.
Une d�tection du r�pertoire python o� les greffons doivent �tre installer est alors lanc�e.

Si aucun r�pertoire n'a �t� trouv�, il peut y avoir deux probl�mes :
- L'executable t�l�charg� ne correspond pas � la version du syst�me : Veuillez bien v�rifier la version des executables t�l�charg�s.
- L'executable t�l�charg� ne correspond pas � la version de python install� : Veuillez bien v�rifier pour quelle version de python l'executable a �t� cr�e.

-------------------------------- PYHOOK -------------------------------------------------------------

L'application n�cessite l'installation du greffon pyHook pour l'enregistrement des inputs sous Windows.
Mais avant cela il faut installer pyWin32 pour que pyHook fonctionne.

PyWin32 est souvent mis � jour, vous pouvez t�l�charger consulter les diff�rents builds � cette addresse :

http://sourceforge.net/projects/pywin32/files/pywin32/

Je d�veloppe avec la version build 218 en ce moment.

Veuillez choisir dans ce dossier l'executable correspondant � votre syst�me (32 ou 64 bit) et surtout n'oubliez pas 
qu'il s'agit de la version 2.7 de python.

Dans le build 218, vous choisirez alors :
- pywin32-218.win-amd64-py2.7.exe pour un windows 64 bit
- pywin32-218.win32-py2.7.exe pour un windows 32 bit

Ensuite vous trouverez PyHook � cette adresse : 

- http://sourceforge.net/projects/pyhook/files/    Il n'y a pas de version 64bit !?! 

Pas de panique, vous la trouverez ,ici:

http://www.lfd.uci.edu/~gohlke/pythonlibs/  

-------------------------------- MATPLOTLIB ---------------------------------------------------------

Vous pouvez t�l�charger matplotlib � cette adresse :

https://github.com/matplotlib/matplotlib/downloads

-------------------------------- PyQt4 --------------------------------------------------------------

Vous pouvez t�l�charger matplotlib � cette adresse :

http://www.riverbankcomputing.co.uk/software/pyqt/download (voir binary packages)

/********************************************************************************************************************************************************/

INSTALLATION SOUS LINUX :

 arrive bient�t ! 

 
 ********** LANCEMENT DE L'APPLICATION :
 
 
  1) Option pour d�veloppeur :
  	-	Installer eclipse et les plug-ins PyDev et Egit
  	- 	Renseigner � Pydev le r�pertoire Python 2.7.X avec les biblot�ques pr�c�dement install�es
  	-	Importer dans eclispe le projet git depuis le repo github : https://github.com/Dufeu/MR52_R-n-Game
 	-	lancer le programme en tant qu'application Pydev depuis le fichier mrQWindow.py
 	
  2) Option pour utilisateur : 
  	-	R�cuperer le projet sur gitHub � l'aide d'un outil git : https://github.com/Dufeu/MR52_R-n-Game
  	-	Lancer en ligne de commande l'application (dans la console windows 'win->cmd') :
  			
  			>Chemin_du_repertoire_python\python.exe chemin_du_repertoire_R'n'Game\src\keylog\mrQWindow.py
  			
  Si vous rencontrez des probl�mes pour le lancement de l'application, n'h�sitez pas � m'envoyer un e-mail.
  