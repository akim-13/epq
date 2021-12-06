import datetime
import os
import logging

# The location of the log file.
log = '/home/akim/dox/cs/epq/activity.log'


def fmtEntry(inp, opt):
    opt = opt.upper()

    # Unformatted date and time
    unfmt_datetime = datetime.datetime.now()
    timestamp = unfmt_datetime.strftime('%d-%m-%Y %H:%m')
    # Formatted input
    fmt_inp = f'[{timestamp}] ({opt}) {inp}\n'

    return fmt_inp


def delEntry(entry_n):
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


def selOpt(inp):
    opt = inp.lower()

    # Show the help menu if no input has been provided.
    if inp == '':
        opt = 'h'
    else:
        # Automatically capitilize the first letter.
        inp = inp.replace(inp[0], inp[0].upper(), 1) 
        # fmt_inp = fmtEntry(inp, opt)
    
    # Help menu 
    if opt == 'h':
        print('\nA -- Activity (Default)'
              '\nAvailable options: \n'
              'I -- Issue\n'
              'W -- Warning\n'
              'E -- Error\n'
              'R -- Resolved\n'
              'U -- Unresolved\n'
              'T -- To-Do\n'
              'D -- Delete an entry\n'
              'P -- Print the log file\n'
              'Q -- Quit')
    
    # Delete an entry.
    elif opt == 'd':
        entry_n = input('Enter the number of entry to be deleted '
                        '(l for the last one): ')
        delEntry(entry_n)
    
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
        fmt_inp = fmtEntry(inp, opt)
        with open(f'{log}', 'a') as log_a:
            log_a.write(fmt_inp)
        # Print the log file.
        os.system(f'bat {log}')


def main():
    inp = None 
    while inp != 'q':
        inp = input('\nEnter an activity or option (h for help): ')
        selOpt(inp)
    
    
if __name__ == '__main__':
    # Logging
    lvl = logging.DEBUG 
    fmt = '[%(levelname)s] %(lineno)s: %(msg)s'
    logging.basicConfig(level = lvl, format = fmt)
    # logging.info('')
    # logging.debug('')
    # logging.warning('')
    # logging.error('')

    main()

