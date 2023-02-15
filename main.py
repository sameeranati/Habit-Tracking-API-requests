import requests
from datetime import datetime
USERNAME="sameera"
TOKEN="hbfivuyfiv"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
headers={"X-USER-TOKEN":TOKEN}
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
headers={"X-USER-TOKEN":TOKEN}
today=datetime(year=2022,month=12,day=15)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"5.74"
}


headers={"X-USER-TOKEN":TOKEN}
today=datetime(year=2022,month=12,day=15)
date=today.strftime("%Y%m%d")
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
graphs_config={
    
    "quantity":"9"
}
# response=requests.put(url=update_endpoint,json=graphs_config,headers=headers)
# print(response.text)



headers={"X-USER-TOKEN":TOKEN}
today=datetime(year=2022,month=11,day=1)
date=today.strftime("%Y%m%d")
delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
graphs_config={
    
    "quantity":"9"
}
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)

