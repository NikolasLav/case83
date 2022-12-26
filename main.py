import requests
from pprint import pprint
from datetime import date, timedelta

search_date = date.today() - timedelta(days=1) #искомая дата - 2 календарных дня (сегодня и вчера)
print("Проверяем записи за прошедшие 2 дня, начиная с", search_date)
# Формируем комбинированную ссылку согласно API начиная с искомой даты. Можно без отдельной переменной, но мне кажется, что так изящнее.
link = 'https://api.stackexchange.com/2.3/questions?fromdate=' + str(
    search_date
) + '%2000:00:00&order=desc&sort=activity&tagged=python&site=stackoverflow'
json_response = requests.get(link, params=b'postId=1')
pprint(json_response.json())