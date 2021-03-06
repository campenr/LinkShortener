# Copyright 2016 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

import sys
import os
from argparse import ArgumentParser
from sqlalchemy.exc import IntegrityError

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.models import User


def add_user():
    """Add a new user to the User database."""

    parser = ArgumentParser()
    parser.add_argument("-u", "--username", dest="username", help="username for new user", required=True)
    parser.add_argument("-p", "--password", dest="password", help="password for new user", required=True)

    args = parser.parse_args()

    try:
        user = User.add_user(username=args.username, password=args.password)
    except IntegrityError:
        print('[ERROR] User with username %s already exists.' % args.username)
    except Exception as e:
        print('[ERROR] Failed to add user %s to users table. See stack trace for details.' % args.username)
        raise

    return

if __name__ == '__main__':
    add_user()