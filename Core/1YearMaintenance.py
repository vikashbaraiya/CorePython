import datetime
from datetime import timedelta
x = datetime.date(2021,1,1)

y =timedelta(days=31)
for i in range(1,13):
    x+=y

    print("Month = ",i,",","Date =",x)