import time
import pandas as pd
import numpy as np

CITY_LIST = {'Chicago': r'D:\all-project-files\chicago.csv',
              'New york city': r'D:\all-project-files\new_york_city.csv',
              'Washington': r'D:\all-project-files\washington.csv'}
MONTH_LIST = ['all', 'January', 'February', 'March', 'April', 'May', 'June']
DAY_LIST = ['all', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
welcome_message = " Hello! Ready for discovering  The bike_share data !? "
print("_" * 20 + welcome_message + "_" * 20)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = "XXX"
    while city_name.title().strip() not in CITY_LIST:  # to make sure that the entered city name is in city list
        city_name = input("* Type the name of the city you want to start with Chicago, New york city, Washington !")
        if city_name.title().strip() in CITY_LIST:
            city = city_name
        else:
            print("We can not reach the name of the CITY you entered")

            break

    # get user input for month (all, january, february, ... , june)

    month_name = "YYY"
    while month_name.title().strip() not in MONTH_LIST:  # to make sure that the entered month name is in month list
        month_name = input(
            f"* Type the name of the month you want to start with{MONTH_LIST}")
        if month_name.title().strip() in MONTH_LIST:
            print(f"---Just For Make Sure You Choose city ({city_name}), Month ({month_name})---")
            month = month_name
        else:
            print("We can not reach the name of the MONTH you entered")

    # to make user input the  day of week (all, monday, tuesday, ... sunday)
    day_name = "ZZZ"
    while day_name.title().strip() not in DAY_LIST:
        day_name = input(f"* Type the name of the DaY you want to start with  {DAY_LIST}!!")
        if day_name.title().strip() in DAY_LIST:
            print(f"---Just For Make Sure You Choose city =>({city_name}),Month =>({month_name}),Day =>({day_name})---")
            day = day_name
        else:
            print("We can not reach the name of the DAY you entered")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month from the given filtered data is:-{common_month} ")

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print(f"The most common day from the given filtered data is:- {common_day}")

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour from the given filtered data is:- {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_start_hour, common_day, common_month


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station from is:- {common_start_station}: ")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used start station from is:- {common_end_station} ")

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "," + df['End Station']).mode()[0]
    print(f"most frequent combination of start station and end station trip{frequent_combination}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is:{total_travel_time} ")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The Mean of Travel Time is {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bike_share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df["User Type"].value_counts()
    print(f"The count of user type is:- {counts_of_user_types}")

    # TO DO: Display counts of gender
    if city != "Washington":
        counts_of_gender = df["Gender"].value_counts()
        print(f"The count of user type is:- {counts_of_gender}")
    else:
        print("the city you have been entered not have a column named => Gender ")
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print(f"Earliest birth from the given filtered data is: {earliest_birth}")
    print(f"Most recent birth from the given filtered data is: {most_recent_birth}")
    print(f"Most common birth from the given filtered data is: {most_common_birth}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This function allows user to see the first n rows from raw data


def show_row_data():

    while true:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter Yes or No?").title().strip()
        num_of_rows = int(input("Type the number of rows you want to see"))
        if view_data == Yes:
            print(df.head(num_of_rows))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
