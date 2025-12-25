import functions
import FreeSimpleGUI as sg

label = sg.Text("Type TODO")
input_box = sg.InputText(tooltip="Enter your input")
add_button = sg.Button("Add")

window = sg.Window('My TODO', layout=[[label], [input_box, add_button]])
window.read()
window.close()
