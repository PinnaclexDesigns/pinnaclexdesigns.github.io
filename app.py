from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the holiday data from the CSV file
holiday_data = pd.read_csv('holidays.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the user's preferences from the HTML form
    category = request.form['category']
    location = request.form['location']
    max_price = float(request.form['max_price'])

    # Filter the holiday data based on the user's preferences
    filtered_data = holiday_data[(holiday_data['Category'] == category) & 
                                 (holiday_data['Location'] == location) &
                                 (holiday_data['Price Per Night'] <= max_price)]

    # Sort the filtered data by star rating and temperature rating
    sorted_data = filtered_data.sort_values(by=['Star Rating', 'Temperature Rating'], ascending=False)

    # Convert the sorted data to a list of dictionaries for use in HTML template
    hotels = sorted_data.to_dict('records')

    return render_template('recommend.html', hotels=hotels)

if __name__ == '__main__':
    app.run()
