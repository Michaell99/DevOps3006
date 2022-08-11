import requests
from selenium import webdriver
import names

my_driver = webdriver.Chrome(executable_path="c:/Users/User/Desktop/chromedriver.exe")
my_driver2 = webdriver.Chrome(executable_path="c:/Users/User/Desktop/chromedriver.exe")

# my_driver3 = webdriver.Chrome()
# my_driver3.get("https://www.ycombinator.com/")
# title = my_driver3.title
# print(title)

repos = requests.get("https://api.github.com/users/avielb/repos")
count = 0
for repo in repos.json():
    if repo != '' and repo.count() > 6:
        print("true")




# my_names = []
# for i in range(3):
#     if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
#         my_names.append(i)
#         print(my_names)
#
# unis = requests.get("http://universities.hipolabs.com/search?country=Israel"), my_driver.get("https://www.ycombinator.com/"), my_driver2.get("https://hub.docker.com")
# assert my_driver.title == "Y Combinator"
# assert my_driver2.title == "Docker Hub Container Image Library |App Containerization"
# assert len(repos.json()) > 5
# assert len(my_names) == 0
# assert len(unis.json()) > 5