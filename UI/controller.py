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
        ddb = self._view.dropdown_biblioteca
        ddb.options.clear()
        ddb.options.append(ft.dropdown.Option(key="Niente", text="Nessun filtro"))
        for bibl in biblioteche:
            ddb.options.append(key=bibl.id, value=bibl.nome)

        ddb.value = "nessuno"


        libri = self._model.get_generi()
        ddg = self._view.dropdown_biblioteca
        ddg.options.clear()
        ddg.options.append(ft.dropdown.Option(key="Niente", text="Nessun filtro"))
        for bibl in biblioteche:
            ddg.options.append(key=bibl.id, value=bibl.nome)

        ddg.value = "nessuno"
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self,e):
        bibl = self._view.dropdown_biblioteca.value
        if bibl != "Niente":
            self.biblioteca_selezionata = bibl

    def seleziona_genere(self,e):
        gen = self._view.dropdown_genere.value
        if gen != "Niente":
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

        return lista_libri
