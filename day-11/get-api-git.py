import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls)
complete_details=response.json()

for i in range(len(complete_details)):
   print(complete_details["user"]["login"])


ython rest-api.py 
sunya-ch
ramzeng
carlory
richabanker
sergeychikd
BenTheElder
michaelasp
gnufied
ArangoGutierrez
p0lyn0mial
sats-23
saschagrunert
cpanato
vikasbolla
Karthik-K-N
vikasbolla
vikasbolla
yongruilin
adrianmoisey
aaron-prindle
BenTheElder
lalitc375
stlaz
vikasbolla
aaron-prindle
mortent
lalitc375
nmn3m
cvan20191
oyiz-michael   
                      
