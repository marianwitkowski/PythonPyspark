

# Pobieranie danych z sieci
import requests

with open("test.txt","rb") as fd:
    upload_files = {
        "test.txt" : fd
    }
    url = "https://httpbin.org/post"
    response = requests.post(url, files=upload_files)
    print(response.json())

url = "https://httpbin.org/post"
response = requests.post(url, data={
    "user" : "jkowalski",
    "password" : "qwerty123"
})
print(response.json())


url="http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
response = requests.get(url,timeout=(5,60),allow_redirects=True, verify=False,headers={
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
} )
print(response.status_code)
curr_data = response.json()
rates = curr_data[0].get("rates")
for rate in rates:
    print(f"{rate.get('currency')} \t {rate.get('code')} \t {rate.get('mid')}")