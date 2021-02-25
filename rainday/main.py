from twilio.rest import Client

import requests
parameters={"lat":43.615021,
            "lon":-116.202316,
            "appid": "56da2dfd00e1fe5abb9a459b05a8c9cc"


}
account_sid = 'AC955574924c656692d4aec5bc5546e3a8'
auth_token = '44d9e99cc23c833efb6b3d335002b24a'

response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_hourly=response.json()
weather_slice=weather_hourly["hourly"][:12]
rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        rain=True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain...please bring ☂️",
        from_='+13238701056',
        to='+14086502861'
    )

    print(message.status)






