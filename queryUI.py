import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from functools import partial
from query import doDemo  # Import the function from your OpenAI script

class FirebaseQueryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Research Query App")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.query_button = QPushButton("Query NoSQL DB")
        self.query_button.clicked.connect(self.run_query)
        layout.addWidget(self.query_button)

        central_widget.setLayout(layout)

    def run_query(self):
        user_input = self.input_field.text()
        file_names = doDemo(user_input)  # Call your OpenAI script function
        print(file_names)  # Print the result (you can update this as needed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirebaseQueryApp()
    window.show()
    sys.exit(app.exec_())