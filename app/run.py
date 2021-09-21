from website.grossbill import Grossbill
from website.minerstat import Minerstat
from website.kryptex import Kryptex
import pandas

# minerstat = Minerstat()
# element = minerstat.get_daily_returns()
# print(element)

kryp = Kryptex()
kryp.get_hashrates()

# gross = Grossbill()
# gross.main_page()