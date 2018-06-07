.. _userguide:

======================
Guide de l'utilisateur
======================

À l'initialisation du logiciel, l'aperçu en temps réel devrait apparaître. Vous avez alors plusieurs fonctionnalités à votre disposition.

.. note:: 

	Le prévisionnement est un `Overlay`_, ce qui signifie qu'il est généré «par-dessus» l'écran.
	C'est pour cela qu'en déplaçant la fenêtre, il ne suit pas immédiatement la position de la fenêtre. Son ajustement est fait de manière à ce que sa position s'adapte lorsque le programme
	détecte un mouvement de la fenêtre principale (`root`) et la fonction est seulement appelée lorsque le déplacement du `root` est complété.
	On ne peut pas prendre de capture d'écran du prévisionnement puisque c'est un `Overlay`. C'est comme s'il était par-dessus la capture. Pour plus d'informations, consultez la `page`_
	du module PiCamera sur l'aperçu et l'`Overlay`.

.. _Overlay: https://en.wikipedia.org/wiki/Overlay_(programming)
.. _page: https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.start_preview


.. _quickstart:

Démarrage rapide
================

Si vous avez téléchargé le dossier au complet, vous remarquerez deux dossiers dans le répertoire principal: **Captures** et **Vidéo**. Ce sont les dossiers dans lesquels
seront enregistrées vos photos et vidéos prises avec l'application. Si vous souhaitez enregistrer vos captures dans un autre répertoire vous pouvez commencer par ouvrir le 
menu **Fichier** et choisir de nouveaux répertoires. Pour plus d'options, consultez la section :ref:`save`.

Vous pouvez maintenant prendre des photos en appuyant sur la barre espace ou sur le bouton avec l'icône d'un appareil photo dans le menu *Commandes* sous l'aperçu. 
Remarquez la barre d'état en bas à droite: elle indique si vous pouvez prendre une photo et ensuite dans quel répertoire la capture est enregistrée.

Pour prendre des vidéos, appuyez sur le bouton avec l'icône d'un caméscope. Un rond rouge vous indiquera que vous êtes en train de filmer. Pour finir l'enregistrement, 
appuyez à nouveau sur le bouton. La barre d'état vous dira dans quel répertoire la vidéo est enregistrée.

.. note::

	Le format des fichiers vidéo est .h264 par défaut et le programme filme à 24 fps. Si vous voulez lire les vidéos, 
	allez dans le répertoire dans lequel se trouve le fichier et exécutez la commande suivante 
	dans l'invite de commande::
		
		omxplayer --fps 24 file_name.h264
	
	Omxplayer est le lecteur vidéo du Raspberry Pi.


.. _zoom:

Zoomer
======

Vous pouvez zoomer dans l'image à l'aide de la glissoire **Zoom**. Après avoir choisi le zoom désiré, vous pouvez vous déplacer avec les deux autres glissoires **X** et **Y**. 
Celles-ci vous feront déplacer horizontalement et verticalement respectivement. Pour la glissoire **X**, une valeur 0 indique que vous vous trouvez complètement à gauche de 
l'image et une valeur de 100, complètement à droite. Pour la glissoire **Y**, 0 indique que vous vous trouvez complètement en haut de 
l'image et une valeur de 100, complètement en bas.    


.. note::

	Il y a une sécurité qui limite le zoom maximal dans le code. À un certain point, la caméra zoome sur seulement quelques pixels et cela fait planter l'application. 
	Si vous devez absolument zoomer plus que ce que le programme propose, vous pouvez changer la valeur 1.05 à la ligne 780 du fichier **PiCameraGUI.py** dans la fonction 
	set_previewScale par 1.00. Cela vous permettera de zoomer jusqu'aux limites de la PiCamera, mais c'est déconseillé. Vous êtes conseillez de remettre ce paramètre à 1.05 par la suite.

Pour réinitialiser le zoom de l'image comme elle était à l'ouverture du programme, appuyez sur le bouton **Réinitialiser** sous la glissoire **Y**. 
Ça fait la même chose que de remettre les
trois glissoires à 0.

.. _image:

Paramètres de l'image
=====================



.. _resolution:

Changer la résolution
=====================



.. _text:

Afficher un texte
=================



.. _save:

Modifier l'endroit de la sauvegarde
===================================


.. _other:

Autres fonctionnalités
======================


* Changer le nombre de prise de photo en séquence



* Changer le temps de la capture vidéo



* Revirements et rotation


* Tout réinitialiser



