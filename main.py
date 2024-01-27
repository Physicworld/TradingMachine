from PyQt5.QtWidgets import QApplication
from app.app import MyApp  # Asegúrate de que esta ruta de importación sea correcta

def main():
    app = QApplication([])

    # Crear la aplicación
    my_app = MyApp()
    my_app.show()

    app.exec_()

if __name__ == "__main__":
    main()