import datetime

# Open the file to append.
log_a = open('activity.log', 'a')


def format(inp, entry):
    entry = entry.upper()
    datetime_unform = datetime.datetime.now()
    timestamp = datetime_unform.strftime('%d-%m-%Y %H:%m:%S %p')
    formatted_inp = f'[{timestamp}] ({entry}) {inp}'
    return formatted_inp

while True:
    
    inp = input('Enter an activity or specify\na type (h for help): ')
    entry = inp.lower()
    
    if entry == 'h':
        print('\nAvailable options: \n'
              'A -- Activity (Default)\n'
              'I -- Issue\n'
              'W -- Warning\n'
              'E -- Error\n'
              'R -- Resolved\n'
              'U -- Unresolved\n'
              'T -- To-Do\n'
              'P -- Print the log file\n'
              'Q -- Quit\n')
    
        format(inp, entry)
    elif entry == 'p':
        # Read the file.
        log_r = open('activity.log', 'r')
        print('\n' + log_r.read())
        log_r.close()
    elif entry == 'q':
        break
    # Default entry (Activity).
    else:
        print()

log_a.close()
