.. _exceptionsmodules:

===================
Modules d'exception
===================

.. currentmodule:: Exceptions_ModuleCamera

Deux classes d'exceptions qui héritent de la classe `Exception`_ de la librairie standard de Python. Cela permet de créer deux nouveaux types d'erreurs: les PiCameraError TkinterError. 
Ces deux classes sont utilisées dans le fichier "Main.py". Si le logiciel ne détecte pas la PiCamera, il lèvera une PiCameraError et propose deux solutions:

* Débrancher et rebrancher la caméra
* Redémarrer le Rasperry Pi avec la caméra branchée

Si le logiciel ne peut importer les packages de la librairie Tkinter, il lèvera une TkinterError. Dans ce cas, il faut s'assurer d'avoir Python 3 sur le Raspberry Pi. Peut-être installer messagebox
La création des deux classes sont basées sur le modèle `suivant`_.

.. autoclass:: TkinterError
	        
.. autoclass:: PiCameraError



.. _Exception: https://docs.python.org/2/tutorial/errors.html
.. _suivant: https://docs.python.org/2/tutorial/errors.html#user-defined-exceptions