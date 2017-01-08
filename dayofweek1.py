#implementation of Zellers Equation to calculate day of week for a given date.
from enum import Enum
class days(Enum):
        Sunday=0
        sunday=7
        Monday=1
        Tuesday=2
        Wednesday=3
        Thursday=4
        Friday=5
        Saturday=6
class months(Enum):
        Jan=1
        Feb=2
        Mar=3
        April=4
        May=5
        Jun=6
        Jul=7
        Aug=8
        Sep=9
        Oct=10
        Nov=11
        Dec=12
def findDayOfWeek(day,month,year):
        if(month.isalpha()):
                month=months[month].value
        K=int(day)
        if(int(month)-2<=0):
                M=int(month)+10
        else:
                M=int(month)-2
        if(M==11 or M==12):
                year=str(int(year)-1)
        C=int(year[0:2])
        D=int(year[2:])
        return (K+int((13*M-1)/5)+D+int(D/4)+int(C/4)-2*C)%7
date=input().strip()
if "/" in date:splitter="/"
elif "-" in date:splitter="-"
else:splitter=","
(day,month,year)=date.split(splitter)
x=findDayOfWeek(day,month,year)
print(days(x).name)
                
        
        
        


