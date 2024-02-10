import requests

API_KEY = "487d5e31a2d60fcb21bd53e4f55c31f6"

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__=="__main__":
    get_data(place="Kosice", forecast_days=1)

