from functions import writelistinfile, getListFromFile

while True:
    user_action = input("Enter The action\n")
    match user_action:
        case 'add':
            list = getListFromFile()
            l = input("Enter the item \n") + "\n"
            list.append(l)
            writelistinfile(list)

        case 'show':
            list = getListFromFile()
            for i, item in enumerate(list):
                item = item.strip()
                print(f"{i}. {item}")

        case 'exit':
            break
        case 'edit':
            list = getListFromFile()

            method = input("Edit by number or word \n")
            match method:
                case 'number':
                    try:
                        list = getListFromFile()
                        l = int(input("Enter the number to be changed\n"))
                        m = input("Enter the new name\n")
                        list[l-1] = m + "\n"
                        writelistinfile(list)
                    except ValueError:
                        print("Unable to edit number")
                        continue
                case 'word':
                    l = input("Enter the word to be changed\n")
                    i = list.index(l)
                    m = input("Enter the new name\n")
                    list[i] = m
                    writelistinfile(list)

            print("New list ")
            print(list)
        case 'complete':
            list = getListFromFile()
            l = int(input("Enter the item completed \n"))
            #list.remove(l)
            list.pop(l)
            writelistinfile(list)
            print(list)
        case w:
            print(f"Invalid Input {w}")

