import datetime
import os


def format(inp, opt):
    opt = opt.upper()
    # Unformatted date and time
    unform_datetime = datetime.datetime.now()
    timestamp = unform_datetime.strftime('%d-%m-%Y %H:%m:%S %p')
    # Formatted input
    form_inp = f'[{timestamp}] ({opt}) {inp}\n'
    return form_inp


def delEntry(entry_n):
    log_r = open(f'{log}', 'r')
    entries = log_r.readlines()
    lines_n = len(entries)
    log_r.close()

    # Delete the last entry
    if entry_n == 'l':
        form_entry = entries[-1].replace('\n', '')
        print(f'Entry "{form_entry}" has been deleted.')
        del entries[-1]
    elif entry_n.isdigit() and int(entry_n) <= lines_n:
        entry_n = int(entry_n)
        if entry_n == 0:
            print('Nothing has been deleted.')
            return
        form_entry = entries[entry_n - 1].replace('\n', '')
        print(f'Entry "{form_entry}" has been deleted.')
        del entries[entry_n - 1]
    else:
        print('Nothing has been deleted.')
        return

    log_w = open(f'{log}', 'w')
    for entry in entries:
        log_w.write(entry)
    log_w.close()

log = '/home/akim/dox/cs/epq/activity.log'
log_a = open(f'{log}', 'a')

while True:
    inp = input('\nEnter an activity or option (h for help): ')
    # Option
    opt = inp.lower()

    # Show the help menu if no input has been provided
    if inp == '':
        opt = 'h'
    else:
        # Automatically capitilize the first letter
        inp = inp.replace(inp[0], inp[0].upper(), 1) 
        form_inp = format(inp, opt)

    # Help menu
    if opt == 'h':
        print('\nAvailable options: \n'
              'A -- Activity (Default)\n'
              'I -- Issue\n'
              'W -- Warning\n'
              'E -- Error\n'
              'R -- Resolved\n'
              'U -- Unresolved\n'
              'T -- To-Do\n'
              'D -- Delete an entry\n'
              'P -- Print the log file\n'
              'Q -- Quit')
    # Delete an entry
    elif opt == 'd':
        entry_n = input('Enter the number of entry to be deleted '
                        '(l for the last one): ')
        delEntry(entry_n)
    # Print the log file
    elif opt == 'p':
        # Prettier alternative to cat
        os.system(f'bat {log}')
    # Quit
    elif opt == 'q':
        break
    # Default option (Activity)
    else:
        opt = 'a'
        form_inp = format(inp, opt)
        log_a.write(form_inp)
        # Re-open the file to save changes
        log_a.close()
        log_a = open(f'{log}', 'a')
        # Print the log file
        os.system(f'bat {log}')

