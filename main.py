def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas")


def get_user_input():

    NUM = input("Enter temperature: ")
    LIST = NUM.split(',')

    print(LIST)
    return(LIST)

def calc_average_temperature(templist):
    sum = 0
    average = 0
    for i in range(len(templist)):
        sum+= int(templist[i])
        average=sum/len(templist)
    print(("The average is: ")+ str(average))

def calc_min_max_temperature(templist):
    Biggest=templist[0]
    Smallest=templist[0]
    for i in range(len(templist)):
        if Biggest < templist[i]:
            Biggest = templist[i]
        if Smallest > templist[i]:
            Smallest = templist[i]
    print(("The max is: ")+ str(Biggest))
    print(("The min is: ")+ str(Smallest))

def calc_median_temperature(templist):
    import statistics
    MEDIAN = statistics.median(templist)
    print(("The Median is: ")+ str(MEDIAN))
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    templist = get_user_input()
    calc_average_temperature(templist)
    calc_min_max_temperature(templist)
    calc_median_temperature(templist)

if __name__ == "__main__":
    main()