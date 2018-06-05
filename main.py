# Main

from PiCameraGUI import PiCameraGUI
from Exceptions_ModuleCamera import TkinterError, PiCameraError
from tkinter import Tk, messagebox
from picamera import PiCamera

# Exécute le programme
def run():
    try:
        win = Tk()
    except:
        messagebox.showerror("Erreur Tkinter", "Erreur d'initialisation de l'interface graphique")
        raise TkinterError("Erreur d'initialisation de Tkinter")
        print("Terminé")
        return 0
    
    try:
        camera = PiCamera()  # Mode autre que 0 pour pouvoir changer de mode plus tard
        camera.sensor_mode = 0	# Retourne au mode 0
    except:
        messagebox.showerror("Erreur PiCamera", "Erreur d'initialisation de la caméra\nElle est peut-être mal installée\nSi ça ne marche toujours pas,\nveuillez redémarrer le Rapsberry Pi")
        raise PiCameraError("Erreur en créant l'instance de PiCamera")
        print("Terminé")
        return 0

    win.resizable(width=False, height=False)
    app = PiCameraGUI(win,camera,title="PiCamera")
    win.mainloop()

    camera.close()
        
# Exécute le programme
if __name__ == "__main__":
    print("Initialisation de la fenêtre")
    run()
