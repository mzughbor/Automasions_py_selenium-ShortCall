
from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard

app = Application(backend="uia").start('notepad.exe')
app.windows()

#app.UntitledNotepad.type_keys("%FX")

dlg = app['Untitled - Notepad']


#dlg.menu_select("View -> Status Bar")
#dlg.menu_select("File -> Save as")

dlg.menu_select("Edit -> Replace")
dlg.Replace.Cancel.click()
d.print_control_identifiers()
#dlg.Edit.type_keys('Welcome to Medium')

#   D:\shortcall\twitter_v3\twitter_v3-01

dlg.set_focus()
keyboard.send_keys('Hello')