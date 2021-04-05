"""
Lump 63 - Disp Multiblend
=========================

This lump is not currently implemented. It will return the raw bytes.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402


@lump_raw
def lump_63(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
