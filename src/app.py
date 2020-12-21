#!/bin/python
import sys

from PyQt5.QtWidgets import QApplication
from view.cockpit_view import CockpitView


def main():
    app = QApplication(sys.argv)
    view = CockpitView()
    view.show()
    app.exec_()


if __name__ == '__main__':
    main()
