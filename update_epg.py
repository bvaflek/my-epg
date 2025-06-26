import requests

url = "http://epg.one/epg2.xml"
response = requests.get(url)
if response.status_code == 200:
    with open("epg2.xml", "wb") as f:
        f.write(response.content)
    print("EPG обновлён успешно.")
else:
    print(f"Ошибка при загрузке EPG: {response.status_code}")