import flet as ft
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

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO

    def handler_btn_mostra_libri(self,e):
        lista_libri = self._model.get_libri_filtrati()
        self._view._list_view.controls.clear()
        for libro in lista_libri:
            self._view._list_view.controls.append(ft.Text(f"{libro}"))
            self._view.update()

