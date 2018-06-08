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


.. image:: _static/gui.png
	:align: center


.. _quickstart:

Démarrage rapide
================

Si vous avez téléchargé le dossier au complet, vous remarquerez deux dossiers dans le répertoire principal: **Captures** et **Vidéo**. Ce sont les dossiers dans lesquels
seront enregistrées vos photos et vidéos prises avec l'application. Si vous souhaitez enregistrer vos captures dans un autre répertoire vous pouvez commencer par ouvrir le 
menu **Fichier** et choisir un nouveau répertoire. Pour plus d'options, consultez la section :ref:`save`.

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

Vous pouvez ajuster les paramètres de l'image avec les options sous le menu Exposition. L'``ISO`` change la luminosité de l'image ainsi que la quantité de `grain`/bruit.
Un faible ISO donnera une image claire en terme de bruit, mais sombre en terme de lumière. Un ISO élevé fera augmenter la luminosité de l'image, mais augmentera aussi la quantité de grain.
Le ``shutter speed`` change le temps d'exposition. Un shutter speed faible permet de capter plus de lumière et d'avoir une image plus éclairée. 
Un shutter speed plus élevé permet de prendre une photo plus figée dans le temps au détriment de capter moins de lumière. 
Lorsqu'il y a beaucoup de mouvement, on voudrait avoir un shutter speed élevé pour éviter un flou.
Les ``modes d'exposition`` sont présentés dans la `rubrique`_ de la documentation de la picamera. Ce sont des modes préprogrammés.
Veuillez consulter ce `lien`_ pour de plus amples explications.

.. _lien: https://photographylife.com/iso-shutter-speed-and-aperture-for-beginners

.. _rubrique: https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.start_preview


.. note::

	Activer un mode d'exposition empêche la configuration manuelle de l'``ISO`` et du ``shutter speed``.

.. note::

	On ne peut changer l'ouverture mécanique de la PiCamera. Par contre, vous pouvez zoomer avec l'option décrite plus haut, mais sachez que l'ouverture reste fixe.

.. note::

	Poser l'``ISO`` ou le ``shutter speed`` à 0 activera l'ajustement automatique de ces paramètres.



.. _resolution:

Changer la résolution
=====================

L'application vous permet de changer la résolution de l'image. À l'ouverture du programme, la résolution sera de 1280x720 px (4:3). 
Il y a plusieurs résolutions préprogrammées dans la boîte ``Résolutions par défaut``. 
Pour en sélectionner une, appuyer sur celle désirée et confirmez votre choix en appuyant sur le bouton confirmer directement sous la boîte. 
Vous pouvez voir la résolution actuelle un peu plus bas. 
Si vous souhaitez configurer votre propre résolution, vous pouvez entrer la largeur et la hauteur de l'image dans les deux boîtes sous ``Résolution personnalisée``. 
Pour confirmer votre choix, appuyez sur le bouton directement sous les deux boîtes. Le bouton au-dessus sert aux résolutions préprogrammées.   


.. note::

	Pour entrer votre résolution personnalisée, vous devez entrer deux nombres entiers. La résolution doit être supérieure à 64x64 px, la résolutoin minimale de la PiCamera, 
	et inférieure à 2592x1944 px. 

.. note::

	Certains modes préprogrammés offrent un ``champ de vision`` partiel. Lorsque vous entrez une résolution personnalisée, le champ de vision sera toujours complet. 
	Si vous voulez le changer, utilisez la fonctionnalité ``Zoom``. Vous pouvez voir la configuration du champ de vision actuel sous la résolution actuelle.


.. _text:

Afficher un texte
=================


Vous pouvez annoter du texte sur la photo. Pour ce faire, écrivez le texte à annoter à côté de la boîte ``Personnalisé`` dans la section **Texte**. Vous pouvez voir un aperçu ce 
ce qui sera affiché dans l'aperçu en temps réel à droite. Vous pouvez aussi annoter le temps présent en cochant la boîte **Annoter le temps à la photo**. Il sera annoté sous le format
affiché juste au-dessous de la boîte. 



.. note::

	La fonction `annotate_text`_ ne peut contenir que les 128 caractères du code `ASCII`_, ce qui exclue les lettres accentuées.
	Écrire un caractère interdit le changera automatiquement par ``%`` pour vous en indiquer.



.. _annotate_text: https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.annotate_text
.. _ASCII: http://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html



.. _save:

Modification de la sauvegarde
=============================

Vous pouvez changer le format du fichier en appuyant sur les flèches de la ``spinbox`` dans la section ``Sauvegarde``. Les formats disponibles sont

	- ``'jpeg'`` - Encodage JPEG
	- ``'png'`` - Encodage PNG sans pertes
        - ``'gif'`` - Encodage GIF
        - ``'bmp'`` - Encodage Windows bitmap
        - ``'rgb'`` - Données images brutes en format 24-bit RGB
        - ``'rgba'`` - Données images brutes en format 32-bit RGBA

Vous pouvez modifier le nom du fichier de la capture en écrivant dans la boîte ``Nom du fichier``. Notez que le temps est ajouté suite au nom que vous aurez donné au fichier pour 
empêcher d'enregistrer une capture par-dessus une capture déjà existante. Appuyez sur le bouton ``Confirmer`` pour valider votre choix.

Si vous souhaitez enregistrer vos captures dans un autre répertoire vous pouvez commencer par ouvrir le 
menu **Fichier** et choisir un nouveau répertoire. Par défaut, le répertoire pour les photos est ``Capture/`` et celui des vidéos est ``Vidéo/``

Si vous n'êtes pas sûr de l'endroit de la sauvegarde ou du nom de fichier, vous pouvez voir un aperçu sous le bouton ``Confirmer``

.. _other:

Autres fonctionnalités
======================


* Changer le nombre de prise de photo en séquence

Pour changer le nombre de photos à prendre en séquence, cliquez sur les flèches de la ``spinbox`` dans la section ``Séquence`` du menu des commandes.



* Revirements et rotation

Vous pouvez effectuer un revirement horizontal, vertical ou une rotation de l'image en appuyant sur les boutons associés à ces fonctionnalités du menu des commandes.



* Tout réinitialiser

Vous pouvez réinitialiser l'application comme elle était à l'ouverture du programme dans le menu ``Fichier`` et en appuyant sur la commande **Tout réinitialiser**.




