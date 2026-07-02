import requests

base_url = "https://www.fruityvice.com/api/fruit/"

response = requests.get(base_url + "raspberry")
least_favorite = response.json()
#print(least_favorite['nutritions']['protein'])

response = requests.get(base_url + "all")
all_fruits = response.json()
sugar_content = {}
for fruit in all_fruits:
    sugar_content.update({fruit['name']: fruit['nutritions']['sugar']})
highest_sugar_content = max(sugar_content, key=sugar_content.get)
print(highest_sugar_content)