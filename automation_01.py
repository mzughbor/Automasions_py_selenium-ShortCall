from pywinauto.application import Application
from pywinauto import actionlogger
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import time
import logging
import argparse

# D:\shortcall\twitter_v3\twitter_v3-01\numbers.txt

parser = argparse.ArgumentParser()
parser.add_argument("--log", help = "enable logging", type=str, required = False)
args = parser.parse_args()

actionlogger.enable()
logger = logging.getLogger('pywinauto')

if args.log:
    logger.handlers[0] = logging.FileHandler(args.log)

app = Application(backend='uia').start(r'D:\shortcall\\twitter_v3\\twitter_v3-01\\Twitter_test.exe')
dlg = app.window(title_re='Twitter')
#dlg.print_control_identifiers()

#dlg.child_window(title="Select ..", auto_id="Btn_add_number", control_type="Button").click()
dlg.child_window(title="Prefix :", auto_id="TextBox2", control_type="Edit").set_text('NG')
dlg.child_window(title="Start", auto_id="Btn_Start", control_type="Button").click()
#file_name_edit = dlg.Twitter.child_window(title="File name:", control_type="Edit")
#file_name_edit.set_text('numbers.txt')
# CancelButton', 'StartButton', 'Button3', 'Start', 'Kill Process', 'Button4', 'Kill ProcessButton', 'Prefix :Edit', 'Edit', 'Prefix :Static', 'Prefix :', 'Static', 'Open File LocationStatic', 'Static0', 'Static1', 'Static2', 'Open File Location', 'Hyperlink', 'Open File LocationHyperlink', 'Open File Location0', 'Open File Location1', 'Open File Location2', '100', 'Static3', '100Static', "Number's :Static", "Number's :", 'Static4', 'Edit0', 'Edit1', 'Edit2', "Number's :Edit", 'Select ..Button', 'Button5', 'Select ..', 'TitleBar', 'Minimize', 'Button6', 'MinimizeButton', 'MaximizeButton', 'Button7', 'Maximize', 'CloseButton', 'Close', 'Button8'])'
