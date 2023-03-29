def countDayOfTheWeek():
    # This first line is provided for yo
    # Initializes the dictionary
    file_name = input("Enter a file name: ")
    day_counter = {}
    
    with open(file_name) as file: 
        for line in file: 
            if line.startswith("From "):
                day = return_day(line)

                day_counter[day] = day_counter.get(day, 0) +1 

    print(day_counter)



def return_day(line: str) -> str: 
    line = line.strip()
    line_list = line.split()
    day = line_list[2]

    return day 

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
