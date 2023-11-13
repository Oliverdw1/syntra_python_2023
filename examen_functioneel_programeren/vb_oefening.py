
def manage_tasks():
    """De functie vraagt om input aan de gebruiker en naargelang die input verandert hij de dictionary"""
    while True:
        choice = input("Wat wil je doen?\nToevoegen, tonen, verwijderen, stoppen: ")
        if choice.lower() == "toevoegen":
            add_or_update(task_list)
        elif choice.lower() == "tonen":
            show_tasks(task_list)
        elif choice.lower() == "verwijderen":
            delete_task(task_list)
        elif choice.lower() == "stoppen":
            break


def add_or_update(tasks):
    """De functie vraagt om een naam, deadline en prioriteit, maakt hier een dict van en voegt deze dict toe aan de dict tasks"""
    taaknaam = input("Taaknaam: ")
    deadline = input("Deadline: ")
    prioriteit = input("Prioriteit (hoog/medium/laag): ")
    while prioriteit not in ["hoog", "medium", "laag"]:
        prioriteit = input("foute input, kies opnieuw uit hoog/medium/laag: ")
    new_task = {}
    new_task["naam"] = taaknaam
    new_task["deadline"] = deadline
    new_task["prioriteit"] = prioriteit
    global counter
    tasks[counter] = new_task
    counter += 1



def show_tasks(tasks):
    for prio in ["hoog", "medium", "laag"]:
        for task in tasks:
            if tasks[task]["prioriteit"] == prio:
                print_dict_nice(tasks[task])


def delete_task(tasks:dict):
    task_input = input("geef de naam van de taak die u wilt verwijderen: ")
    for task in tasks:
        if tasks[task]["naam"] == task_input:
            tasks.pop(task)
            return

def print_dict_nice(dictionary):
    last_key = list(dictionary)[-1]
    for key in dictionary:
        if key == last_key:
            print(f"{key}: {dictionary[key]}", end="")
        else:
            print(f"{key}: {dictionary[key]}", end=", ")
    print()

print("hello")
if __name__ == '__main__':
    #task_list = {}
    task_list = {1: {'naam': 'oizahzf', 'deadline': 'lahu', 'prioriteit': 'hoog'},
                 2: {'naam': 'oahoia', 'deadline': 'ioahia', 'prioriteit': 'laag'},
                 3: {'naam': 'alkalkn', 'deadline': 'lazhaln', 'prioriteit': 'medium'},
                 4: {'naam': 'lsqkhqhs', 'deadline': 'lqshlqs', 'prioriteit': 'laag'}}
    counter = 1
    manage_tasks()
    print(task_list)
print("world")