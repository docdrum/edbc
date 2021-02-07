#!/usr/bin/env python
"""
Copyright (C) 2021  DocDrum


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
