class Solution:
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        #day on 1-1-1971 : Friday
        ref_dict = {0:"Friday", 1: "Saturday",2:"Sunday",3 : "Monday",4 : "Tuesday",5 : "Wednesday", 6 : "Thursday"}
        month_offset = [3,0,3,2,3,2,3,3,2,3,2,3]
        lc = 0
        for i in range (1971,year+1):
            if i % 4 == 0 and i%100 != 0 : lc += 1
            if i % 4 ==0 and i%100 == 0 and i%400 == 0: lc += 1
        
        
        
        if ((year%4 == 0 and year % 100!= 0) or (year%4==0 and year%100 == 0 and year%400 ==0)) and ((month <2) or (day <30 and month == 2)):
            lc -=1
        
        day_count = day - 1 + sum(month_offset[:month-1]) + (year - 1971) + lc
        
        return (ref_dict [day_count%7])
        