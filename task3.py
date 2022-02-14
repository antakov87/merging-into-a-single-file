import os

files = ['1.txt', '2.txt', '3.txt']


def creat_merg_file(files, filename):
    from operator import itemgetter
    all_lines = []
    for file in files:
        file_lines = [os.path.basename(file)]
        lines = []
        for line in open(file, encoding='utf-8'):
            lines.append(line[:-1])
        file_lines.append(str(len(lines)))
        file_lines.extend(lines)
        all_lines.append(file_lines)

    with open(filename, 'w', encoding='utf-8') as f:
        for lines in sorted(all_lines, key=itemgetter(1)):
            for line in lines:
                f.write(line + '\r')


creat_merg_file(files, 'new.txt')