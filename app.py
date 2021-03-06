from qtpy.QtWidgets import QApplication, QListWidget, QDialog, QTabWidget, QGroupBox, QCheckBox, QComboBox, QWidget, QVBoxLayout, QDialogButtonBox, QLabel, QLineEdit
import sys
from qtpy.QtGui import QIcon

class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("First Python App!")
        self.setWindowIcon(QIcon("./myicon.png"))

        tabwidgt = QTabWidget()
        self.firstTab = FirstTab()
        # self.secondTab = SecondTab()
        tabwidgt.addTab(self.firstTab,"Information")
        # tabwidgt.addTab(self.secondTab, "Result")
        # tabwidgt.addTab(ThirdTab(), "Information")

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.firstTab.save)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidgt)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)


class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name:")
        nameEdit = QLineEdit()
        self.nameEdit = nameEdit

        dob = QLabel("Birth Date:")
        dobEdit = QLineEdit()
        self.dobEdit = dobEdit

        phone = QLabel("Phone Number:")
        phoneEdit = QLineEdit()
        self.phoneEdit = phoneEdit

        address = QLabel("Address:")
        addressEdit = QLineEdit()
        self.addressEdit = addressEdit

        layout = QVBoxLayout()
        layout.addWidget(name)
        layout.addWidget(nameEdit)
        layout.addWidget(dob)
        layout.addWidget(dobEdit)
        layout.addWidget(phone)
        layout.addWidget(phoneEdit)
        layout.addWidget(address)
        layout.addWidget(addressEdit)
        self.setLayout(layout)

    def save(self):
        name = self.nameEdit.text()
        dob = self.dobEdit.text()
        phone = self.phoneEdit.text()
        address = self.addressEdit.text()
        print(name, dob, phone, address)


class SecondTab(QWidget):
    def __init__(self):
        super().__init__()

        selectGroup = QGroupBox("Select Operationg Systems")
        combo = QComboBox()
        list = ["Windows","Mac","Linux","Fedora","Kali"]
        combo.addItems(list)
        selectLayout = QVBoxLayout()
        selectLayout.addWidget(combo)
        selectGroup.setLayout(selectLayout)

        checkGroup = QGroupBox("Which Operating System You Like?")
        windows = QCheckBox("Windows")
        mac = QCheckBox("Mac")
        linux = QCheckBox("Linux")
        checkLayout = QVBoxLayout()
        checkLayout.addWidget(windows)
        checkLayout.addWidget(mac)
        checkLayout.addWidget(linux)
        checkGroup.setLayout(checkLayout)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(selectGroup)
        mainLayout.addWidget(checkGroup)
        self.setLayout(mainLayout)



class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Terms And Conditions")
        listwidget = QListWidget()
        list = []

        for i in range(1,20):
            list.append("This Is Terms and Conditions")

        listwidget.insertItems(0,list)

        checkbox = QCheckBox("Agree The Terms And Conditions")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(listwidget)
        layout.addWidget(checkbox)

        self.setLayout(layout)


if __name__=="__main__":
    app = QApplication(sys.argv)
    tabwidgt = TabWidget()
    tabwidgt.show()
    app.exec()