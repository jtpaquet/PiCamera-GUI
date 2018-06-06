# Main_template

from PiCameraGUI_template import PiCameraGUI_template
from tkinter import Tk, messagebox

# Exécute le programme
def run():
    try:
        win = Tk()
    except:
        messagebox.showerror("Erreur Tkinter", "Erreur d'initialisation de l'interface graphique")
        raise TkinterError("Erreur d'initialisation de Tkinter")
        print("Terminé")
        return 0

    win.resizable(width=False, height=False)
    appGeneral = PiCameraGUI_template(win,title="self.title")
    win.mainloop()
        
# Exécute le programme
if __name__ == "__main__":
    print("Initialisation de la fenêtre")
    run()
