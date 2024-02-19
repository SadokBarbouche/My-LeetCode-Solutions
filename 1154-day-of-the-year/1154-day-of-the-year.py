class Solution:
    def dayOfYear(self, date: str) -> int:
        splitted_date = date.split('-')
        year = int(splitted_date[0])
        month = int(splitted_date[1])
        day = int(splitted_date[2])
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        months_map = {
            1: 31,
            2: 29 if is_leap_year else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }        
        day_of_year = sum(months_map[i] for i in range(1, month)) + day
        return day_of_year
