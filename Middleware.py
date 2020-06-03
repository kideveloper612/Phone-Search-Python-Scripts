import csv
import os


def source_read(file):
    file = open(file=file, encoding='utf-8')
    read_lines = file.readlines()
    file.close()
    return read_lines


def pass_read(file):
    if os.path.isfile(file):
        f = open(file=file, encoding='utf-8')
        read_lines = f.readlines()
        f.close()
        return read_lines
    else:
        return []


def write_phones(lines, file_name):
    file = open(file_name, 'w')
    l = map(lambda x: x + '\n', lines)
    file.writelines(l)
    file.close()


def execute(prefix):
    total = []
    source_file = '/home/ubuntu/laptop/{}.txt'.format(prefix)
    pass_file = '/home/ubuntu/laptop/output/pass_phones_{}.csv'.format(prefix)
    source = source_read(file=source_file)
    pass_phones = pass_read(file=pass_file)

    for phone in source:
        if phone not in pass_phones:
            total.append(phone.strip())

    print('========================')
    print('Pass: ', len(pass_phones))
    print('Source: ', len(source))
    print('Yet: ', len(total))
    write_phones(lines=total, file_name=source_file)
    try:
        if os.path.isfile(pass_file):
            os.remove(pass_file)
    except OSError as e:
        print(e.strerror)


if __name__ == '__main__':
    print('Start')
    file_prefix = 'Filtered'
    execute(prefix=file_prefix)
    print('Exit from main thread')

