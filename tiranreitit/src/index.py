from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Reitit")                                 ## Luodaan aloitus näkymä Reitit

        aloitus_label = ttk.Label(master=self._root, text="Aloitus")                                ## Aloitus kenttä, etsitään aloitus tietokannasta
        aloitus_entry = ttk.Entry(master=self._root)

        maaranpaa_label = ttk.Label(master=self._root, text="Määränpää")                            ## Määränpää kenttä, etsitään määränpää tietokannasta
        maaranpaa_entry = ttk.Entry(master=self._root)

        etsi = ttk.Button(master=self._root, text="Etsi nopein reitti")                             ## Etsintä -nappi, tämä tulostaa käyttäjälle lyhyimmän/nopeimman reitin 

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        aloitus_label.grid(padx=5, pady=5)
        aloitus_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        maaranpaa_label.grid(padx=5, pady=5)
        maaranpaa_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        etsi.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

window = Tk()
window.title("TiranReitit")

ui = UI(window)
ui.start()

window.mainloop()