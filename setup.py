#!/usr/bin/env python

from distutils.core import setup

version = "0.14.1"

"""Setup script for pexif"""

setup (
    name = "thumbor-pexif",
    version = version,
    description = "A module for editing JPEG EXIF data",
    long_description = "This module allows you to parse and edit the EXIF data tags in a JPEG image.",
    author = "Ben Leslie",
    author_email = "benno@benno.id.au",
    url = "https://github.com/thumbor/pexif",
    download_url = "https://pypi.python.org/packages/source/t/thumbor-pexif/thumbor-pexif-%s.tar.gz" % version,
    license = "http://www.opensource.org/licenses/mit-license.php",
    py_modules = ["pexif"],
    scripts = ["scripts/dump_exif.py", "scripts/setgps.py", "scripts/getgps.py", "scripts/noop.py",
               "scripts/timezone.py"],
    platforms = ["any"],
    classifiers = ["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Topic :: Multimedia :: Graphics"]
    )


