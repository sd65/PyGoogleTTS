import os
import sys
import textwrap
from urllib.parse import urlencode

command = "mpg123 -q "
googleTranslateUrl = "http://translate.google.com/translate_tts?"
params = urlencode({ "tl": "fr", "ie": "utf-8"})
text = textwrap.wrap(sys.argv[1], width=100)

for sub in text:
    text = urlencode({ "q": sub })
    cmd = command + "'%s'" % (googleTranslateUrl + params + "&" + text)
    os.system(cmd)
