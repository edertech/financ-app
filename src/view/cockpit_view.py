import sys
import requests
import json
from PyQt5 import QtWidgets, uic
from model.cockpit_model import CockpitModel

ui_file = 'view/cockpit.ui'
Ui_CockpitView, QtBaseClass = uic.loadUiType(ui_file)
URL = 'http://localhost:5000/'


class CockpitView(QtWidgets.QMainWindow, Ui_CockpitView):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_CockpitView.__init__(self)
        self.setupUi(self)

        self.push_button_refresh.pressed.connect(self.refresh)
        self.push_button_quit.pressed.connect(self.quit)

    def refresh(self):
        self.model_fiis = load_recomendacoes('recomendacoes_fiis')
        self.model_dividendos = load_recomendacoes('recomendacoes_dividendos')
        self.model_valores = load_recomendacoes('recomendacoes_valores')
        self.model_encerradas = load_encerrados('ativos_encerrados')

        self.table_fiis.setModel(self.model_fiis)
        self.table_dividendos.setModel(self.model_dividendos)
        self.table_valores.setModel(self.model_valores)
        self.table_encerradas.setModel(self.model_encerradas)

        self.statusbar.showMessage('Done!')

    def quit(self):
        sys.exit()


# ==================== FUNCs ==================================================
def load_recomendacoes(method):
    resp = requests.get('{}{}'.format(URL, method))
    parsed_json = (json.loads(resp.content))
    ret = []
    for item in parsed_json:
        ret.append((item['ranking'], item['ativo'], item['participacao'],
                    item['precoAtual'], item['precoTeto'],
                    item['recomendacao']))
    return CockpitModel(ret)


def load_encerrados(method):
    resp = requests.get('{}{}'.format(URL, method))
    parsed_json = (json.loads(resp.content))
    ret = []
    for item in parsed_json:
        ret.append((item['ativo'], item['dataEncerramento']))
    return CockpitModel(ret, is_encerradas=True)
