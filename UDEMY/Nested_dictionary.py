

#Nesting Dictionary in a dictionary
# travel_log = {
#     "France" :{
#         "Cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany":{
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits":32

#     },
#     "Australia": {
#         "cities_visited": ["Taree", "Wingham", "Tinonee"], "total_vists":34
#     }
# }


#Nesting a dictionary in a list
travel_log = [
    {
    "country":"France",
    "total_visits": 12,
    "cities_visited": ["Paris", "Lille", "Dijon"]

    },
    {
    "country": "Germany",
    "total_visits":32,
    "cities_visited": ["Berlin", "Hamburg", "Stuttgard"]
    },
    {
    "country":"Australia",
    "total_vists":34,
    "cities_visited": ["Taree", "Wingham", "Tinonee"]

    }
]

#Do not change the code below


def add_new_country(country_visited, times_visited, cities_visted):

    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visted
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersberg", "CraiGo"])

print(travel_log)

