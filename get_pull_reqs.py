# Program to  fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.


import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)


# method-1
"""
collection = response.json()
names = []
if response.status_code == 200:
    for i in range(len(collection)):
        names.append(collection[i]["user"]["login"])
    print(names)

    print()

    unique_names = list(set(names))
    print(unique_names)
    print()
    for name in unique_names:
        user = name
        count = 0 
        for i_name in names:
            if user == i_name:
                count += 1
        print (user, count)
else:
    print(f"Failed to fetch data , Status code: {response.status_code}")
"""

# method - 2

if response.status_code == 200:
    pull_reqs = response.json()

    pr_creators = {}

    for pull in pull_reqs:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    for creator, count in pr_creators.items():
        print(f"{creator} : {count} PRs")
else:
    print(f"Failed to fetch data , Status code: {response.status_code}")