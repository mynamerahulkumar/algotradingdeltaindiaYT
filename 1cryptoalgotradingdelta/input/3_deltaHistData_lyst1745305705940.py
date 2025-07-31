import requests
import pandas as pd
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
TIME_ZONE =  ZoneInfo("Asia/Kolkata")
headers = {
  'Accept': 'application/json'
}
end = int(datetime.now(TIME_ZONE).timestamp())
start = int((datetime.now(TIME_ZONE) -  timedelta(minutes=10)).timestamp())
r = requests.get('https://api.india.delta.exchange/v2/history/candles', params={
  'resolution': '1m',  'symbol': 'MARK:C-BTC-86600-220425',  'start': start,  'end': end
}, headers = headers)

# C-BTC-86600-220425   
# BTCUSD


res= r.json()
candeldata = pd.DataFrame(res['result'])
candeldata["time"] = pd.to_datetime(candeldata["time"], unit="s", utc=True).dt.tz_convert("Asia/Kolkata")
candeldata