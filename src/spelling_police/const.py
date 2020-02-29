# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import re, os
from pathlib import Path


RE_DICT_EXT_ENABLED = re.compile(r'\.bdic$', re.I)

RE_DICT_EXT_DISABLED = re.compile(r'\.bdic\.disabled$', re.I)

DICT_DIR = os.environ["QTWEBENGINE_DICTIONARIES_PATH"]
Path(DICT_DIR).mkdir(parents=True, exist_ok=True)
