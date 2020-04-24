import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'april', 'may', 'june']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nWould you like to see data for Chicago, New York City or Washington? \n>').lower()
            if city in cities:
                break
            else:
                print('\nPlease enter a valid city\n')
                continue
        except:
            print('\nPlease enter a valid city\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nWhich month? January, February, March, April, May or June? Type 'all' to apply no month filter. \n>")
            if month.lower() in months or month == 'all':
                break
            else:
                print('\nPlease enter a valid month filter\n')
                continue
        except:
            print('\nPlease enter a valid month filter\n')
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nWhich day would you like to analyze? Or type 'all' to apply no day filter. \n>")
            if day.lower() in days or day == 'all':
                break
            else:
                print('\nPlease enter a valid day filter\n')
                continue
        except:
            print('Please enter a valid day filter')
            continue

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_dow)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip is: {}, {}'.format(frequent_start_end_station[0], frequent_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('Gender count is:\n', gender_count)
        print()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
          earliest_year = df['Birth Year'].min()
          print('Earliest year of birth is: ', earliest_year)
          most_recent_year = df['Birth Year'].max()
          print('Most recent year of birth is: ', most_recent_year)
          most_common_year = df['Birth Year'].mode()[0]
          print('The most common year of birth is: ', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 10
    yes = input("\nWould you like to examine the particular user trip data? Type 'yes' or 'no'\n>")
    if yes.lower() == 'yes':
        raw_data = df.head()
        print(raw_data)
    while True:
        answer = input("\nWould you like to see more? Type 'yes' or 'no'\n")
        if answer.lower() == 'yes':
            raw_dataa = df.head(i)
            i += 5
            print(raw_dataa)
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
