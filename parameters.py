import argparse
import os


def parameter_parse():
    description = 'Check RPM(s)/driver(s) support status.'
    usage = 'usage'
    parser = argparse.ArgumentParser(usage=usage, description=description)
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument('-d', '--dir', dest='dir', help='RPM(s) in this dirctory')
    command_group.add_argument('-r', '--rpm', dest='rpm', help='RPM file')
    command_group.add_argument('-i', '--driver', dest='driver', help='driver file')
    command_group.add_argument('-s', '--system', action='store_true', help='check drivers running in the system')
    command_group.add_argument('-e', '--remote', dest='remote', help='check remote servers')

    parser.add_argument('-f', '--file', dest='file', help="output file name")
    parser.add_argument('-o', '--output', dest="output", choices=['html', 'excel', 'terminal', 'all'], default='terminal', help="output to a file")
    parser.add_argument('-q', '--query', dest="query", choices=['suse', 'vendor', 'unknow', 'all'], default='all', help='only show suse build, vendor build, unknow or all of them')

    args = parser.parse_args()
    if args.dir is not None:
        if os.path.isdir(args.dir) is False:
            print('Directory "(%s)" not found.' % (args.dir))
            exit(0)

        if args.output != 'terminal' and args.file is None:
            print('Please give a file name.')
            parser.print_help()
            exit(0)

        return args
    elif args.rpm is not None:
        if os.path.isfile(args.rpm) is False:
            print('File "(%s)" not found.' % (args.rpm))
            exit(0)

        return args
    elif args.driver is not None:
        if os.path.isfile(args.driver) is False:
            print('Driver "(%s)" not found.' % (args.driver))
            exit(0)

        return args
    elif args.system:
        if args.output != 'terminal' and args.file is None:
            print('Please give a file name.')
            parser.print_help()
            exit(0)

        return args
    elif args.remote is not None:
        if args.output != 'terminal' and args.file is None:
            print('Please give a file name.')
            parser.print_help()
            exit(0)

        return args
    else:
        parser.print_help()
        exit(0)
