# This module provides the main GUI window for the application
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDialog, QTextEdit, QFileDialog, QGroupBox, \
    QTabWidget, QCheckBox, QLineEdit, QDialogButtonBox
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import QtCore, QtWidgets
import sys

# custom library imports
from db_params import db_params
from pcap_store_params import pcap_store_params

main_window_text = "Welcome to the VoIP Monitor Configuration Generator!\n" + \
                   "Select the appropriate parameters from the 'Parameters' window to add to your " + \
                   "generated configuration and click the 'Generate Config' button. You can also" + \
                   "preview the configuration before generating it using the 'Preview Config' button.\n\n" + \
                   "You can click on any parameter to see the parameter description" + \
                   "on the 'Parameter Description' window."

# List of widgets to be stored for generating the config
# This will be populated by the parameter window tabs
# and will be consumed by the preview and generate
# callbacks
param_widgets = {
    "db_params": list(),
    "pcap_store_params": list(),

}

# Helper function to generate configuration file
def generate_configuration_file():
    config_text = ""
    param_type_text = {
        "db_params": "DATABASE PARAMETERS",
        "pcap_store_params": "PCAP STORAGE PARAMETERS",
    }

    for param_type in param_widgets:
        config_text += param_type_text[param_type] + "\n"
        for each_widget in param_widgets[param_type]:
            if each_widget[1].isEnabled() == True:
                config_text += each_widget[0] + " = " + each_widget[1].text() + "\n"
        config_text += "\n"
    return config_text

# The Main Window widget class
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # The main text to display at the top of the main window
        self.window_label = QLabel(main_window_text)
        self.window_label.setWordWrap(True)

        # Helper function to create a Tab window for parameters
        self._create_param_window()

        # Helper function to create control buttons
        self._create_buttons()

        # Create a layout to add elements to it
        self.layout = QtWidgets.QGridLayout(self)

        # Add widgets to the layout
        self.layout.addWidget(self.window_label, 0, 1)
        self.layout.addWidget(self.param_window_box, 1, 1)
        self.layout.addWidget(self.buttons_group, 2, 1)

        # Attach layout with the window
        self.setLayout(self.layout)

    # The callback to trigger when the 'Generate Config' button is clicked
    def generate_button_callback(self):
        self.config_dialog = GenerateConfigDialog()
        self.config_dialog.show()
        self.close()

    # The callback to trigger when the 'Preview Config' button is clicked
    def preview_button_callback(self):
        self.preview_dialog = PreviewConfigDialog()
        self.preview_dialog.show()

    # Internal method used inside the constructor to
    # Create widgets needed for the parameters window
    def _create_param_window(self):
        # The parent group box which holds the window
        # in order to add a title to it
        self.param_window_box = QGroupBox("Parameters")
        self.param_window_box_layout = QtWidgets.QHBoxLayout()
        self.param_window_box.setLayout(self.param_window_box_layout)

        # ====== CREATING THE MULTI-TAB PARAMETER WINDOW
        # The child tab widget to hold all the different
        # tab windows
        self.param_tab = QTabWidget()

        # Each parameter tab needs to have scroll area enabled
        self._create_db_param_tab()

        self.db_param_tab_scroll_area = QScrollArea()
        self.db_param_tab_scroll_area.setWidget(self.db_param_tab_item)

        self._create_pcap_store_param_tab()

        self.pcap_store_param_tab_scroll_area = QScrollArea()
        self.pcap_store_param_tab_scroll_area.setWidget(self.pcap_store_param_tab_item)

        # Add tab items to the tab
        self.param_tab.addTab(self.db_param_tab_scroll_area, "Database")
        self.param_tab.addTab(self.pcap_store_param_tab_scroll_area, "PCAP Store")

        # ======== END OF MULTI-TAB PARAMETER WINDOW

        # Create parameter description window in the same horizontal layout
        self.param_desc_window_box = QGroupBox("Parameter Description")
        self.param_desc_window_box_layout = QtWidgets.QHBoxLayout()
        self.param_desc_window_box.setLayout(self.param_desc_window_box_layout)
        self.param_desc_label = QLabel()
        self.param_desc_label.setWordWrap(True)
        self.param_desc_window_box_layout.addWidget(self.param_desc_label)

        # Add window to the QGroupBox
        self.param_window_box_layout.addWidget(self.param_tab)
        self.param_window_box_layout.addWidget(self.param_desc_window_box)
        self.param_window_box_layout.setStretch(1, 30)
        self.param_window_box_layout.setStretch(2, 10)

    def _create_db_param_tab(self):
        self.db_param_tab_item = QWidget()
        self.db_param_tab_item_layout = QtWidgets.QGridLayout(self)
        self.db_param_tab_item.setLayout(self.db_param_tab_item_layout)

        for i, each_item in enumerate(db_params):
            checkbox_widget = MyCheckBox(each_item)
            line_widget = QLineEdit(str(db_params[each_item].p_def_value))
            line_widget.setDisabled(True)

            checkbox_widget.stateChanged.connect(line_widget.setEnabled)
            checkbox_widget.clicked_str.connect(self.show_description)

            self.db_param_tab_item_layout.addWidget(checkbox_widget, i + 1, 1)
            self.db_param_tab_item_layout.addWidget(line_widget, i + 1, 2)

            param_widgets["db_params"].append([each_item, line_widget])

    def _create_pcap_store_param_tab(self):
        self.pcap_store_param_tab_item = QWidget()
        self.pcap_store_param_tab_item_layout = QtWidgets.QGridLayout(self)
        self.pcap_store_param_tab_item.setLayout(self.pcap_store_param_tab_item_layout)

        for i, each_item in enumerate(pcap_store_params):
            checkbox_widget = MyCheckBox(each_item)
            line_widget = QLineEdit(str(pcap_store_params[each_item].p_def_value))
            line_widget.setDisabled(True)

            checkbox_widget.stateChanged.connect(line_widget.setEnabled)
            checkbox_widget.clicked_str.connect(self.show_description)

            self.pcap_store_param_tab_item_layout.addWidget(checkbox_widget, i + 1, 1)
            self.pcap_store_param_tab_item_layout.addWidget(line_widget, i + 1, 2)

            param_widgets["pcap_store_params"].append([each_item, line_widget])

    def show_description(self, param_name):
        description = ""
        if param_name in db_params:
            description = db_params[param_name].get_desc()
        elif param_name in pcap_store_params:
            description = pcap_store_params[param_name].get_desc()

        self.param_desc_label.setText(description)

    # Creates widgets needed for control buttons at the bottom
    def _create_buttons(self):
        # The QGroupBox for orienting all the buttons at the bottom
        # will have a horizontal layout
        self.buttons_group = QGroupBox()
        self.buttons_group_layout = QtWidgets.QHBoxLayout()

        # The Generate configuration button with text
        self.generate_button = QPushButton("Generate Config")
        # Attach the callback with the button's clicked event
        self.generate_button.clicked.connect(self.generate_button_callback)

        # The Preview configuration button with text
        self.preview_button = QPushButton("Preview Config")
        # Attach the callback with the button's clicked event
        self.preview_button.clicked.connect(self.preview_button_callback)

        # The exit button
        self.exit_button = QPushButton("Exit")
        # Bind the callback to window's close function
        self.exit_button.clicked.connect(self.close)

        self.buttons_group_layout.addWidget(self.preview_button)
        self.buttons_group_layout.addWidget(self.generate_button)
        self.buttons_group_layout.addWidget(self.exit_button)

        self.buttons_group.setLayout(self.buttons_group_layout)


# This class implements a specific signal which can carry the checkbox name
# to the slot, to allow for parameter lookup
class MyCheckBox(QCheckBox):
    clicked_str = pyqtSignal(str)
    def __init__(self, *args):
        super(QCheckBox, self).__init__(*args)
        self.clicked.connect(self.update_description)

    def update_description(self):
        self.clicked_str.emit(self.text())


class Paramtab(QWidget):
    """This class represents the generic parameter tab functionality."""
    def __init__(self):
        super(QWidget, self).__init__()

        # TODO: Implement this class later


class DBParamTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()




class PCAPStoreParamTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QtWidgets.QGridLayout(self)
        self.setLayout(self.layout)

        for i, each_item in enumerate(pcap_store_params):
            checkbox_widget = QCheckBox(each_item)
            line_widget = QLineEdit(str(pcap_store_params[each_item].p_def_value))
            line_widget.setDisabled(True)

            checkbox_widget.stateChanged.connect(line_widget.setEnabled)

            self.layout.addWidget(checkbox_widget, i+1, 1)
            self.layout.addWidget(line_widget, i+1, 2)

            param_widgets["pcap_store_params"].append([each_item, line_widget])


# This class represents the dialog screen for the 'Generate Config' button
class GenerateConfigDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        # General configuration parameters
        self.setWindowTitle("Generate Config")

        # The choose file text
        self.choose_file_label = QLabel("Enter filename:")
        # The textbox to show the filename
        self.choose_file_text = QLineEdit()

        # The choose directory text
        self.choose_dir_label = QLabel("Choose directory by clicking 'Browse':")
        # The browse button for files
        self.choose_file_browse_button = QPushButton("Browse")
        # Bind a callback with the button to open FileDialog
        self.choose_file_browse_button.clicked.connect(self.browse_button_callback)

        # The label to display currently chosen dir
        self.current_dir = None
        self.current_dir_label = QLabel("Currently selected dir: None")
        # The save config button
        self.save_config_button = QPushButton("Save Config")
        # Bind a call back with the button to save config to file
        self.save_config_button.clicked.connect(self.save_config_button_callback)

        # Create widget layout
        self.layout = QtWidgets.QGridLayout()
        # Set the layout of the dialog box
        self.setLayout(self.layout)

        # Adding all widgets to the Dialog box
        self.layout.addWidget(self.choose_file_label, 1, 1)
        self.layout.addWidget(self.choose_file_text, 1, 2)
        self.layout.addWidget(self.choose_dir_label, 2, 1)
        self.layout.addWidget(self.current_dir_label, 3, 1)
        self.layout.addWidget(self.choose_file_browse_button, 3, 2)
        self.layout.addWidget(self.save_config_button, 4, 1)

    def browse_button_callback(self):
        # Create the FileDialog to browse for directory
        self.dialog_window = QFileDialog()
        # Set file mode to '2' to allow selecting only directories
        self.dialog_window.setFileMode(2)
        self.dialog_window.show()
        self.current_dir_label.setText(self.dialog_window.directory().path())

    def save_config_button_callback(self):
        # The filename to use
        dir = self.current_dir_label.text()
        filename = self.choose_file_text.text()
        if filename == "":
            # generate a dialog to say select a filename
            print("[DEBUG] Config not stored due to empty filename!\n")
        else:
            # generate a dialog to say config has been written to the file
            with (open(dir + "/" + filename, "w")) as file:
                file.write(generate_configuration_file())
                print("[DEBUG] Configuration written successfully to: {}\n".format(dir + "/" + filename))
                self.close()


def generate_dialog_with_label(label):
    pass

# This class represents the dialog window for the 'Preview Config' button
class PreviewConfigDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        # Configuration parameters of the Dialog
        self.setWindowTitle("Configuration Preview")
        self.resize(600, 450)

        self.label_text = "This what the generated configuration file will look like"
        # The text that will hold the generated text file
        self.config_text = generate_configuration_file()

        self.config_label = QLabel(self.label_text)
        self.show_config_text = QLabel(self.config_text)
        self.show_config_area = QScrollArea()
        self.show_config_area.setWidget(self.show_config_text)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.accept)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.layout.addWidget(self.config_label)
        self.layout.addWidget(self.show_config_area)
        self.layout.addWidget(self.button_box)


app = QApplication(sys.argv)

win = MainWindow()
win.setWindowTitle("VoIP Monitor Configuration Generator")
win.resize(500, 500)
win.show()

sys.exit(app.exec())
