#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import shutil, sys, subprocess
from time import sleep

PROJECT_ROOT = path.abspath(path.dirname(__file__))
REQUIREMENTS = path.join(PROJECT_ROOT, 'requirements.txt')

VE_ROOT = path.join(PROJECT_ROOT, 'env')


def go_to_ve():
    # going into ve
    if not sys.prefix == VE_ROOT:
        if sys.platform == 'win32':
            python = path.join(VE_ROOT, 'Scripts', 'python.exe')
        else:
            python = path.join(VE_ROOT, 'bin', 'python')

        retcode = subprocess.call([python, __file__] + sys.argv[1:])
        sys.exit(retcode)

update_ve = 'update_ve' in sys.argv
if update_ve:
    # install ve
    if not path.exists(VE_ROOT):
        import virtualenv
        sys.stderr.write('Creating virtualenv...')
        virtualenv.logger = virtualenv.Logger(consumers=[])
        virtualenv.create_environment(VE_ROOT, site_packages=False)
        sys.stderr.write('Done.')

    go_to_ve()
    # check requirements
    import pip
    pip.main(initial_args=['install', '-r', REQUIREMENTS])
    sys.exit(0)

if path.exists(VE_ROOT):
    go_to_ve()
    sys.stderr.write('Found virtualenv. Entering...\n')

# run django
from django.core.management import execute_manager
try:
    from proj import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory")
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
