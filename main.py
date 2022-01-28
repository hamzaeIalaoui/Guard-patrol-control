if __name__ == "__main__":

    from PyQt5.QtWidgets import QApplication

    import sys
    import gui
    
    app = QApplication(sys.argv)
    Mainwindow = gui.MainWindow()
    Mainwindow.setup(1000,685)
    Mainwindow.show()
    sys.exit(app.exec_())   