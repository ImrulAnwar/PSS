import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout, \
    QTableWidget, QTableWidgetItem, QLineEdit, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QPushButton, \
    QScrollArea, QGroupBox, QMessageBox
from PyQt5.QtGui import QFont, QGuiApplication
import sqlite3
from datetime import datetime


def show_message(msg_txt):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(msg_txt)
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
        self.radio_buttons_questions = []
        self.radio_buttons_doctors = []

        self.set_window_properties()
        self.create_pages()
        self.create_widgets_for_patient_form_page()
        self.create_layout_for_patient_page()
        scroll = self.create_widgets_for_questions_page()
        scroll_layout = self.create_layout_for_questions_page(scroll)
        self.create_widgets_for_suggestions_page()
        self.create_layout_for_suggestions_page()
        self.display_the_questions(scroll_layout)
        self.create_widgets_for_tables_page()
        self.create_layout_for_tables_page()
        self.connect_all_buttons()
        self.set_main_layout()

    def set_main_layout(self):
        # Add pages to stacked layout
        self.stacked_layout.addWidget(self.patient_form_page)
        self.stacked_layout.addWidget(self.questions_page)
        self.stacked_layout.addWidget(self.suggestions_page)
        self.stacked_layout.addWidget(self.tables_page)
        # Set layout for widget
        self.setLayout(self.stacked_layout)

    def connect_all_buttons(self):
        # connect all the buttons
        self.next_button.clicked.connect(self.on_next_button_clicked)
        self.submit_button.clicked.connect(self.on_submit_button_clicked)
        self.choose_button.clicked.connect(self.on_choose_button_clicked)
        self.close_button.clicked.connect(self.close)
        self.execute_button.clicked.connect(self.on_execute_button_clicked)

    def create_layout_for_tables_page(self):
        # Create layout for tables page
        self.tables_page_layout = QVBoxLayout()
        self.tables_page_layout.addWidget(self.tab_widget)
        self.tables_page_layout.addWidget(self.prescription_label)
        self.tables_page_layout.addWidget(self.close_button)
        self.tables_page.setLayout(self.tables_page_layout)

    def create_widgets_for_tables_page(self):
        self.prescription_label = QLabel("Prescription: \nYou should take medicine for ")
        # Create a QTabWidget to hold the tabs
        self.tab_widget = QTabWidget(self)
        # Create the Doctors tab and add a QTableWidget to it
        doctors_tab = QWidget()
        self.doctors_table = QTableWidget()
        doctors_tab_layout = QVBoxLayout()
        doctors_tab_layout.addWidget(self.doctors_table)
        doctors_tab.setLayout(doctors_tab_layout)
        self.tab_widget.addTab(doctors_tab, 'Doctors')
        # Create the Patients tab and add a QTableWidget to it
        patients_tab = QWidget()
        self.patients_table = QTableWidget()
        patients_tab_layout = QVBoxLayout()
        patients_tab_layout.addWidget(self.patients_table)
        patients_tab.setLayout(patients_tab_layout)
        self.tab_widget.addTab(patients_tab, 'Patients')
        # Create the Prescriptions tab and add a QTableWidget to it
        prescriptions_tab = QWidget()
        self.prescriptions_table = QTableWidget()
        prescriptions_tab_layout = QVBoxLayout()
        prescriptions_tab_layout.addWidget(self.prescriptions_table)
        prescriptions_tab.setLayout(prescriptions_tab_layout)
        self.tab_widget.addTab(prescriptions_tab, 'Prescriptions')
        self.close_button = QPushButton("Close")
        # Create the Execute SQL tab
        execute_sql_tab = QWidget()
        self.execute_sql_table = QTableWidget()
        execute_sql_tab_layout = QVBoxLayout()
        self.sql_query_label = QLabel('Enter your query: ')
        self.sql_query_line_edit = QLineEdit()
        self.execute_button = QPushButton("Execute!")
        execute_sql_tab_layout.addWidget(self.sql_query_label)
        execute_sql_tab_layout.addWidget(self.sql_query_line_edit)
        execute_sql_tab_layout.addWidget(self.execute_button)
        execute_sql_tab_layout.addWidget(self.execute_sql_table)
        execute_sql_tab.setLayout(execute_sql_tab_layout)
        self.tab_widget.addTab(execute_sql_tab, 'Execute SQL')


    def display_the_questions(self, scroll_layout):
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

    def create_layout_for_suggestions_page(self):
        # Create layout for suggestions page
        self.table_page_layout = QVBoxLayout()
        self.table_page_layout.addWidget(self.label3)
        self.table_page_layout.addWidget(self.table_widget)
        self.table_page_layout.addWidget(self.choose_doctor_label)
        self.suggestions_page.setLayout(self.table_page_layout)

    def create_widgets_for_suggestions_page(self):
        # Create widgets for suggestions page
        self.label3 = QLabel("These doctors are available: ")
        self.choose_doctor_label = QLabel("Choose a doctor you want to visit: ")
        self.choose_button = QPushButton("Choose")
        self.table_widget = QTableWidget()

    def create_layout_for_questions_page(self, scroll):
        # Create layout for questions page
        form = QWidget(scroll)
        scroll_layout = QVBoxLayout(form)
        page2_layout = QVBoxLayout()
        scroll.setWidget(form)
        page2_layout.addWidget(self.label2)
        page2_layout.addWidget(scroll, 1)
        page2_layout.addWidget(self.submit_button)
        self.questions_page.setLayout(page2_layout)
        return scroll_layout

    def create_widgets_for_questions_page(self):
        # Create widgets for questions page
        self.label2 = QLabel("Please Answer the following questions: ")
        self.submit_button = QPushButton("Submit")
        # Create a scroll area widget and set its properties
        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        return scroll

    def create_layout_for_patient_page(self):
        # Create layout for patient form page
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
        patient_form_layout.addWidget(self.next_button)
        self.patient_form_page.setLayout(patient_form_layout)

    def create_widgets_for_patient_form_page(self):
        # Create widgets for patient form page
        self.label1 = QLabel("Please fill up the following form: ")
        self.next_button = QPushButton("Next")
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

    def create_pages(self):
        # Create stacked layout
        self.stacked_layout = QStackedLayout()
        # Create pages for stacked layout
        self.patient_form_page = QWidget()
        self.questions_page = QWidget()
        self.suggestions_page = QWidget()
        self.tables_page = QWidget()

    def set_window_properties(self):
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

    def show_doctor_names(self):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT name FROM doctors WHERE specialization = '" + self.probable_disease + "';"
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
            show_message("Please answer each question!")
            return
        self.update_scores(answers)
        self.probable_disease = max(self.scores, key=self.scores.get)
        # call the query now
        self.show_the_doctors_table(self.probable_disease)
        self.show_doctor_names()
        self.stacked_layout.setCurrentIndex(2)

    def on_next_button_clicked(self):
        # Check if any of the line edits are empty
        for line_edit in [self.phoneLineEdit, self.nameLineEdit, self.ageLineEdit,
                          self.genderLineEdit, self.emailLineEdit, self.phoneLineEdit, self.addressLineEdit]:
            if line_edit.text().strip() == "":
                show_message("Please fill in all fields!")
                return
        self.stacked_layout.setCurrentIndex(1)
        # Retrieve the entries from the text boxes and store them in an array
        self.patient_details = [self.phoneLineEdit.text(), self.nameLineEdit.text(), self.ageLineEdit.text(),
                                self.genderLineEdit.text(), self.emailLineEdit.text(), self.phoneLineEdit.text(),
                                self.addressLineEdit.text()]

    def on_choose_button_clicked(self):
        # select what he chose
        selected_doctor = None
        for rb in self.radio_buttons_doctors:
            if rb.isChecked():
                selected_doctor = rb.text()
                break

        if selected_doctor is None:
            show_message("Please choose a Doctor!")
            return
        self.add_patient_to_the_database(selected_doctor)
        self.add_prescription_to_the_table()
        self.prescription_label.setText(f"Prescription: \n{self.prescription_text}")

        self.show_doctors_table()
        self.show_patients_table()
        self.show_prescription_table()
        # show all 3 table
        # show the prescription text
        self.stacked_layout.setCurrentIndex(3)

    def show_doctors_table(self):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT * FROM doctors;"
        # Get the query results as a list of rows
        rows = cursor.execute(sql_command).fetchall()
        conn.commit()
        conn.close()
        # Set the number of rows and columns in the table
        self.doctors_table.setRowCount(len(rows))
        self.doctors_table.setColumnCount(len(rows[0]))
        # Set the column headers
        headers = [description[0] for description in cursor.description]
        self.doctors_table.setHorizontalHeaderLabels(headers)
        # Populate the table with the query results
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.doctors_table.setItem(i, j, item)
        # Resize columns and rows to fit the contents
        self.doctors_table.resizeColumnsToContents()
        self.doctors_table.resizeRowsToContents()
        # Show the table widget
        self.doctors_table.show()

    def show_patients_table(self):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT * FROM patients;"
        # Get the query results as a list of rows
        rows = cursor.execute(sql_command).fetchall()
        conn.commit()
        conn.close()
        if len(rows) == 0:
            return
        # Set the number of rows and columns in the table
        self.patients_table.setRowCount(len(rows))
        self.patients_table.setColumnCount(len(rows[0]))
        # Set the column headers
        headers = [description[0] for description in cursor.description]
        self.patients_table.setHorizontalHeaderLabels(headers)
        # Populate the table with the query results

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.patients_table.setItem(i, j, item)
        # Resize columns and rows to fit the contents
        self.patients_table.resizeColumnsToContents()
        self.patients_table.resizeRowsToContents()
        # Show the table widget
        self.patients_table.show()

    def show_prescription_table(self):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT * FROM prescriptions;"
        # Get the query results as a list of rows
        rows = cursor.execute(sql_command).fetchall()
        conn.commit()
        conn.close()
        if len(rows) == 0:
            return
        # Set the number of rows and columns in the table
        self.prescriptions_table.setRowCount(len(rows))
        self.prescriptions_table.setColumnCount(len(rows[0]))
        # Set the column headers
        headers = [description[0] for description in cursor.description]
        self.prescriptions_table.setHorizontalHeaderLabels(headers)
        # Populate the table with the query results

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.prescriptions_table.setItem(i, j, item)
        # Resize columns and rows to fit the contents
        self.prescriptions_table.resizeColumnsToContents()
        self.prescriptions_table.resizeRowsToContents()
        # Show the table widget
        self.prescriptions_table.show()

    def add_prescription_to_the_table(self):
        prescriptions = {
            "Cardiology": "Take aspirin daily to reduce risk of heart attack.",
            "Hypertension": "Limit salt intake and exercise regularly to control blood pressure.",
            "Pulmonology": "Use an inhaler as directed to manage symptoms of asthma.",
            "Endocrinology": "Monitor blood sugar levels and take medication as prescribed to manage diabetes.",
            "Allergy and immunology": "Avoid allergens and take antihistamines as needed to manage allergies.",
            "Psychiatry": "Attend therapy sessions and take medication as prescribed to manage mental health.",
            "Pain management": "Use non-opioid pain relievers and participate in physical therapy to manage chronic "
                               "pain.",
            "Neurology": "Take medication as prescribed and attend therapy sessions to manage neurological disorders.",
            "Gastroenterology": "Avoid trigger foods and take medication as prescribed to manage gastrointestinal "
                                "problems.",
            "Nutrition and weight management": "Eat a balanced diet and exercise regularly to manage weight and "
                                               "appetite changes."
        }
        patient_id = self.patient_details[0]
        doctor_id = self.patient_details[8]
        prescription_id = patient_id + doctor_id
        probable_disease = self.patient_details[7]
        self.prescription_text = prescriptions[probable_disease]
        now = datetime.now()
        date_prescribed = now.strftime("%Y-%m-%d")
        # connect to the database and create a cursor object
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()

        # insert the values into the prescription table
        sql_command = f"INSERT INTO prescriptions (id, patient_id, doctor_id, prescription_text, date_prescribed) " \
                      f"VALUES ({prescription_id}, {patient_id}, {doctor_id}, '{self.prescription_text}', '{date_prescribed}');"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    def add_patient_to_the_database(self, selected_doctor):
        # add patient id, probable disease, assigned doctor
        self.patient_details.append(self.probable_disease)
        doctors_id = self.get_the_doctor_id(selected_doctor)
        self.patient_details.append(doctors_id)
        patient_id = self.patient_details[0]
        patient_name = self.patient_details[1]
        patient_age = self.patient_details[2]
        patient_gender = self.patient_details[3]
        patient_email = self.patient_details[4]
        patient_phone_number = self.patient_details[5]
        patient_address = self.patient_details[6]
        probable_disease = self.patient_details[7]
        assigned_doctor = self.patient_details[8]
        sql_command = "INSERT INTO patients (id, name, age, gender, email, phone, address, probable_disease, " \
                      "assigned_doctor) VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}');".format(
            patient_id, patient_name, patient_age, patient_gender, patient_email, patient_phone_number,
            patient_address, probable_disease, assigned_doctor)
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    def on_execute_button_clicked(self):
        conn = sqlite3.connect('PSS.db')
        try:
            cursor = conn.cursor()
            sql_command = self.sql_query_line_edit.text()
            rows = cursor.execute(sql_command).fetchall()
            self.show_the_table(rows, cursor)
            conn.commit()
            show_message("Query executed successfully!")
        except Exception as e:
            show_message("Please Enter a valid query!")
        finally:
            conn.close()

    def show_the_table(self, rows, cursor):
        if len(rows) == 0:
            return
        # Set the number of rows and columns in the table
        self.execute_sql_table.setRowCount(len(rows))
        self.execute_sql_table.setColumnCount(len(rows[0]))
        # Set the column headers
        headers = [description[0] for description in cursor.description]
        self.execute_sql_table.setHorizontalHeaderLabels(headers)
        # Populate the table with the query results
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.execute_sql_table.setItem(i, j, item)
        # Resize columns and rows to fit the contents
        self.execute_sql_table.resizeColumnsToContents()
        self.execute_sql_table.resizeRowsToContents()
        # Show the table widget
        self.execute_sql_table.show()

    def get_the_doctor_id(self, selected_doctor):
        conn = sqlite3.connect('PSS.db')
        cursor = conn.cursor()
        sql_command = "SELECT id FROM doctors WHERE name = '" + selected_doctor + "';"
        # Get the query results as a list of rows
        doctors_id = cursor.execute(sql_command).fetchall()
        doctors_id = str(doctors_id)
        conn.commit()
        conn.close()
        result = ""
        for char in doctors_id:
            if char.isdigit():
                result += char
        return str(result)


if __name__ == '__main__':
    # Create a QFont object with the desired font family, size and weight
    font = QFont('Comic Sans MS', 12, QFont.Normal)
    app = QApplication([])
    # Set the default font of the application
    app.setFont(font)
    questionnaire = PatientSupportSystem()
    questionnaire.show()
    app.exec_()
