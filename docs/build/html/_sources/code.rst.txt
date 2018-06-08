.. _code:

=================
Notes sur le code
=================

Voici un résumé de ce que fait le code. La plupart des commentaires sont déjà présents dans les fichiers, n'hésitez pas à les consulter au besoin.


.. _main:

Main.py
=======

En premier lieu, le programme essaie de détecter s'il y a des problèmes d'initialisation. 
D'abord, il détecte si Python peut bel et bien initialiser la fenêtre et, ensuite, si il peut initialiser l'objet `PiCamera`_.
S'il ne peut pas, il lèves deux types d'erreurs et propose des solutions exposées :ref:`exceptionsmodules`.
`
L'instance `app` de la classe :ref:`gui` est crée avec ``win`` comme ``root`` et ``camera`` comme objet ``PiCamera``. Le programme exécute ensuite la ligne::

	win.mainloop()

Essentiellement, il s'agit d'une boucle infinie dans laquelle la fenêtre réagit aux divers événements (cliques, touches, déplacements de la souris, etc.).
Pour mieux comprendre la fonction `mainloop()`_ de Tkinter, consulter le sujet `suivant`_ sur **Stack Overflow**. Techniquement, le programme n'est pas supposé quitter la boucle ``mainloop``, 
mais si c'est le cas, il se doit d'effacer l'instance `camera` pour éviter les problèmes de mémoire.


.. _PiCamera: https://picamera.readthedocs.io/en/release-1.10/index.html
.. _mainloop(): http://wiki.tcl.tk/2029
.. _suivant: https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


.. _gui:

PiCameraGUI.py
==============

Ce fichier contient la classe ``PiCameraGUI`` qui s'occupe de la création de l'interface ainsi que des fonctionnalités du programme.

.. currentmodule:: PiCameraGUI
.. autoclass:: PiCameraGUI
     :members:


.. _layout:

Disposition de l'interface
==========================

Si vous devez ajouter, modifier ou supprimer des fonctionnalités, vous devrez connaitre la disposition des objets dans la fenêtre.
Voici l'architecture du logiciel. Les `Frames` agissent comme des fenêtres qui contiennent les boutons et autres widgets. Les canvas servent à contenir les images.
Elles servent donc à l'organisation et à la disposition. Les ``buttons``, ``scales``, ``entry``, ``listbox``, ``spinbox`` servent à utiliser ou changer une fonctionnalité.

.. image:: _static/layout.png
	:align: center

* 1: self.seqButton
* 2: self.photoButton
* 3: self.videoButton
* 4: self.hflipButton
* 5: self.rotateButton
* 6: self.vflipButton
* 7: self.etatCanvas




