# 파일명: main.py
import requests
import pandas as pd

def fetch_data(api_key):
    url = 'http://apis.data.go.kr/B551182/nonPaymentDamtInfoService'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(api_key)
    }
    response = requests.get(url, headers=headers)
    data = response.json() 

    df = pd.DataFrame(data)
    df.to_excel('output.xlsx') 

if __name__ == "__main__":
    import os
    API_KEY = os.environ['UKoA3ATKwDj6VH8EeN%2B1%2F8PipEZvEYrRqim6XNw7Kuk0izhXAuQBdDkKdD5g8Nub6xfpwJk0v2ueY24GhqdZFA%3D%3D']
    fetch_data(API_KEY)