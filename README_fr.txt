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

Les sources sont enti�rement libres: vous �tes autoris�s � toutes mofications et r�utilisations du code.
Je serais simplement reconnaissant d'�tre cit� dans vos sources si vous r�utilisez une partie de mon code.

--------------------------------- CODE REVIEW et BUG REPORT -----------------------------------------------

L'application �tant en cours de d�veloppement, je vous serais reconnaissant d'envoyer un e-mail � <lois.aubree@gmail.com> pour 
signaler quelconque bug rencontr� au cours de l'utilisation.

Pour tous apports de fonctionnalit� � l'application R'n'GAME, veuillez aussi prendre contact avec moi en envoyant un e-mail � 
<lois.aubree@gmail.com>. Pour tout ajout accept� vous serez cit� dans les sources du code, dans le readme ainsi que sur le site 
de l'application. 


Ce logiciel est d�velopp� en python et utilise les biblioth�ques :
 - PyQT4 pour l'interface.
 - PyHook pour la capture d'inputs sur win32 ainsi que pyWin32.
 - pyxHook pour Linux ( inclue dans le dossier de l'application : pas besoin d'installer).
 - Matplotib pour le dessin des graphes des inputs.


INTALLATION SOUS WINDOWS 32bit ou 64bit :

-------------------------------- PYTHON ------------------------------------------------------------

La version actuelle du logiciel n�cessite l'installation de python 2.7.X :
Vous pouvez t�l�charger les binaires de python 2.7.X � cet emplacement :

http://www.python.org/getit/

ATTENTION : La version actuelle du logiciel n'est pas compatible avec python 3.X.

Pour l'installation de greffons python sous Windows, il faut t�l�charger les executables correspondants aux plug-ins
que l'on veut installer lancer l'executable.
Une d�tection du r�pertoire python o� les greffons doivent �tre installer est alors lanc�e.

Si aucun r�pertoire est trouv�, il peut y avoir deux probl�mes :
- L'executable t�l�charg� ne correspond pas � la version du syst�me : Veuillez bien v�rifier la version des executables t�l�charg�s.
- L'executable t�l�charg� ne correspond pas � la version de pyton install� : Veuillez bien v�rifier pour quelle version de python les executables ont �t� cr�es.

-------------------------------- PYHOOK -------------------------------------------------------------

L'application n�cessite l'installation du greffon pyHook pour l'enregistrement des inputs sous Windows.
Mais avant cela il faut installer pyWin32 pour que pyHook fonctionne.

PyWin32 est souvent mis � jour, vous pouvez t�l�charger consulter les diff�rents builds � cette addresse :

http://sourceforge.net/projects/pywin32/files/pywin32/

Je d�veloppe avec la version build 218 en ce moment.

Veuillez choisir dans ce dossier l'executable correspondant � votre syst�me (32 ou 64 bit) et surtout n'oubliez pas 
qu'il s'agit de la version 2.7 de python.

Dans le build 218, vous choisirez alors :
- pywin32-218.win-amd64-py2.7.exe pour un syst�me 64 bit
- pywin32-218.win32-py2.7.exe

Remarquez que ce sont les deux executables les plus t�l�charg�s.

Ensuite vous trouverez PyHook � cette adresse : 

http://sourceforge.net/projects/pyhook/files/


-------------------------------- MATPLOTLIB ---------------------------------------------------------

Vous pouvez t�l�charger matplotlib � cette adresse :

https://github.com/matplotlib/matplotlib/downloads


/********************************************************************************************************************************************************/

INSTALLATION SOUS LINUX :

 arrive bient�t ! 
