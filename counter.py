def countDayOfTheWeek():
    # This first line is provided for yo
    # Initializes the dictionary
    fname = input('Enter a file name: ')
    counter = {}
    
    with open(fname) as file: 
        for line in file: 
            if line.startswith("From "):
                day = return_day(line)

            counter[day] = counter.get(day,0) + 1

    print(counter)



def return_day(line: str) -> str: 
    line = line.strip()
    line_list = line.split()
    day = line_list[2]

    return day 

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
