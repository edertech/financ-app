from PyQt5 import QtCore
from PyQt5.QtCore import QVariant, Qt

head_recomendadas = [
    'Ranking', 'Ativo', 'Alocação', 'Preço Atual', 'Preco Teto', 'Recomendação'
]
head_encerradas = ['Ativo', 'Data de Encerramento']


class CockpitModel(QtCore.QAbstractTableModel):
    def __init__(self, data_list, is_encerradas=False):
        QtCore.QAbstractTableModel.__init__(self)
        self.headers = head_encerradas if is_encerradas else head_recomendadas
        self.data_list = data_list

    def rowCount(self, parent):
        return len(self.data_list)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return self.data_list[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.headers[section]
