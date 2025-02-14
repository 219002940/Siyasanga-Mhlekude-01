import calendar

def display_calendar(year, month):
    print(calendar.month(year, month))

def main():
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        if 1 <= month <= 12:
            display_calendar(year, month)
        else:
            print("Invalid month! Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter numeric values for year and month.")

if __name__ == "__main__":
    main()
