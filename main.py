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
    API_KEY = os.environ['API_KEY']
    fetch_data(API_KEY)