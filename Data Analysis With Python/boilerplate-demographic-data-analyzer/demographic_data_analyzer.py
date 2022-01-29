import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'Data Analysis With Python\boilerplate-demographic-data-analyzer\adult.data.csv')# print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race']  # index out the race column # print("race",race)
    race_count_dict = {}  # create a blank dict
    for i in range(0, len(race)):  # check for every race value from the race column
        # race at ith row print(race[i])
        if race[i] in race_count_dict:
            race_count_dict[race[i]] = race_count_dict[race[i]] + 1
        else:
            race_count_dict[race[i]] = 1
    race_count = pd.DataFrame(race_count_dict.items(), columns=['race',''])  # print("race_count_dict",race_count_dict)# print("race_count",race_count)
    race_count=race_count.set_index(keys='race')
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round((((df[(df['sex'] == 'Male')])['age']).mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[(df['education'] == 'Bachelors')]) / len(df) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round(((len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')]) /len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]))*100), 1)
    lower_education_rich = round(((len(df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')]) /len(df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))]))*100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    rich_percentage = (len(df[(df['salary']=='>50K') & (df['hours-per-week']==min_work_hours)])/len(df[(df['hours-per-week']==min_work_hours)]))*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_percentage = 0
    highest_earning_country = ''
    highest_earning_country_arr = pd.DataFrame(df[(df['salary'] == '>50K')]['native-country'].value_counts())
    for index, row in highest_earning_country_arr.iterrows():
        if (len(df[(df['native-country'] == index) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == index)]) * 100) > highest_earning_country_percentage:
            highest_earning_country = index
            highest_earning_country_percentage = round(len(df[(df['native-country'] == index) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == index)]) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (((df[(df['native-country'] == 'India') & (df['salary'] == '>50K')])['occupation']).mode())[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
