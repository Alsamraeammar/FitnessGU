# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys # For system arguments if needed to run the app
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi # Reads the UI file
import kuntoilija # Home brew module for athlete objects
import timetools # DIY module for date and time calculations
# TODO: Import some library able to plot trends and make it as widget in the UI

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.nameLineEdit
        self.birthDateE = self.birthDateEdit
        self.genderCB = self.genderComboBox
        self.weighingDateE = self.weighingDateEdit

        # Set the weighing date to the current date
        self.weighingDateE.setDate(QtCore.QDate.currentDate()) 
        self.heightSB = self.heightSpinBox
        self.weightSB = self.weightSpinBox
        self.neckSB =  self.neckSpinBox
        self.waistSB = self.waistSpinBox 
        self.hipSB = self.hipSpinBox
        
        # TODO: Disable Calculate button until values have been edited
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)

        # TODO: Disable Save button until new values are calculated
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie methods

    # Calculates BMI, Finnish and US fat percentages and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value() # Spinbox value as an integer
        weight = self.weightSB.value()

        #  Convert birthday to ISO string using QtCore's methods
        birthday = self.birthDateE.date().toString(format=QtCore.Qt.ISODate)
        
        # Set Gender Value according to Combobox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1

        else:
            gender = 0

        # Convert Weighing day to ISO string    
        dateOfWeighing = self.weighingDateE.date().toString(format=QtCore.Qt.ISODate)
        
        # Calculate time difference using our home made tools
        age = timetools.datediff2(birthday, dateOfWeighing, 'year')

        # Create an athlete from Kuntoilija class
        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, dateOfWeighing)
        bmi = athlete.bmi

        self.bmiLabel.setText(str(bmi))

    # TODO: Make this method to save results to a disk drive
    # Saves data to disk
    def saveData(self):
        pass


if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())
    
