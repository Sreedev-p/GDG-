import requests

url = "http://10.102.216.203/laP3BD6G/" # The unusual path Nikto found
cookies = {'admin': 'true'}

r = requests.get(url, cookies=cookies)
print(f"Status: {r.status_code}")
print(r.text)
