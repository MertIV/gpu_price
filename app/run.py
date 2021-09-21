from model.grossbill import Grossbill
from model.minerstat import Minerstat
from model.kryptex import Kryptex
import pandas

# minerstat = Minerstat()
# element = minerstat.get_daily_returns()
# print(element)

kryp = Kryptex()
kryp.get_hashrates()

# gross = Grossbill()
# gross.main_page()