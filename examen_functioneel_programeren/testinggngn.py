data = {
    1: {'naam': 'oizahzf', 'deadline': 'lahu', 'prioriteit': 'hoog'},
    2: {'naam': 'oahoia', 'deadline': 'ioahia', 'prioriteit': 'laag'},
    3: {'naam': 'alkalkn', 'deadline': 'lazhaln', 'prioriteit': 'medium'},
    4: {'naam': 'lsqkhqhs', 'deadline': 'lqshlqs', 'prioriteit': 'laag'}
}

# Define a custom function to assign a numeric value to each priority
def priority_value(item):
    priorities = {'hoog': 1, 'medium': 2, 'laag': 3}
    return priorities[item[1]['prioriteit']]

# Sort the dictionary based on the custom function
sorted_data = dict(sorted(data.items(), key=priority_value))

# Print the sorted dictionary
print(sorted_data)
print(data.items())

def optellen(*args):
    som = 0
    for i in args:
        som += i
    print(som)