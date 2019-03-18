from sys import argv

file = argv[1]

fp = open(file)


def print_list():
    print("1 - insert a new task (a string of text)")
    print("2 - remove a task (by typing a substring)")
    print("3 - show all existing tasks")
    print("4 - close the program")

    ris = int(input("\nYour choice: "))
    return ris


def create():
    nuovo = input("\nInsert new task: ")
    vet.append(nuovo)
    print("Task inserted succesfully\n")


def remove():
    togli = input("\nInsert task to remove: ")
    for x in vet:
        if togli in x:
            vet.remove(x)
            print("Task removed succesfully\n")
            break
    print("The requested task doesn't exist\n")



def lists():
    print(sorted(vet))
    print()


def close():
    fp = open(file, "w")
    for x in vet:
        fp.write(x+"\n")
    fp.close()
    exit(0)


def wrong():
    print("\nInvalid choice\n")


def choose(argument):
    switcher = {
        1: create,
        2: remove,
        3: lists,
        4: close
    }

    func = switcher.get(argument, wrong)
    func()


vet=[]
vet = fp.readlines()
fp.close()
for i in range(0, len(vet)):
    vet[i]=vet[i].strip()

while 1:
    print("Insert the number corresponding to the action you want to perform:")
    choice = print_list()
    choose(choice)












