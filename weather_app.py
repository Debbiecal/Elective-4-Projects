import requests


def get_weather(city):
    # Replace 'your_actual_api_key' with your OpenWeatherMap API key
    api_key = '280e30108fe989a8323776a5dcb5fd2e'

    # Construct the API URL with the city name and your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Send the request to the OpenWeatherMap API
    response = requests.get(url)

    # Parse the response into JSON
    data = response.json()

    # Check if the request was successful (status code 200)
    if data['cod'] == 200:
        # Extract the weather description and temperature
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        # Print the weather details
        print(f'Weather in {city}: {weather}, {temp}°C')
    else:
        # If city not found or any other error
        print(f'City {city} not found.')


# Example usage: Get the weather for Manila
get_weather('Manila')
