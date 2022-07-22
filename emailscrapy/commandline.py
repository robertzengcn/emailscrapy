# -*- coding: utf-8 -*-

import argparse
from emailscrapy.version import __version__


def get_command_line(only_print_help=False):
    """
    Parse command line arguments when emailscrapy is used as a CLI application.

    Returns:
        The configuration as a dictionary that determines the behaviour of the app.
    """

    parser = argparse.ArgumentParser(prog='Emailscrapy',
                                     description='grab email from web site',
                                     epilog='Emailscrapy {version}. '
                                            'Please use it on your own risk. (c) by Robert Zeng'
                                            ', 2012-2019.')

    parser.add_argument('-u', '--url', type=str, action='store',
                        help='url pass to the program '
                        )


    parser.add_argument('-o-', '--output-filename', type=str, action='store', default='',
                        help='The name of the output file. If the file ending is "json", write a json file, if the '
                             'ending is "csv", write a csv file.')


    if only_print_help:
        parser.print_help()
    else:
        args = parser.parse_args()

        return vars(args)
