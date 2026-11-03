import flet as ft
from flet import value

from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd(self):
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        if biblioteche is None or generi is None:
            self._view.show_alert("Impossibile caricare i filtri")
            return

        ddb = self._view.dropdown_biblioteca
        ddb.options.clear()
        ddb.options.append(ft.dropdown.Option(key="Niente", text="Nessun filtro"))

        for bibl in biblioteche:
            ddb.options.append(ft.dropdown.Option(key=str(bibl.id), text=bibl.nome))

        ddb.value = "Niente"

        ddg = self._view.dropdown_genere
        ddg.options.clear()
        ddg.options.append(ft.dropdown.Option(key="Niente", text="Nessun filtro"))

        for genere in generi:
            ddg.options.append(ft.dropdown.Option(key=genere, text=genere))

        ddg.value = "Niente"
        self._view.update()
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self, e):
        bibl = self._view.dropdown_biblioteca.value
        if bibl == "Niente":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(bibl)

    def seleziona_genere(self, e):
        gen = self._view.dropdown_genere.value
        if gen == "Niente":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = gen

    # AZIONE: MOSTRA LIBRI
    # TODO

    def handler_btn_mostra_libri(self,e):
        lista_libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view._list_view.controls.clear()

        if lista_libri is None:
            self._view.show_alert("Impossibile recuperare i libri")
            return None

        for libro in lista_libri:
            self._view._list_view.controls.append(ft.Text(f"{str(libro)}"))
        self._view.update()

        if not lista_libri:
            self._view.show_alert("Nessun libro trovato")
