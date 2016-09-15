# -*- Mode: python; indent-tabs-mode: nil; tab-width: 40 -*-
# vim: set filetype=python:
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def lint(files, **lintargs):
    return 1


LINTER = {
    'name': "BadReturnCodeLinter",
    'description': "Returns an error code no matter what",
    'include': [
        'files',
    ],
    'type': 'external',
    'extensions': ['.js', '.jsm'],
    'payload': lint,
}