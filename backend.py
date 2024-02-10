import requests

API_KEY = "487d5e31a2d60fcb21bd53e4f55c31f6"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    if kind == "Temperature":
        filtered_data = [i["main"]["temp"] for i in filtered_data]
        return filtered_data
    if kind == "Sky":
        filtered_data = [i['weather'][0]['main'] for i in filtered_data]
        return filtered_data

if __name__=="__main__":
    print(get_data(place="Kosice", forecast_days=1, kind="Temperature"))