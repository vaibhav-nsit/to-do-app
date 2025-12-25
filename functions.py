def writelistinfile(list):
    with open("todo.txt", 'w') as f_r:
        f_r.writelines(list)

def getListFromFile():
    list = []
    with open("todo.txt", 'r') as f_r:
        list = f_r.readlines()
    return list


