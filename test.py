from fortnite import *

API_KEY = ""


f = FortniteApi(API_KEY)
r = f.solo('psn','AlexRamiGaming')
print (r)

r = f.duo('pc','TSM_Myth')
print (r)

r = f.lifetime('pc','NinjasHyper')
print (r)

r = f.squad('pc','绝死绝命')
print (r)