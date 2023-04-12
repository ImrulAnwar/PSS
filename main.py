import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout, \
    QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QPushButton, \
    QScrollArea, QGroupBox, QMessageBox
from PyQt5.QtGui import QFont, QGuiApplication
import sqlite3


def show_message():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Please answer each question!")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class PatientSupportSystem(QWidget):

    def __init__(self):
        super().__init__()
        self.patient_details = None
        self.questions = [
            {
                'question': 'Have you experienced chest pain or discomfort in the past month?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Do you have a family history of heart disease?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with high cholesterol?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced dizziness or headaches in the past month?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Do you have a family history of high blood pressure?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with kidney disease?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Do you experience shortness of breath or wheezing?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with asthma or COPD?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you been exposed to any environmental toxins, such as cigarette smoke or air '
                            'pollution?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced increased thirst or hunger?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you noticed any changes in your vision?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with gestational diabetes during pregnancy?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced sneezing or a runny nose in the past month?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Do you have a family history of allergies?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever had a severe allergic reaction?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced feelings of sadness or hopelessness in the past month?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with a mental health condition, such as depression or '
                            'anxiety?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any changes in sleep or appetite recently?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced pain in any specific areas of your body, such as your back?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you tried any pain management techniques, such as physical therapy or medication?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any changes in your level of pain in the past month?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any seizures or convulsions?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with a neurological disorder, such as Parkinson\'s or '
                            'multiple sclerosis?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any numbness or tingling sensations?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any abdominal pain or discomfort?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any changes in bowel movements or stool consistency?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with a gastrointestinal condition, such as Cron\'s or '
                            'ulcerative colitis?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you experienced any changes in weight or appetite recently?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you ever been diagnosed with an eating disorder, such as anorexia or bulimia?',
                'options': ['Yes', 'No']
            },
            {
                'question': 'Have you tried any specific diets or weight loss programs in the past?',
                'options': ['Yes', 'No']
            }
            # Add more questions here...
        ]
        self.medical_specialties = {
            "heart disease": "Cardiology",
            "high blood pressure": "Hypertension",
            "lung disease": "Pulmonology",
            "diabetes": "Endocrinology",
            "allergies": "Allergy and immunology",
            "mental health": "Psychiatry",
            "chronic pain": "Pain management",
            "neurological disorders": "Neurology",
            "gastrointestinal problems": "Gastroenterology",
            "weight or appetite changes": "Nutrition and weight management"
        }
        self.scores = {
            "Cardiology": 0,
            "Hypertension": 0,
            "Pulmonology": 0,
            "Endocrinology": 0,
            "Allergy and immunology": 0,
            "Psychiatry": 0,
            "Pain management": 0,
            "Neurology": 0,
            "Gastroenterology": 0,
            "Nutrition and weight management": 0
        }
        self.specializations = [
            'Cardiology',
            'Hypertension',
            'Pulmonology',
            'Endocrinology',
            'Allergy and immunology',
            'Psychiatry',
            'Pain management',
            'Neurology',
            'Gastroenterology',
            'Nutrition and weight management'
        ]

        self.setWindowTitle('Patient Support System')
        # Calculate the size and position of the window
        screen = QGuiApplication.primaryScreen()
        screen_rect = screen.geometry()
        width = int(screen_rect.width() * 0.6)
        height = int(width / 16 * 9)
        x = int((screen_rect.width() - width) / 2)
        y = int((screen_rect.height() - height) / 2)

        # Set the size and position of the window
        self.setGeometry(x, y, width, height)

        # Create stacked layout
        self.stacked_layout = QStackedLayout()
        # Create pages for stacked layout
        self.patient_form_page = QWidget()
        self.questions_page = QWidget()
        self.suggestions_page = QWidget()
        self.prescriptions_page = QWidget()

        # Create widgets for page 1
        self.label1 = QLabel("This is page 1")
        self.next_button1 = QPushButton("Next")
        # Create labels and text entry boxes
        self.nameLabel = QLabel('Name:')
        self.nameLineEdit = QLineEdit()

        self.ageLabel = QLabel('Age:')
        self.ageLineEdit = QLineEdit()

        self.genderLabel = QLabel('Gender:')
        self.genderLineEdit = QLineEdit()

        self.emailLabel = QLabel('Email:')
        self.emailLineEdit = QLineEdit()

        self.phoneLabel = QLabel('Phone No:')
        self.phoneLineEdit = QLineEdit()

        self.addressLabel = QLabel('Address:')
        self.addressLineEdit = QLineEdit()

        # Create layout for page 1
        patient_form_layout = QVBoxLayout()
        patient_form_layout.addWidget(self.label1)
        patient_form_layout.addWidget(self.nameLabel)
        patient_form_layout.addWidget(self.nameLineEdit)
        patient_form_layout.addWidget(self.ageLabel)
        patient_form_layout.addWidget(self.ageLineEdit)
        patient_form_layout.addWidget(self.genderLabel)
        patient_form_layout.addWidget(self.genderLineEdit)
        patient_form_layout.addWidget(self.emailLabel)
        patient_form_layout.addWidget(self.emailLineEdit)
        patient_form_layout.addWidget(self.phoneLabel)
        patient_form_layout.addWidget(self.phoneLineEdit)
        patient_form_layout.addWidget(self.addressLabel)
        patient_form_layout.addWidget(self.addressLineEdit)
        patient_form_layout.addWidget(self.next_button1)
        self.patient_form_page.setLayout(patient_form_layout)

        # Connect next button 1 to switch to page 2
        self.next_button1.clicked.connect(self.on_next_button_clicked)

        # Create widgets for page 2
        self.label2 = QLabel("Please Answer the following questions: ")
        self.submit_button = QPushButton("Submit")

        # Create a scroll area widget and set its properties
        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)

        # Create layout for page 2
        form = QWidget(scroll)
        scroll_layout = QVBoxLayout(form)
        page2_layout = QVBoxLayout()
        scroll.setWidget(form)
        page2_layout.addWidget(self.label2)
        page2_layout.addWidget(scroll, 1)
        page2_layout.addWidget(self.submit_button)
        self.questions_page.setLayout(page2_layout)

        # Create an empty list to store the radio buttons
        self.radio_buttons_questions = []
        self.radio_buttons_doctors = []
        ct = 0

        for question in self.questions:
            group_box = QGroupBox(question['question'])
            group_box_layout = QVBoxLayout()

            # Loop over options and create a radio button for each option
            for option in question['options']:
                ct += 1
                radio_button = QRadioButton(option)
                radio_button.setObjectName("RB" + str(ct))
                group_box_layout.addWidget(radio_button)
                # Add the radio button to the list
                self.radio_buttons_questions.append(radio_button)

            # Add group box to main layout
            group_box.setLayout(group_box_layout)
            scroll_layout.addWidget(group_box)

        # Connect next button 2 to switch to page 3
        self.submit_button.clicked.connect(self.on_submit_button_clicked)

        # Create widgets for page 3
        self.label3 = QLabel("This is page 3")
        self.choose_doctor_label = QLabel("Choose a doctor you want to visit: ")
        self.choose_button = QPushButton("Choose")
        self.table_widget = QTableWidget()

        scroll_layout_for_doctors = QVBoxLayout(form)

        # Create layout for page 3
        self.table_page_layout = QVBoxLayout()
        self.table_page_layout.addWidget(self.label3)
        self.table_page_layout.addWidget(self.table_widget)
        self.table_page_layout.addWidget(self.choose_doctor_label)
        self.suggestions_page.setLayout(self.table_page_layout)

        # Connect close button to close the application
        self.choose_button.clicked.connect(self.on_choose_button_clicked)

        # Add pages to stacked layout
        self.stacked_layout.addWidget(self.patient_form_page)
        self.stacked_layout.addWidget(self.questions_page)
        self.stacked_layout.addWidget(self.suggestions_page)
        self.stacked_layout.addWidget(self.prescriptions_page)

        # Set layout for widget
        self.setLayout(self.stacked_layout)

    def get_selected_answers(self):
        answers = []
        for i in range(0, len(self.radio_buttons_questions) - 1, 2):
            rb1 = self.radio_buttons_questions[i]
            rb2 = self.radio_buttons_questions[i + 1]
            if (not rb1.isChecked()) and (not rb2.isChecked()):
                return []
            if rb1.isChecked():
                answers.append(rb1.text())
            elif rb2.isChecked():
                answers.append(rb2.text())
        return answers

    def show_the_doctors_table(self, probable_disease):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT * FROM doctors WHERE specialization = '" + probable_disease + "';"
        # Get the query results as a list of rows
        rows = cursor.execute(sql_command).fetchall()
        conn.commit()
        conn.close()
        # Set the number of rows and columns in the table
        self.table_widget.setRowCount(len(rows))
        self.table_widget.setColumnCount(len(rows[0]))

        # Set the column headers
        headers = [description[0] for description in cursor.description]
        self.table_widget.setHorizontalHeaderLabels(headers)

        # Populate the table with the query results
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(i, j, item)
        # Resize columns and rows to fit the contents
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        # Show the table widget
        self.table_widget.show()

    def show_doctor_names(self, probable_disease):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT name FROM doctors WHERE specialization = '" + probable_disease + "';"
        # Get the query results as a list of rows
        doctor_names = cursor.execute(sql_command).fetchall()
        conn.commit()
        conn.close()

        # Create a radio button for each doctor name and add it to the layout
        for name in doctor_names:
            radio_button = QRadioButton(name[0])
            self.table_page_layout.addWidget(radio_button)
            self.radio_buttons_doctors.append(radio_button)
        self.table_page_layout.addWidget(self.choose_button)

    def update_scores(self, answers):
        multiplier = 10
        for i, ans in enumerate(answers):
            curr_index = int(i / 3)
            if ans == "Yes":
                self.scores[self.specializations[curr_index]] += multiplier
            if (i + 1) % 3 == 0:
                multiplier -= 1

    def on_submit_button_clicked(self):
        answers = self.get_selected_answers()
        # if all the questions aren't answered you can not submit
        if len(answers) != len(self.radio_buttons_questions) / 2:
            show_message()
            return
        self.update_scores(answers)
        probable_disease = max(self.scores, key=self.scores.get)
        # call the query now
        self.show_the_doctors_table(probable_disease)
        self.show_doctor_names(probable_disease)
        self.stacked_layout.setCurrentIndex(2)

    def on_next_button_clicked(self):
        self.stacked_layout.setCurrentIndex(1)
        # Retrieve the entries from the text boxes and store them in an array
        self.patient_details = [self.phoneLineEdit.text(), self.nameLineEdit.text(), self.ageLineEdit.text(),
                                self.genderLineEdit.text(), self.emailLineEdit.text(), self.phoneLineEdit.text(),
                                self.addressLineEdit.text()]
        print(self.patient_details)

    def on_choose_button_clicked(self):
        self.stacked_layout.setCurrentIndex(3)


if __name__ == '__main__':
    # Create a QFont object with the desired font family, size and weight
    font = QFont('Comic Sans MS', 12, QFont.Normal)
    app = QApplication([])
    # Set the default font of the application
    app.setFont(font)
    questionnaire = PatientSupportSystem()
    questionnaire.show()
    app.exec_()
