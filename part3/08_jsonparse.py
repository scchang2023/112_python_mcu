import json

# jsonData='{"name" : "Anna", "age" : 18, "city": "Taoyuan"}';
# text=json.loads(jsonData)
# for key,value in text.items():
#     print(key,value)
    
# jsonData='{"familys" : [{"name" : "Anna", "age" : 18, "city" : "Taoyuan"},	{"name" : "Don", "age" : 21, "city" : "Tainan"} ] }';
# text=json.loads(jsonData)
# for people in text["familys"]:
#     print(people["name"],people["age"])

menu={ 
    "breakfast": {
        "hours": "7-11",
        "items": {
            "burritos": "$60",
            "pancakes": "$40"
        }
    },
    "lunch" : {
        "hours": "11-3",
        "items": {
            "hamburger": "$50"
        }
    },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$80"
        }
    }
}
# for meal in menu:
#     print(meal,menu[meal]["hours"])
    
# for meal in menu:
#     print(meal,end=":")
#     for item in menu[meal]["items"]:
#         print(item,end="/")
#     print()
    
# for meal in menu:
#     for item in menu[meal]["items"]:
#         print(item,menu[meal]["items"][item])

for meal in menu:
    for item, price in menu[meal]["items"].items():
        print(item,price)