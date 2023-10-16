from functions import *
import psycopg2

def load(username):
    """
    Creates a connection to a defined Database.
    After the login the function uses the username to load all todos in the programm
    """
    conn = psycopg2.connect(host="localhost", dbname="todos", user="postgres", password="postgres", port=5432)  # connect to DB
    cur = conn.cursor()

    cur.execute(f"SELECT todo, status, categorie FROM todolist WHERE username='{username}'")
    res = cur.fetchall()

    for i in range(len(res)):
        todo = Todo(res[i][0], res[i][2])
        todo.setStatus(res[i][1])
        todos.append(todo)

    conn.commit()
    cur.close()
    conn.close()

def login():
    """
    Creates a connection to a defined Database.
    Gets all usernames and passwords from the database.
    Then lets you enter your username.
    If it exists you can enter your password. If it is the right one the function closes the connection and returns the user.
    """
    index = ""
    conn = psycopg2.connect(host="localhost", dbname="todos", user="postgres", password="postgres", port=5432)  # connect to DB
    cur = conn.cursor()

    cur.execute('SELECT * FROM userpass')

    res = cur.fetchall()

    print("|LogIn|")
    usercontrol = True
    while usercontrol:
        user = input("Username: ")
        for i in range(len(res)):
            if user == res[i][0]:
                index = i
                usercontrol = False
        if usercontrol:
            print("Benutzer nicht gefunden")


    
    passcontrol = True
    while passcontrol:
        passw = input("Password: ")
        for i in range(len(res)):
            if passw == res[index][1]:
                passcontrol = False
        if passcontrol:
            print("Passwort falsch!")
    print("Eingabe korrekt")

    conn.commit()
    cur.close()
    conn.close()
    return user

def newUser():
    """
    Creates a connection to a defined Database.
    Gets all users inside the database and saves them in a list.
    Then it lets you enter a new username. Checks if the username already exists and then persists that you enter a new one.
    If you enter a new username you can enter a password for that user.
    Then the username and its password get inserted into the table.
    Returns the username in the end
    """
    users = []
    conn = psycopg2.connect(host="localhost", dbname="todos", user="postgres", password="postgres", port=5432)  # connect to DB
    cur = conn.cursor()
    cur.execute("SELECT username FROM userpass")
    res = cur.fetchall()
    for i in range(len(res)):
        users.append(res[i][0])
    
    checking = True
    while checking:
        username = input("Gib einen gültigen Benutzername ein: ")
        if username not in users:
            checking = False
        if checking:
            print("Diesen Benutzer gibt es bereits!")
    passw = input("Gebe dein Passwort ein: ")
    cur.execute(f"INSERT INTO userpass(username, passw) VALUES('{username}','{passw}')")

    conn.commit()
    cur.close()
    conn.close()
    return username

def saveTodos(user):
    """
    Creates a connection to a defined Database.
    First it deletes all todos from the user inside the table and than it loads all new todos in it
    """
    conn = psycopg2.connect(host="localhost", dbname="todos", user="postgres", password="postgres", port=5432)  # connect to DB
    cur = conn.cursor()

    cur.execute(f"DELETE FROM todolist WHERE username='{user}'")
    for i in range(len(todos)):
        cur.execute(f"""INSERT INTO todolist(username, todo, status, categorie) 
                    VALUES('{user}','{todos[i].getText()}','{todos[i].getStatus()}','{todos[i].getCat()}')""")

    conn.commit()
    cur.close()
    conn.close()

def main():
    enter = input("Neuen Benutzer erstellen(e) oder einloggen(l)?: ")
    if enter == "l":
        user = login()
        load(user)
    elif enter == 'e':
        user = newUser()
        print("Benutzer erfolgreich angelegt")
    if len(todos) == 0:
        print("Keine bisherigen TODO's vorhanden")
    else:
        print()
        print("------------------------------------------------------------------")
        for i in range(len(todos)):
            print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
        print("------------------------------------------------------------------")
        print()

    while True: # runs as long the user wants
        enter = input("TODO hinzufügen(h)/bearbeiten(b)/löschen(l)/fertigstellen(f)/nur offene(o)/kategorisiern(k)/Schlüsselwort(s)/alle(a)/createCSV(c)? or quit(q): ").lower()
        match enter:
            case "h":   # add a ToDo
                while True:
                    createToDo()
                    print("Weiteres ToDo hinzufügen? (y/n): ")
                    if input() != "y":
                        break
            case "b":   # change a ToDo
                while True:
                    changeToDo()
                    print("Weiteres ToDo bearbeiten? (y/n): ")
                    if input() != "y":
                        break
            case "l":
                while True:
                    delete()
                    print("Weiteres ToDo löschen? (y/n): ")
                    if input() != "y":
                        break
            case "f":
                while True:
                    markAsDone()
                    print("Weiteres ToDo abschließen? (y/n): ")
                    if input() != "y":
                        break
            case "o":
                onlyOpen()
            case "k":
                searchCat()
            case "a":
                print()
                print("------------------------------------------------------------------")
                for i in range(len(todos)):
                    print(f"#{i+1} {todos[i].getText()}: {todos[i].getStatus()}; {todos[i].getCat()}")
                print("------------------------------------------------------------------")
                print()
            case "s":
                keywords()
            case "c":
                createCSV(todos)
            case "q":   # exit the programm
                saveTodos(user)
                break

main()