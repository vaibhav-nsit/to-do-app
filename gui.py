import functions
import FreeSimpleGUI as sg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as f:
        pass

label = sg.Text("Type TODO")

add_box = sg.InputText(tooltip="Enter your input", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.getListFromFile(), key="todos",
                      enable_events=True,size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")



window = sg.Window('My TODO',
                   layout=[[label],
                           [add_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],
                   font = ('Helvetica', 20),
                   )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            functions.addNewItem(values['todo'] + "\n")
            window["todos"].update(functions.getListFromFile())
        case "Edit":
            try:
                old_name = values['todos'][0]
                new_name = values['todo'] + "\n"
                functions.editItemByName(old_name, new_name)
                window["todos"].update(functions.getListFromFile())
            except IndexError:
                sg.popup("Invalid Input", font=("Helvetica", 20))
        case 'todos':
            window["todo"].update(value=values['todos'][0])
        case 'Complete':
            try:
                item = values['todos'][0]
                print(f"Remove {item}")
                functions.removeItemByName(item)
                window["todos"].update(functions.getListFromFile())
            except IndexError:
                sg.popup("Invalid Input", font=("Helvetica", 20))

        case "Exit":
            exit()
        case sg.WIN_CLOSED:
            break
window.close()
