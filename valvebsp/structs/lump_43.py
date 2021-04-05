"""
Lump 43 - Texture Data String Data
==================================

This lump contains an array of :any:`string<string>`. They are texture names used by the level.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


@lump_array
def lump_43(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return CString("ascii")
