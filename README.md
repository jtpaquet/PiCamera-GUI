# [PiCamera-GUI](http://picamera-gui.readthedocs.io/en/latest/)

Ce programme fournit un interface graphique (GUI) pour le [module de caméra](https://www.raspberrypi.org/products/camera-module-v2/) de [Raspberry Pi](https://www.raspberrypi.org/).
Ce programme est écrit dans le language de programmation [Python](https://www.python.org/) à l'aide de la librarie Tkinter.


### Fonctionnalités

* Aperçu en temps réel
* Aperçu de la photo prise
* Prise de photo, vidéo et de photos en séquence
* Zoom et déplacement à l'intérieur de l'image en temps réel
* Ajout de texte et du temps présent sur la photo
* Différents formats de photo supportés
* Rotation et revirement horizontal et vertical de l'image

### Installation de Python 3

Le plus important est de s'assurer que votre système contient les packages de la picamera. Pour ce faire, entrez la commande suivante dans l'invite de commande de votre Raspberry Pi


```
	$ sudo apt-get update
	$ sudo apt-get install python3-picamera
```

Si vous éprouvez des difficultés pour mettre à jour votre Raspberry Pi, consultez cette [page](https://picamera.readthedocs.io/en/release-1.10/install3.html) bien détaillée de la documentation du package [PiCamera](https://picamera.readthedocs.io/en/release-1.10/index.html).

### Télécharger le projet

Vous pouvez importer le projet en entrant la commande suivante

```	
	$ sudo apt-get install git
	$ git clone https://github.com/jtpaquet/PiCamera-GUI
```

Sinon, vous pouvez télécharger le projet en tant que fichier compressé .zip et le déplacé dans le répertoire voulu.


### Ouvrir l'application


Déplacer le fichier ayant cette icône sur le bureau de votre Raspberry Pi. Copiez le chemin du fichier (*right click > copy path*) du fichier ``PiCamera_exec`` et coller le chemin dans le fichier avec l'icône déplacé sur le bureau.

En ouvrant ce fichier, l'interface graphique devrait s'ouvrir et vous devriez pouvoir l'utiliser. Assurez vous que la PiCamera soit bien branchée. Si l'erreur persiste, essayez de redémarrer le Rapsberry Pi.

Sinon, vous pouvez ouvrir l'invite de commande dans le répertoire dans lequel se trouve les fichier et entrer la ligne de commande

```
	$ python3 picamera-gui/main.py
```

## Crée avec

* [Tkinter](https://docs.python.org/2/library/tkinter.html) - La librairie de l'interface graphique utilisé
* [TipTool Window](http://www.voidspace.org.uk/python/weblog/arch_d7_2006_07_01.shtml#e387) - Un package crée par Michael Foord


## Contribution

Please read [CONTRIBUTING.md](https://github.com/jtpaquet/PiCamera-GUI/graphs/contributors) for details on our code of conduct, and the process for submitting pull requests to us.

## Auteurs

* **Jérémy Talbot-Pâquet** - *Initial work* - [Jtpaquet](https://github.com/jtpaquet)

Consultez aussi la liste des [collaborateurs](https://github.com/jtpaquet/PiCamera-GUI/graphs/contributors) pour savoir qui a contribué à cette application.

## Licence

* Ce code est licencé sous la [Licence BSD](https://opensource.org/licenses/BSD-3-Clause). Consultez le fichier [rights.rst](rights.rst) pour plus de détails.

## Autres

* Toute la [documentation](http://picamera-gui.readthedocs.io/en/latest/) est disponible sur ReadTheDocs
* Merci à la documentation complète sur les modules de la [Pi Camera](https://picamera.readthedocs.io/) accesssible sur Read The Docs
