.. _calltipwindow:

===============
Call Tip Window
===============

Ce `package`_ sert à afficher un label en survolant un objet Tkinter.

Par exemple, pour attacher un ToolTip au Label "self.modeLabel", il suffit d'appeler la fonction "createToolTip" à partir du fichier CallTipWindow.py 
et de mettre le widget parent en premier argument et le texte à afficher en deuxième argument.::

	from CallTipWindow import createToolTip

	note = "Activer un mode d'exposition\nempêche la configuration manuelle
		\nde l'iso et du shutter speed"
	createToolTip(self.modeLabel, note)


.. image:: _static/tooltip.png
    :align: center

Note: L'auteur du programme PiCamera GUI ne détient pas les droits sur ce package et la license ne s'applique pas sur celui-ci. Les droits de ce package reviennent à Michael Foord.

.. _package: http://www.voidspace.org.uk/python/weblog/arch_d7_2006_07_01.shtml#e387
