import requests
response = requests.get("https://api.github.com/users/avielb/repos")
my_file = open("assigment4.json", "a")

result = [repo["full_name"] for repo in response.json() if "first" in repo["full_name"]]

print(result)