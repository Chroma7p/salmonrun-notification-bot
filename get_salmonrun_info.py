import requests
import json

def get_salmonrun_schedule():

    header={"user-agent":"salmonrun-notification-bot/0.1(https://github.com/Chroma7p/salmonrun-notification-bot, Twitter @Chroma7p)"}
    p1="coop-grouping"#salmonrun
    p2="schedule"     #schedule
    res=requests.get(f"https://spla3.yuu26.com/api/{p1}/{p2}",headers=header)
    print(res.status_code)
    if res.status_code == 200:
        print(res.text)
        result=json.loads(res.text)
        return result["results"]
    return {"fail":True}

