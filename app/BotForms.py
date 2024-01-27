
from PyQt5.QtWidgets import (
    QFormLayout,
    QLineEdit,
    QDialog,
    QDialogButtonBox,
    QComboBox,
    QCheckBox
)

class BotForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.form = QFormLayout(self)

        self.nameInput = QLineEdit()
        self.symbolInput = QComboBox()
        self.marketTypeInput = QComboBox()
        self.exchangeInput = QComboBox()
        self.strategyInput = QComboBox()
        self.initialBalanceInput = QLineEdit()
        self.currentBalanceInput = QLineEdit()
        self.orderSizeInput = QLineEdit()
        self.runningInput = QCheckBox()

        # Añadir opciones a los comboboxes
        self.symbolInput.addItems(['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT'])
        self.marketTypeInput.addItems(['Spot', 'Futures'])
        self.exchangeInput.addItems(['Binance', 'Bitfinex', 'Kraken'])
        self.strategyInput.addItems(['GridBot', 'MeanReversionBot', 'DCABot', 'RSIBot'])

        self.form.addRow('Name', self.nameInput)
        self.form.addRow('Symbol', self.symbolInput)
        self.form.addRow('Market Type', self.marketTypeInput)
        self.form.addRow('Exchange', self.exchangeInput)
        self.form.addRow('Strategy', self.strategyInput)
        self.form.addRow('Initial Balance', self.initialBalanceInput)
        self.form.addRow('Current Balance', self.currentBalanceInput)
        self.form.addRow('Order Size', self.orderSizeInput)
        self.form.addRow('Running', self.runningInput)

        # Crear los botones de diálogo
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.form.addRow(self.buttons)