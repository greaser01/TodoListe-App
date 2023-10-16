from pathlib import Path
import csv
categories = ["Einkaufen", "Haushalt", "Freizeit", "Arbeit"]
todos = []

class Todo:
    def __init__(self, text, cat):
        self.text = text
        self.status = "offen"
        self.cat = cat
    def getText(self):
        return self.text
    def getStatus(self):
        return self.status
    def getCat(self):
        return self.cat
    def setText(self, text):
        self.text = text
    def setStatus(self, status):
        self.status = status
    def setCat(self, cat):
        self.cat = cat



def createToDo():
    '''
    User inputs a Value for an ToDo entry and chooses an category according to his ToDo
    '''
    text = input("Gib dein TODO ein: ")
    print(categories)
    decide = input("Neue Kategorie oder alte?: (n/a)").lower()
    match decide:
        case "a":
            while True:
                cat = input("Welche Kategorie?: ")
                if cat in categories:
                    todo = Todo(text, cat)
                    todos.append(todo)
                    break

        case "n":
            while True:
                cat = input("Neue Kategorie: ")
                if cat not in categories:
                    categories.append(cat)
                    todo = Todo(text, cat)
                    todos.append(todo)
                    break
    print()
    print("------------------------------------------------------------------")
    for i in range(len(todos)): # show list of todos
        print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
    print("------------------------------------------------------------------")
    print()

def changeToDo():
    """
    User inputs the index of a ToDo to change the text to a new one
    """
    print()
    print("------------------------------------------------------------------")
    for i in range(len(todos)): # show list of todos
        print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
    print("------------------------------------------------------------------")
    print()

    i = int(input("Welchen ToDo möchtest du bearbeiten?: (Enter number)")) - 1
    print(f"ToDo: {todos[i].getText()}")
    newToDo = input("Änderung: ")
    todos[i].setText(newToDo)
    print("Changed the ToDo")
    print()
    print("------------------------------------------------------------------")
    for i in range(len(todos)): # show list of todos
        print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
    print("------------------------------------------------------------------")
    print()

def markAsDone():
    '''
    ask the user which entry should be marked as done and does so
    '''
    try:
        #user is not obligated to know that list count start at 0, therefore entry at 0 can be accessed with typing 1
        x= int(input("Gib die Zahl des abgeschlossenen Eintrags an: ")) - 1
        #prints the ToDo-entry which should be marked as done
        if x in range(len(todos)):
            print()
            print(f"{todos[x].getText()}: {todos[x].getStatus()}; {todos[x].getCat()}")
            print()
            #double checks
            if input("Ist das der richtige Eintrag? (y/n) ") == "y":
                todos[x].setStatus("fertig")
            #show current list-entrys
        print()
        print("------------------------------------------------------------------")
        for i in range(len(todos)): # show list of todos
            print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
        print("------------------------------------------------------------------")
        print()
    except:
        print("gib einen gültigen Eintrag an.")

def delete():
    """
    the user can enter the number of a todo to be deleted
    the numbers of all other todos get updated
    """
    x = int(input("Welchen ToDo möchtest du löschen?: (Enter number)")) - 1
    if x in range(len(todos)):    # checks if todo is in the dic
        print()
        print(f"{todos[x].getText()}: {todos[x].getStatus()}; {todos[x].getCat()}")
        print()

        # double check
        if input("Zu löschender Eintrag? (y/n): ") == "y":
            del todos[x]
        print()
        print("------------------------------------------------------------------")
        for i in range(len(todos)): # show list of todos
            print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
        print("------------------------------------------------------------------")
        print()
    else: print("Keine gültige Eingabe oder keine Einträge mehr")

def onlyOpen():
    """
    shows only the todos which are open
    """
    print()
    print("------------------------------------------------------------------")
    for i in range(len(todos)):
        if todos[i].getStatus() == "offen": # checks which are open
            print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
    print("------------------------------------------------------------------")
    print()

def searchCat():
    """
    lets user search for specific catogeries
    """
    print(categories)
    while True:
        search = input("Gib eine Kategorie an: ")
        if search in categories:    # checks if the catogerie is valid
            print()
            print("------------------------------------------------------------------")
            for i in range(len(todos)):
                if todos[i].getCat() == search:
                    print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
            print("------------------------------------------------------------------")
            print()
        else: print("Keine gültige Angabe!")

def keywords():
    """
    lets the user search for keywords or letters
    if there is no match then there is no output
    """
    keyword = input("Gib ein Schlüsselwort ein: ").lower()
    print()
    print("------------------------------------------------------------------")
    for i in range(len(todos)):
        if keyword in todos[i].getText().lower():
            print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
    print("------------------------------------------------------------------")
    print()

def createCSV(todos):
    with open("save.csv","w+") as save:
        for i in range(len(todos)):
            save.write(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}\n" )
