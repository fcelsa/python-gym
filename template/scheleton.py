#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
scheleton.py: basic python script scheleton

Copyright (c) 2019 Fabio Celsalonga
MIT License

"""

# Built-in modules
import sys
import os
import argparse
import logging
from datetime import datetime


# 3rd party modules
# from pexpect import run, spawn
# from colorama import Fore, Style

# Local modules * esempio per definizione delle costanti.
from constants import Constants

__appname__ = "scheleton"
__version__ = "1.0.0"

logger = logging.getLogger(__appname__)


def main(args):
    # TODO: Do something more interesting here...
    print('Hello world! from script scheleton')


def setup_logger(args):
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    # todo: place them in a log directory, or add the time to the log's
    # filename, or append to pre-existing log
    fh = logging.FileHandler(__appname__ + ".log")
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()

    if args.verbose:
        ch.setLevel(logging.DEBUG)
    else:
        ch.setLevel(logging.INFO)

    # create formatter and add it to the handlers
    fh.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    ch.setFormatter(logging.Formatter(
        '%(message)s'
    ))
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Description printed to command-line if -h is called."
    )
    # during development, I set default to False so I don't have to keep
    # calling this with -v
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, help='verbose output')

    return parser.parse_args()


if __name__ == '__main__':
    try:
        start_time = datetime.now()

        args = get_arguments()
        setup_logger(args)
        logger.debug(start_time)

        main(args)

        finish_time = datetime.now()
        logger.debug(finish_time)
        logger.debug('Execution time: {time}'.format(
            time=(finish_time - start_time)
        ))
        logger.debug("#"*20 + " END EXECUTION " + "#"*20)

        sys.exit(0)

    except KeyboardInterrupt as e:  # Ctrl-C
        raise e

    except SystemExit as e:  # sys.exit()
        raise e

    except Exception as e:
        logger.exception("Something happened and I don't know what to do D:")
        sys.exit(1)
