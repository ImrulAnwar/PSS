import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QButtonGroup
from PyQt5.QtGui import QFont


class HealthQuestionnaire(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Patient Support System')
        self.setGeometry(100, 100, 500, 500)

        # Add a vertical layout
        layout = QVBoxLayout(self)

        # Cardiology questions
        cardiology_label = QLabel('Cardiology (heart disease)', self)
        layout.addWidget(cardiology_label)
        question1_group = QButtonGroup(self)
        chest_pain_label = QLabel('Have you experienced chest pain or discomfort in the past month?', self)
        layout.addWidget(chest_pain_label)

        yes_chest_pain = QRadioButton('Yes', self)
        layout.addWidget(yes_chest_pain)
        question1_group.addButton(yes_chest_pain)
        no_chest_pain = QRadioButton('no', self)
        layout.addWidget(no_chest_pain)
        question1_group.addButton(yes_chest_pain)

        family_history_label = QLabel('Do you have a family history of heart disease?', self)
        layout.addWidget(family_history_label)

        no_family_history = QRadioButton('No', self)
        layout.addWidget(no_family_history)

        high_cholesterol = QRadioButton('Yes', self)
        layout.addWidget(high_cholesterol)

        high_cholesterol_label = QLabel('Have you ever been diagnosed with high cholesterol?', self)
        layout.addWidget(high_cholesterol_label)

        no_high_cholesterol = QRadioButton('No', self)
        layout.addWidget(no_high_cholesterol)

        # Hypertension questions
        hypertension_label = QLabel('Hypertension (high blood pressure)', self)
        layout.addWidget(hypertension_label)

        dizziness = QRadioButton('Yes', self)
        layout.addWidget(dizziness)

        dizziness_label = QLabel('Have you experienced dizziness or headaches in the past month?', self)
        layout.addWidget(dizziness_label)

        no_dizziness = QRadioButton('No', self)
        layout.addWidget(no_dizziness)

        hypertension_family_history = QRadioButton('Yes', self)
        layout.addWidget(hypertension_family_history)

        hypertension_family_history_label = QLabel('Do you have a family history of high blood pressure?', self)
        layout.addWidget(hypertension_family_history_label)

        no_hypertension_family_history = QRadioButton('No', self)
        layout.addWidget(no_hypertension_family_history)

        kidney_disease = QRadioButton('Yes', self)
        layout.addWidget(kidney_disease)

        kidney_disease_label = QLabel('Have you ever been diagnosed with kidney disease?', self)
        layout.addWidget(kidney_disease_label)

        no_kidney_disease = QRadioButton('No', self)
        layout.addWidget(no_kidney_disease)

        # Add a submit button
        submit_button = QPushButton('Submit', self)
        layout.addWidget(submit_button)
        submit_button.clicked.connect(self.submit)

    def closeEvent(self, event):
        # Stop the event loop when the window is closed
        QApplication.quit()

    def submit(self):
        # TODO: Add code to process the questionnaire answers
        pass


if __name__ == '__main__':
    # Create a QFont object with the desired font family, size and weight
    font = QFont('Verdana', 12, QFont.Normal)
    app = QApplication([])
    # Set the default font of the application
    app.setFont(font)
    questionnaire = HealthQuestionnaire()
    questionnaire.show()
    app.exec_()
