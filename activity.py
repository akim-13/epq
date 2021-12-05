import datetime
import os

# The location of the log file
log = '/home/akim/dox/cs/epq/activity.log'
# Open the activity log to append
log_a = open(f'{log}', 'a')


def format(inp, opt):
    opt = opt.upper()
    # Unformatted date and time
    unform_datetime = datetime.datetime.now()
    timestamp = unform_datetime.strftime('%d-%m-%Y %H:%m:%S %p')
    # Formatted input
    form_inp = f'\n[{timestamp}] ({opt}) {inp}'
    return form_inp


while True:
    inp = input('Enter an activity or option (h for help): ')
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
              'Q -- Quit\n')
    # Print the log file
    elif opt == 'p':
        # Prettier alternative to cat
        os.system(f'bat {log}')
        print()
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
        print()

