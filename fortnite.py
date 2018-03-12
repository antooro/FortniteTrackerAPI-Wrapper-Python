import requests

class FortniteApi():
    def __init__(self,API_KEY):
        self.API_KEY = API_KEY
    def squad(self,platform,user):

        r=requests.get("https://api.fortnitetracker.com/v1/profile/"+platform+"/"+user, headers={"TRN-Api-Key": self.API_KEY})
        dic = r.json()

        squad = dic['stats']['p9']
        r = dic['platformNameLong']+" "+dic['epicUserHandle']
        for key, value in squad.items():
            if not ('Top' in squad[key]['label']):
                r += '\n'+squad[key]['label']+' '+squad[key]['displayValue']
            else:
                continue
        return (r)
    def solo(self,platform,user):

        r=requests.get("https://api.fortnitetracker.com/v1/profile/"+platform+"/"+user, headers={"TRN-Api-Key": self.API_KEY})
        dic = r.json()

        solo = dic['stats']['p2']

        r = dic['platformNameLong']+" "+dic['epicUserHandle']
        for key, value in solo.items():
            if not ('Top' in solo[key]['label']):
                r += '\n'+solo[key]['label']+' '+solo[key]['displayValue']
            else:
                continue
        return (r)
    def duo(self,platform,user):

        r=requests.get("https://api.fortnitetracker.com/v1/profile/"+platform+"/"+user, headers={"TRN-Api-Key": self.API_KEY})
        dic = r.json()
        duo = dic['stats']['p10']

        r = dic['platformNameLong']+" "+dic['epicUserHandle']
        for key, value in duo.items():
            if not ('Top' in duo[key]['label']):
                r += '\n'+duo[key]['label']+' '+duo[key]['displayValue']
            else:
                continue
        return (r)
    def lifetime(self,platform,user):
        
        r=requests.get("https://api.fortnitetracker.com/v1/profile/"+platform+"/"+user, headers={"TRN-Api-Key": self.API_KEY})
        dic = r.json()
        lifetime = dic["lifeTimeStats"]
        nuevo = {}
        for i in range (len(lifetime)):
            nuevo[lifetime[i]['key']] = lifetime[i]['value']
        
        r = dic['platformNameLong']+" "+dic['epicUserHandle']
        
        for key, value in nuevo.items():
            if not ('Top' in str(key)):
                r += '\n'+key+' '+value
            else:
                continue
        return (r)
    