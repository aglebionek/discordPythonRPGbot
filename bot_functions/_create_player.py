import json
import urllib.request
#WIP
async def create_player(stats_file, author_id, current_campaign):
    req = urllib.request.Request(f"{stats_file}", headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req)
    data = json.load(data)
    print(data)
    
    with open(f"./campaigns/{current_campaign}.json", encoding='utf-8') as file:
        campaign_data: dict = json.load(file)
        if author_id not in campaign_data:
            campaign_data[author_id] = 