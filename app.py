import pandas as pd
import random

# Load the holiday data from the CSV file
holiday_data = pd.read_csv('holidays.csv')

# Define a function to return a random hotel from the filtered data
def get_random_hotel(filtered_data):
    return filtered_data.iloc[random.randint(0, len(filtered_data)-1)]

# Define a function to filter the holiday data based on user input
def filter_data(category, location, max_price):
    filtered_data = holiday_data[(holiday_data['Category'] == category) & 
                                 (holiday_data['Location'] == location) &
                                 (holiday_data['Price Per Night'] <= max_price)]
    return filtered_data

# Define a function to handle user input and return a recommended holiday location
def get_recommendation(user_input):
    if 'lazy' in user_input.lower() or 'relaxing' in user_input.lower():
        category = 'Lazy'
    else:
        category = 'Active'

    if 'europe' in user_input.lower():
        location = 'Europe'
    elif 'asia' in user_input.lower():
        location = 'Asia'
    elif 'north america' in user_input.lower():
        location = 'North America'
    elif 'south america' in user_input.lower():
        location = 'South America'
    elif 'africa' in user_input.lower():
        location = 'Africa'
    elif 'australia' in user_input.lower():
        location = 'Australia'
    else:
        return "Sorry, I'm not sure which continent you're interested in. Please try again."

    try:
        max_price = float(user_input.split('$')[1])
    except:
        max_price = 100

    filtered_data = filter_data(category, location, max_price)

    if len(filtered_data) == 0:
        return "Sorry, I couldn't find any holiday locations that match your preferences. Please try again with different preferences."

    recommended_hotel = get_random_hotel(filtered_data)
    return f"I recommend {recommended_hotel['Hotel Name']} in {recommended_hotel['City']}, {recommended_hotel['Country']}. It has a {recommended_hotel['Star Rating']} star rating and a {recommended_hotel['Temperature Rating']} temperature rating. The price per night is {recommended_hotel['Price Per Night']}."

# Start the chatbot
print("Welcome to the holiday location recommender chatbot! Please enter your questions below. To exit, type 'quit'.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break

    response = get_recommendation(user_input)
    print("Chatbot:", response)
