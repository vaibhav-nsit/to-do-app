def writelistinfile(list):
    with open("todo.txt", 'w') as f_r:
        f_r.writelines(list)

def getListFromFile():
    list = []
    with open("todo.txt", 'r') as f_r:
        list = f_r.readlines()
    return list


def addNewItem(item):
    list = getListFromFile()
    list.append(item)
    writelistinfile(list)

def editItemByNumber(num, newName):
    list = getListFromFile()
    list[int(num)-1] = newName
    print(f"Writting at {int(num)-1} Value {newName}")
    writelistinfile(list)

def editItemByName(oldName, newName):
    list = getListFromFile()
    index = list.index(oldName)
    list[index] = newName
    print(f"Writting at {index} Value {newName}")
    writelistinfile(list)

def removeItemByName(name):
    list = getListFromFile()
    list.remove(name)
    writelistinfile(list)
    print(f"Removing Value {name}")