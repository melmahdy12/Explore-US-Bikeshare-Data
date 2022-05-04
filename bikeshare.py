import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Enter A City(chicago, new york city, washington):').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Please enter a valid city name: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter A Month(all, january, february, march, april, may, june):').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input ("Please enter a valid month: ").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter A Day(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday):').lower()
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input ("Please enter a valid day: ").lower()

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
    # Loads data for the specified city into DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert columns of Start Time and End Time into date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month from Start Time into new column called month
    df['month'] = df['Start Time'].dt.month
    # Extract day from Start Time into new column called day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # Extract hour from Start Time into new column called hour to use this column when calculating most common start hour 
    df['start hour'] = df['Start Time'].dt.hour
    
    """Convert month name to integer"""
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        """Filter by month"""
        df = df[df['month'] == month]
    
    if day != 'all':
        """Filter by day of week"""
        df = df[df['day_of_week'] == day.title()]
    
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {} ".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day is: {} ".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is: {} ".format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(df ['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most common end station is: {} ".format(df ['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df ['Start Station']+","+df ['End Station'] 
    print("The most common route is: {} ".format(df ['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum().round() / 3600.0
    print("total travel time in hours is: ", total_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean().round() / 3600.0
    print("mean travel time in hours is: ", mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_YOB = int(df['Birth Year'].min())
        most_recent_YOB = int(df['Birth Year'].max())
        most_common_YOB = int(df['Birth Year'].mode()[0])
        print('The earliest YOB is: ',earliest_YOB)
        print('The most recent YOB is: ',most_recent_YOB)
        print('The most common YOB is: ',most_common_YOB)
    else:
        print('No Avaiable Data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """shows 5 rows of raw data at a time."""
    print("Would you like to see 5 rows of raw data?(yes or no)")
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))
        print("Would you like to see another 5 rows of raw data?(yes or no)")

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
