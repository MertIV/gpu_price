from website.grossbill import Grossbill
from website.minerstat import Minerstat
from website.kryptex import Kryptex
from app.helper.checker import similarity_check
from app.model.db import drop_tables,truncate_tables

# minerstat = Minerstat()
# minerstat.get_daily_income()

# drop_tables()
# truncate_tables()

# kryp = Kryptex()
# kryp.get_hashrates()

# kryp.selenium.driver.quit()

# print(similarity_check('RTX 3090','RTX 3090 LHR'))

print(similarity_check('RTX 3090TI','RTX 3090 TI'))

# gross = Grossbill()
# gross.main_page()

