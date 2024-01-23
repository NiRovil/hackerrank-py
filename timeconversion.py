def timeConversion(s):
    # Write your code here
    hour = s[:2]

    if s[-2::] == "PM":
        nhour = "12"
        if int(hour) != 12: 
            nhour = int(hour)+12
        s = s.replace(s[:2], str(nhour)) + 'PM'
    
    if s[-2::] == "AM":
        nhour = hour
        if int(hour) == 12: 
            nhour = "00"
        s = s.replace(s[:2], str(nhour)) + 'AM'
    
    nhour = s[:-4]
    print(nhour)

s = "12:45:54AM"

timeConversion(s=s)