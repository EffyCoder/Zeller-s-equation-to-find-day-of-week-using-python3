#implementation of Zellers Equation to calculate day of week for a given date.
Days={0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",5:"Friday", 6:"Saturday"}
months=['NULL','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
#This implementation is a modified to take 1st month to be january and so on.It can one of the forms of date :dd-month-yyyy
#dd-mon-yyyy , dd-mm-yyyy and it can also take input with ',' or '/' as a separator.
def findDayOfWeek(day,month,year):
        if(month[:3].isalpha()):
                mon=month[:3].lower()
                month=months.index(mon)
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
print(Days[x])
                
        
        
        


