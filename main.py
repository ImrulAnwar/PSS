import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QPushButton, \
    QScrollArea, QGroupBox
from PyQt5.QtGui import QFont, QGuiApplication


class PatientSupportSystem(QWidget):
    def __init__(self):
        super().__init__()

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
        self.welcome_page = QWidget()
        self.questions_page = QWidget()
        self.page3 = QWidget()

        # Create widgets for page 1
        self.label1 = QLabel("This is page 1")
        self.next_button1 = QPushButton("Next")

        # Create layout for page 1
        page1_layout = QVBoxLayout()
        page1_layout.addWidget(self.label1)
        page1_layout.addWidget(self.next_button1)
        self.welcome_page.setLayout(page1_layout)

        # Connect next button 1 to switch to page 2
        self.next_button1.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(1))

        # Create widgets for page 2
        self.label2 = QLabel("This is page 2")
        self.next_button2 = QPushButton("Next")

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
        page2_layout.addWidget(scroll, 1)
        page2_layout.addWidget(self.label2)
        page2_layout.addWidget(self.next_button2)
        self.questions_page.setLayout(page2_layout)

        # List of questions and options
        questions = [
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

        for question in questions:
            group_box = QGroupBox(question['question'])
            group_box_layout = QVBoxLayout()

            # Loop over options and create a radio button for each option
            for option in question['options']:
                radio_button = QRadioButton(option)
                group_box_layout.addWidget(radio_button)

            # Add group box to main layout
            group_box.setLayout(group_box_layout)
            scroll_layout.addWidget(group_box)

        # Connect next button 2 to switch to page 3
        self.next_button2.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(2))

        # Create widgets for page 3
        self.label3 = QLabel("This is page 3")
        self.close_button = QPushButton("Close")

        # Create layout for page 3
        page3_layout = QVBoxLayout()
        page3_layout.addWidget(self.label3)
        page3_layout.addWidget(self.close_button)
        self.page3.setLayout(page3_layout)

        # Connect close button to close the application
        self.close_button.clicked.connect(self.close)

        # Add pages to stacked layout
        self.stacked_layout.addWidget(self.welcome_page)
        self.stacked_layout.addWidget(self.questions_page)
        self.stacked_layout.addWidget(self.page3)

        # Set layout for widget
        self.setLayout(self.stacked_layout)


if __name__ == '__main__':
    # Create a QFont object with the desired font family, size and weight
    font = QFont('Verdana', 12, QFont.Normal)
    app = QApplication([])
    # Set the default font of the application
    app.setFont(font)
    questionnaire = PatientSupportSystem()
    questionnaire.show()
    app.exec_()
