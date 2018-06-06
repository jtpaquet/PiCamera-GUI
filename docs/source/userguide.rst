.. _userguide:

======================
Guide de l'utilisateur
======================

À l'initialisation du logiciel, l'aperçu en temps réel devrait apparaître. Vous avez alors plusieurs fonctionnalités à votre disposition.

Note: Le prévisionnement est un `Overlay`_, ce qui signifie qu'il est généré «par-dessus» l'écran.
C'est pour cela qu'en déplaçant la fenêtre, il ne suit pas immédiatement la position de la fenêtre. Son ajustement est fait de manière à ce que sa position s'adapte lorsque le programme
détecte un mouvement de la fenêtre principale (`root`) et la fonction est seulement appelée lorsque le déplacement du `root` est complété.
On ne peut pas prendre de capture d'écran du prévisionnement puisque c'est un `Overlay`. C'est comme s'il était par-dessus la capture. Pour plus d'informations, consultez la `page`_
du module PiCamera sur l'aperçu et l'`Overlay`.

.. _Overlay: https://en.wikipedia.org/wiki/Overlay_(programming)
.. _page: https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.start_preview


Démarrage rapide
================



Zoomer
======




Changer la résolution
=====================





Afficher un texte
=================





Modifier l'endroit de la sauvegarde
===================================




Autres fonctionnalités
======================


* Changer le nombre de prise de photo en séquence



* Changer le temps de la capture vidéo



* Revirements et rotation







Ce `package`_ sert à afficher un label en survolant un objet Tkinter.

Par exemple, pour attacher un ToolTip au Label "self.modeLabel", il suffit d'appeler la fonction "createToolTip" à partir du fichier CallTipWindow.py 
et de mettre le widget parent en premier argument et le texte à afficher en deuxième argument.::

	from CallTipWindow import createToolTip

	note = "Activer un mode d'exposition\nempêche la configuration manuelle\nde l'iso et du shutter speed"
	createToolTip(self.modeLabel, note)


.. image:: tooltip.png
    :align: center

Note: L'auteur du programme PiCamera GUI ne détient pas les droits sur ce package et la license ne s'applique pas sur celui-ci. Les droits de ce package reviennent à Michael Foord.

