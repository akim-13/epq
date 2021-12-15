import datetime
import logging
import os


# The location of the log file.
log = '/home/akim/dox/cs/epq/activity.log'


def gen_timestamp():
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    return timestamp


def fmt_entry(inp, opt, opt_num):
    opt = opt.upper()
    # Automatically capitilize the first letter.
    inp = inp.replace(inp[0], inp[0].upper(), 1) 
    timestamp = gen_timestamp()

    if opt_num == None:
        fmt_inp = f'[{timestamp}] ( {opt} ) {inp}\n'
    elif opt_num < 10:
        fmt_inp = f'[{timestamp}] ({opt}0{opt_num}) {inp}\n'
    else:
        fmt_inp = f'[{timestamp}] ({opt}{opt_num}) {inp}\n'

    return fmt_inp


def sel_entry(entry_n):
    # With...as is the same as file.open() and file.close(), but cleaner.
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    if entry_n == 'l':
        return lines_n - 1
    elif (entry_n.isdigit() and int(entry_n) <= lines_n
                            and int(entry_n) > header_size):
        return int(entry_n) - 1
    else:
        print('ERROR: Invalid entry number.')
        return


def del_entry(entry_n):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()

    del_entry_n = sel_entry(entry_n)

    if del_entry_n == None:
        return
    else:
        entry = entries[del_entry_n].replace('\n', '')
        print(f'Entry "{entry}" has been deleted.')
        del entries[del_entry_n]

    with open(f'{log}', 'w') as log_w:
        for entry in entries:
            log_w.write(entry)


def find_last(entries, lines_n, opt):
    opt = opt.upper()
    timestamp = gen_timestamp()
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
            last = int(char[opt_pos + 1 : opt_pos + 3])
            break

    if last >= 99:
        # Not the most practical solution, but it doesn't really hurt 
        # the user, so might as well go for the aesthetics.
        last = 0
        print('\nOVERFLOW WARNING: the count has been reset!\n')

    return last


def add_entry(opt, inp, name):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    # Activities are not numbered, therefore 
    # there is no need in finding the last one.
    if opt == 'a':
        entry = fmt_entry(inp, opt, None)
    else:
        # Automatically capitilize the first letter.
        inp = inp.replace(inp[0], inp[0].upper(), 1) 
        last = find_last(entries, lines_n, opt)
        entry = fmt_entry(inp, opt, last + 1)

    with open(f'{log}', 'a') as log_a:
         log_a.write(entry)

    entry = entry.replace('\n', '')
    print(f'{name} "{entry}" has been added.')


def annotate(entry_n, opt):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()

    timestamp_len = len(gen_timestamp())
    actual_entry_n = sel_entry(entry_n)
    if actual_entry_n is None:
        return

    cur_entry = entries[actual_entry_n].replace('\n', '')
    tag = cur_entry[timestamp_len + 4 : timestamp_len + 7]

    if opt == 'd' and (tag[1]=='A' or tag[0]=='W' or tag[0]=='I'):
        opt_name = 'desctiption'
        report = f'Added a description to {tag}' 
        if tag[1] == 'A':
            report = f'Added a description to A{actual_entry_n + 1}'

    elif tag[0]=='W' or tag[0]=='I':
        opt_name = 'fix'
        report = f'Fixed {tag}'

    else:
        print('ERROR: unable to annotate this type of entry.')
        return

    annot = input(f'Add a {opt_name} to "{cur_entry}": ')
    fmt_report = fmt_entry(report, 'a', None)
    fmt_annot = fmt_entry(annot, opt, None)
    entries[actual_entry_n] = f'{cur_entry}\n  {fmt_annot}'
    entries.append(fmt_report)
    print(report)

    with open(f'{log}', 'w') as log_w:
        for entry in entries:
            log_w.write(entry)


def sel_opt(inp):
    opt = inp.lower()

    # Help menu 
    if opt=='h' or opt=='':
        print('\nA - Activity (Default)\n\n'
              'Available options:\n'
              'I - Issue\n'
              'W - Warning\n'
              'F - Fixed\n'
              'D - Description to an entry\n'
              'X - Delete an entry\n'
              'P - Print the log file\n'
              'Q - Quit')
    
    # Add an issue.
    elif opt == 'i':
        issue_inp = input('Add an issue: ')
        add_entry(opt, issue_inp, 'Issue')

    # Add a warning.
    elif opt == 'w':
        warning_inp = input('Add a warning: ')
        add_entry(opt, warning_inp, 'Warning')

    # Add a fix.
    elif opt == 'f':
        fix_n = input('Enter the line number of the entry you fixed '
                      '(l for the last one): ')
        annotate(fix_n, opt)

    # Add a description to an entry.
    elif opt == 'd':
        desc_n = input('Enter the line number of the entry you want to '
                       'add a description to (l for the last one): ')
        annotate(desc_n, opt)

    # Delete an entry.
    elif opt == 'x':
        entry_n = input('Enter the line number of an entry to be deleted '
                        '(l for the last one): ')
        del_entry(entry_n)
    
    # Print the log file.
    elif opt == 'p':
        # Prettier alternative to cat.
        os.system(f'bat {log}')
    
    # Quit.
    elif opt == 'q':
        return
    
    # Default option (Activity).
    else:
        opt = 'a'
        add_entry(opt, inp, 'Activity')


def prepend_header():
    header = ('    _        _   _       _ _            _                                    \n'
              '   / \\   ___| |_(_)_   _(_) |_ _   _   | | ___   __ _  __ _  ___ _ __       \n'
              '  / _ \\ / __| __| \\ \\ / / | __| | | |  | |/ _ \\ / _` |/ _` |/ _ \\ __|   \n'
              ' / ___ \\ (__| |_| |\\ V /| | |_| |_| |  | | (_) | (_| | (_| |  __/ |        \n'
              '/_/   \\_\\___|\\__|_| \\_/ |_|\\__|\\__, |  |_|\\___/ \\__, |\\__, |\\___|_|\n'
              '                               |___/            |___/ |___/                  \n'
              'Creator: Akim                                                                \n'
              'Source code: https://github.com/Jac0g/epq\n                                  \n'
              'Tags:                                                                        \n'
              '( A ) - Activity                                                             \n'
              '( D ) - Description                                                          \n'
              '( F ) - Fixed                                                                \n'
              '(I__) - Issue                                                                \n'
              '(W__) - Warning\n                                                            \n'
              '=====================================================================\n      \n')
    global header_size
    header_size = header.count('\n')

    with open(f'{log}', 'r+') as log_r:
        contents = log_r.read()
        # If there is no header, prepend one.
        if contents[0 : len(header)] != header[0 : len(header)]:
            log_r.seek(0)
            log_r.write(header + contents)


def main():
    # Logging
    lvl = logging.DEBUG 
    fmt = '%(lineno)s: [%(levelname)s] %(msg)s'
    logging.basicConfig(level = lvl, format = fmt)
    # logging.info('')
    # logging.debug('')
    # logging.warning('')
    # logging.error('')

    prepend_header()
    inp = None 
    while inp != 'q':
        inp = input('\nEnter an activity or option (h for help): ')
        sel_opt(inp)

    
if __name__ == '__main__':
    main()

