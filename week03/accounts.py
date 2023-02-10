# accounts.py
# Author: Kealan McGuinness
# Week03 weekly task account number

import re

ccstring = "123456789"
digitstokeep = 4
maskchar = "*"


ccstringtotal = sum(map(str.isdigit, ccstring))
digitstomask = ccstringtotal - digitstokeep
maskedccstring = re.sub('\d', maskchar, ccstring, digitstomask)

print (maskedccstring)
