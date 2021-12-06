import datetime
import logging
import os

# The location of the log file.
log = '/home/akim/dox/cs/epq/activity.log'


def fmt_entry(inp, opt, opt_num):
    opt = opt.upper()

    # Unformatted date and time
    unfmt_datetime = datetime.datetime.now()
    global timestamp 
    timestamp = unfmt_datetime.strftime('%d-%m-%Y %H:%m')
    if opt_num == None:
        # Formatted input
        fmt_inp = f'[{timestamp}] ( {opt} ) {inp}\n'
    else:
        if opt_num < 10:
            fmt_inp = f'[{timestamp}] ({opt}0{opt_num}) {inp}\n'
        else:
            fmt_inp = f'[{timestamp}] ({opt}{opt_num}) {inp}\n'

    return fmt_inp


def del_entry(entry_n):
    # With...as is the same as file.open() and file.close(), but cleaner.
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    # Delete the last entry.
    if entry_n == 'l':
        fmt_entry = entries[-1].replace('\n', '')
        print(f'Entry "{fmt_entry}" has been deleted.')
        del entries[-1]

    elif entry_n.isdigit() and int(entry_n) <= lines_n:
        entry_n = int(entry_n)
        if entry_n == 0:
            print('Nothing has been deleted.')
            return
        fmt_entry = entries[entry_n - 1].replace('\n', '')
        print(f'Entry "{fmt_entry}" has been deleted.')
        del entries[entry_n - 1]

    else:
        print('Nothing has been deleted.')
        return

    with open(f'{log}', 'w') as log_w:
        for entry in entries:
            log_w.write(entry)


def find_last(entries, lines_n, opt):
    # Make the letter uppercase just in case.
    opt = opt.upper()
    global timestamp
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%m')
    # Position of the option in an entry in the log file.
    # Next time use regex instead of whatever this is... 
    opt_pos = len(timestamp) + 4
    last = 0
    # Scan the file from the end to find the last issue/warning.
    for i in range(lines_n - 1, 0, -1):
        char = entries[i]
        if char[opt_pos] == opt:
            # The 2 digits after the option letter 
            # is the number of an issue/warning.
            last = int(str(char[opt_pos + 1])
                             + str(char[opt_pos + 2]))
            logging.debug(last) 
            break

    return last


def add_issue(opt, inp):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    # Automatically capitilize the first letter.
    inp = inp.replace(inp[0], inp[0].upper(), 1) 
    last = find_last(entries, lines_n, opt)
    issue = fmt_entry(inp, opt, last + 1)

    with open(f'{log}', 'a') as log_a:
         log_a.write(issue)


def sel_opt(inp):
    opt = inp.lower()

    # Show the help menu if no input has been provided.
    if inp == '':
        opt = 'h'
    else:
        # Automatically capitilize the first letter.
        inp = inp.replace(inp[0], inp[0].upper(), 1) 
        # fmt_inp = fmt_entry(inp, opt)
    
    # Help menu 
    if opt == 'h':
        print('\nA - Activity (Default)\n\n'
              'Available options:\n'
              'I - Issue\n'
              'W - Warning\n'
              'R - Resolved\n'
              'F - Fixed\n'
              'T - To-Do\n'
              'D - Description to the last entry\n'
              'X - Delete an entry\n'
              'P - Print the log file\n'
              'Q - Quit')
    
    # Add an issue.
    elif opt == 'i':
        issue = input('Add an issue: ')
        add_issue(opt, issue)

    # Delete an entry.
    elif opt == 'x':
        entry_n = input('Enter the number of entry to be deleted '
                        '(l for the last one): ')
        del_entry(entry_n)
    
    # Print the log file.
    elif opt == 'p':
        # Prettier alternative to cat.
        os.system(f'bat {log}')
    
    # Quit.
    elif opt == 'q':
        return
    
    # Default option (Activity)
    else:
        opt = 'a'
        # Reformat the input for it to have the correct option.
        fmt_inp = fmt_entry(inp, opt, None)
        with open(f'{log}', 'a') as log_a:
            log_a.write(fmt_inp)
        # Print the log file.
        os.system(f'bat {log}')


def main():
    inp = None 
    while inp != 'q':
        inp = input('\nEnter an activity or option (h for help): ')
        sel_opt(inp)

    # Logging
    lvl = logging.DEBUG 
    fmt = '[%(levelname)s] %(lineno)s: %(msg)s'
    logging.basicConfig(level = lvl, format = fmt)
    # logging.info('')
    # logging.debug('')
    # logging.warning('')
    # logging.error('')
    
if __name__ == '__main__':
    main()

