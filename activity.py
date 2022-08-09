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

    if opt_num:
        opt_num += 1

    if opt == 'A':
        # Activities don't have "A" in the tag as
        # it is implied, they are only numbered.
        opt = ''
        if opt_num < 10:
            opt_num = f'00{opt_num}'
        elif opt_num < 100:
            opt_num = f'0{opt_num}'

    elif opt_num < 10:
        opt_num = f'0{opt_num}'

    fmt_inp = f'[{timestamp}] ({opt}{opt_num}) {inp}\n'
    return fmt_inp

# def sel_entry(entry_n):
#    # With...as is the same as file.open() and file.close(), but cleaner.
#    with open(f'{log}', 'r') as log_r:
#        entries = log_r.readlines()
#        lines_n = len(entries)
#
#    if entry_n == 'l':
#        return lines_n - 1
#    elif (entry_n.isdigit() and int(entry_n) <= lines_n
#                            and int(entry_n) > header_size):
#        return int(entry_n) - 1
#    else:
#        print('ERROR: Invalid entry number.')
#        return


def find_entry(tag):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        line_n = len(entries) - 1

    if tag == 'l' or tag == 'L':
        return line_n

    for i in range(line_n, -1, -1):
        cur_tag = entries[i][timestamp_l + 4 : timestamp_l + 7]
        if cur_tag == tag.upper():
            return i
        elif i == 0:
            print('ERROR: tag not found. A tag is the '
                  'contents of () in each entry.')
            return None

def has_annot(entry_n):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()

    # Because a fix or description is one entry below the current one.
    entry_n += 1
    try:
        tag = entries[entry_n][timestamp_l + 7]
    # Doesn't have annotations
    except IndexError:
        return 0

    cnt = 0
    while tag == 'D' or tag == 'F':
        cnt += 1
        entry_n += 1
        try:
            tag = entries[entry_n][timestamp_l + 7]
        # Last annotation is also the last line of the file
        except IndexError:
            break

    return cnt


def del_annot(n_of_annot, del_entry_n):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()

    # Because a fix or description is one entry below the current one.
    del_entry_n += 1

    for i in range(n_of_annot):
        #logging.debug(i)
        print(f'{i + 1}. {entries[del_entry_n + i]}')
    del_annot_n = input('Choose an annotation to delete or press '
                        'ENTER to delete the entry itself: ')
    print()
    if del_annot_n == '':
        del_entry_n -= 1
        for i in range(n_of_annot + 1):
            entry = entries[del_entry_n].replace('\n', '')
            print(f'Entry "{entry}" has been deleted.')
            del entries[del_entry_n]
    elif del_annot_n.isdigit() and int(del_annot_n) > 0 and int(del_annot_n) <= n_of_annot:
        del_annot_n = int(del_annot_n)
        entry = entries[del_entry_n + del_annot_n - 1].replace('\n', '')
        print(f'Entry "{entry}" has been deleted.')
        del entries[del_entry_n + del_annot_n - 1]
    else:
        print('ERROR: invalid annotation number.')
        return

    with open(f'{log}', 'w') as log_w:
        for entry in entries:
            log_w.write(entry)


def del_entry(tag):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()

    del_entry_n = find_entry(tag)

    if del_entry_n == None:
        return
    elif has_annot(del_entry_n) > 0:
        n_of_annot = has_annot(del_entry_n) 
        del_annot(n_of_annot, del_entry_n)
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
    # Position of the option in an entry in the log file.
    # Next time use regex instead of whatever this is... 
    opt_pos = timestamp_l + 4
    last = 0
    # Scan the file from the bottom to find the last entry.
    for i in range(lines_n - 1, 0, -1):
        char = entries[i]
        logging.debug(char[opt_pos])
        # FIXME: input: 'f' then 'l' to recreate
        if char[opt_pos] == opt:
            # The 2 digits after the option letter 
            # is the number of an issue/warning.
            last = int(char[opt_pos + 1 : opt_pos + 3])
            if last >= 99:
                # Not the most practical solution, but it doesn't really hurt 
                # the user, so might as well go for the aesthetics.
                last = 0
                print('\nOVERFLOW WARNING: the count has been reset!\n')
            break

        elif opt == 'A' and char[opt_pos].isdigit():
            last = int(char[opt_pos : opt_pos + 3])
            if last >= 999:
                last = 0
                print('\nOVERFLOW WARNING: the count has been reset!\n')
            break
        else:
            print('ERROR: invalid option.')
            return

    return last


def add_entry(opt, inp, name):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    if not inp:
        print('ERROR: no input has been provided.')
        return

    # Automatically capitilize the first letter.
    inp = inp.replace(inp[0], inp[0].upper(), 1) 
    last = find_last(entries, lines_n, opt)
    entry = fmt_entry(inp, opt, last)

    with open(f'{log}', 'a') as log_a:
         log_a.write(entry)

    entry = entry.replace('\n', '')
    print(f'{name} "{entry}" has been added.')


# FIXME
def annotate(tag, opt):
    with open(f'{log}', 'r') as log_r:
        entries = log_r.readlines()
        lines_n = len(entries)

    if tag == 'l' or tag == 'L':
        opt = input("Enter 'I' for last issue or 'W' for warning: ")
        last_tag_n = find_last(entries, lines_n, opt)
        entry_tag = opt + str(last_tag_n)
        # fix me or smth idk
        entry_n = find_entry(entry_tag)
    else:
        entry_n = find_entry(tag)
        entry_tag = tag.upper()[0]

    if not entry_n:
        return

    logging.debug(entry_tag)

    if opt == 'd' and (tag.isdigit() or entry_tag == 'W' or entry_tag == 'I'):
        opt_name = 'description'
        report = f'Added a description to {tag}' 
    elif entry_tag == 'W' or entry_tag == 'I':
        opt_name = 'fix'
        report = f'Fixed {tag}'
    else:
        print('ERROR: unable to annotate this type of entry.')
        return

    annot = input(f'Add a {opt_name} to "{tag}": ')
    if not annot:
        print(f'ERROR: no {opt_name} has been provided.')
        return

    cur_entry = entries[entry_n].replace('\n', '')

    last = find_last(entries, lines_n, opt)
    fmt_report = fmt_entry(report, 'a', last)
    fmt_annot = fmt_entry(annot, opt, None)
    entries[entry_n] = f'{cur_entry}\n  {fmt_annot}'
    entries.append(fmt_report)
    print(report)

#   actual_entry_n = sel_entry(entry_n) 
#   if actual_entry_n is None:
#       return

#   cur_entry = entries[actual_entry_n].replace('\n', '')
#   tag = cur_entry[timestamp_l + 4 : timestamp_l + 7]

#   # TODO: fix tag[1]=='A'
#   if opt == 'd' and (tag[1]=='A' or tag[0]=='W' or tag[0]=='I'):
#       opt_name = 'desctiption'
#       report = f'Added a description to {tag}' 
#       if tag[1] == 'A':
#           report = f'Added a description to A{actual_entry_n + 1}'

#   elif tag[0]=='W' or tag[0]=='I':
#       opt_name = 'fix'
#       report = f'Fixed {tag}'

#   else:
#       print('ERROR: unable to annotate this type of entry.')
#       return

#   annot = input(f'Add a {opt_name} to "{cur_entry}": ')
#   if not annot:
#       print(f'ERROR: no {opt_name} has been provided.')
#       return

#   fmt_report = fmt_entry(report, 'a', None)
#   fmt_annot = fmt_entry(annot, opt, None)
#   entries[actual_entry_n] = f'{cur_entry}\n  {fmt_annot}'
#   entries.append(fmt_report)
#   print(report)

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
        tag = input('Enter the tag of an issue/warning to add a fix to '
                      '(l for the last one): ')
        # TODO: change relative search to absolute (based on tags)
        annotate(tag, opt)

    # Add a description to an entry.
    elif opt == 'd':
        desc_n = input('Enter the tag of an entry you want to '
                       'add a description to (l for the last one): ')
        # TODO: change relative search to absolute (based on tags)
        # FIXME: annotate(tag, opt), look at the previous elif
        annotate(desc_n, opt)

    # Delete an entry.
    elif opt == 'x':
        tag = input('Enter the tag of an entry to be deleted: '
                        '(l for the last one): ')
        del_entry(tag)
    
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

    global timestamp_l
    timestamp_l = len(gen_timestamp())
    prepend_header()
    inp = None 
    while inp != 'q':
        inp = input('\nEnter an activity or option (h for help): ')
        sel_opt(inp)

    
if __name__ == '__main__':
    main()

