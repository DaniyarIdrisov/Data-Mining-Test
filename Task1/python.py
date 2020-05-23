import requests
import time

token = ...  # TOKEN API
version = 5.103
domain = ...  # ID MyVk
activity = 'activity'
genre = "Юмор"  # Тематика
friends_id = requests.get('https://api.vk.com/method/friends.get',
                          params={
                              'access_token': token,
                              'v': version,
                              'user_id': domain
                          })

friends_data = friends_id.json()

list = dict()
array = []
for id in friends_data['response']['items']:
    temp = requests.get('https://api.vk.com/method/groups.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'user_id': id
                        })
    try:
        list[id] = temp.json()['response']['items']
        for g_id in list[id]:
            temp1 = requests.get('https://api.vk.com/method/groups.getById',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'group_id': g_id,
                                     'fields': activity
                                 })
            try:
                if genre == temp1.json()['response'][0]['activity']:
                    array.append(id)
                    print(array)
                    break
            except:
                continue
            time.sleep(0.6)
    except:
        continue

    time.sleep(0.6)

print("id страниц с данной тематикой:")
for i in array:
    print(i);
