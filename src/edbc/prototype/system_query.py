import requests

system_bodies_url = "https://www.edsm.net/api-system-v1/bodies"
system_estimated_value_url = "https://www.edsm.net/api-system-v1/estimated-value"

def get_system_bodies(system_name):
    params = dict(
        systemName = system_name
    )
    resp = requests.get(system_bodies_url, params=params)
    data = resp.json()
    return data

def get_system_estimated_value(system_name):
    params = dict(
        systemName = system_name
    )
    resp = requests.get(url=system_estimated_value_url, params=params)
    data = resp.json()
    return data

def print_system_overview(system_name):
    bodies = get_system_bodies(system_name)
    value = get_system_estimated_value(system_name)
    star = bodies["bodies"][0]
    scoopable = star["isScoopable"]
    print(f'System: {bodies["name"]}')
    print(f'Main star: {star["name"]}')
    print(f'Type {star["subType"]} ({"NOT " if not scoopable else ""}scoopable)')
    print(f'Estimated value/mapped: {value["estimatedValue"]} / {value["estimatedValueMapped"]}')
    for i in value["valuableBodies"]:
        print(f'  {i["bodyName"]}: {i["valueMax"]} ({i["distance"]}ls)')

print_system_overview("Sol")
