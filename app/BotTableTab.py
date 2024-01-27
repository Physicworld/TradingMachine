from PyQt5.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QDialog,
    QDialogButtonBox
)

from .BotForms import BotForm

from Models.Bot import Bot
from DatabaseConnection.DatabaseConnection import DatabaseConnection

class BotTable(QWidget):
    def __init__(self):
        super().__init__()

        # Crear la conexión a la base de datos
        self.db = DatabaseConnection()

        # Crear los botones
        self.addButton = QPushButton('Add')
        self.editButton = QPushButton('Edit')
        self.deleteButton = QPushButton('Delete')

        # Conectar los botones a sus funciones correspondientes
        self.addButton.clicked.connect(self.addBot)
        self.editButton.clicked.connect(self.editBot)
        self.deleteButton.clicked.connect(self.deleteBot)

        # Crear el layout de los botones
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.editButton)
        buttonLayout.addWidget(self.deleteButton)

        # Crear la tabla
        self.table = QTableWidget()

        # Crear el layout principal y añadir la tabla y los botones
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.table)
        mainLayout.addLayout(buttonLayout)

        # Actualizar la tabla
        self.updateTable()

    def updateTable(self):
        # Obtener todos los bots de la base de datos
        bots = self.db.readModel(Bot)

        # Crear la tabla
        self.table.setRowCount(len(bots))  # Ajustar al número de bots
        self.table.setColumnCount(9)  # Ajustar al número de atributos de Bot

        # Configurar las cabeceras de las columnas
        self.table.setHorizontalHeaderLabels(["Name", "Symbol", "Market Type", "Exchange", "Strategy", "Initial Balance", "Current Balance", "Order Size", "Running"])

        # Añadir datos a la tabla
        for i, bot in enumerate(bots):
            self.table.setItem(i, 0, QTableWidgetItem(bot.name))
            self.table.setItem(i, 1, QTableWidgetItem(bot.symbol))
            self.table.setItem(i, 2, QTableWidgetItem(bot.market_type))
            self.table.setItem(i, 3, QTableWidgetItem(bot.exchange))
            self.table.setItem(i, 4, QTableWidgetItem(bot.strategy))
            self.table.setItem(i, 5, QTableWidgetItem(str(bot.initial_balance)))
            self.table.setItem(i, 6, QTableWidgetItem(str(bot.current_balance)))
            self.table.setItem(i, 7, QTableWidgetItem(str(bot.order_size)))
            self.table.setItem(i, 8, QTableWidgetItem('Running' if bot.running else 'Stopped'))

    def addBot(self):
        # Crear el formulario para añadir un bot
        self.dialog = BotForm()

        if self.dialog.exec_():
            bot_data = {
                'name': self.dialog.nameInput.text(),
                'symbol': self.dialog.symbolInput.currentText(),
                'market_type': self.dialog.marketTypeInput.currentText(),
                'exchange': self.dialog.exchangeInput.currentText(),
                'strategy': self.dialog.strategyInput.currentText(),
                'initial_balance': float(self.dialog.initialBalanceInput.text()),
                'current_balance': float(self.dialog.currentBalanceInput.text()),
                'order_size': float(self.dialog.orderSizeInput.text()),
                'running': self.dialog.runningInput.isChecked()
            }

            # Crear el bot en la base de datos
            new_bot = Bot(**bot_data)
            self.db.saveModel(new_bot)

            # Actualizar la tabla
            self.updateTable()

    def editBot(self):
        pass
        # Crear el formulario para editar un bot
        # Este código sería similar al de addBot(), pero necesitarías cargar los datos del bot seleccionado en la tabla en el formulario

    def deleteBot(self):
        pass
        # Implementar la lógica para eliminar un bot