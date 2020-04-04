# -*- coding: utf-8 -*-
def open_without_closing(filename):
    fd1 = open(filename, 'a')
    fd1.write('I wouldn\'t do with it anything\n')


def main():
    open_without_closing(filename)
    fd2 = open(filename, 'r')
    for line in fd2:
        print line,

if __name__ == '__main__':
    filename = r'C:\Heights\PortableApps\PortablePython2.7.6.1\App\hafifot\python101\temp_file.txt'
    main()