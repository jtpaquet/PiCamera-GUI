#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ce fichier contient deux classes d'exceptions qui héritent de "Exception"


# Exception de Tkinter
class TkinterError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
        

# Exception de la PiCamera
class PiCameraError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
