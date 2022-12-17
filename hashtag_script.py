import json

new_string = ""
hashtags = []
result = []
tweet_id = []
mapped_hashtags = []

with open("tweet.json", "r", encoding='utf-8') as file:
    jsonData = json.load(file)
for i in jsonData:
    for j in i['text'].split():
        if j.startswith('#'):
            hashtags.append(j)
            tweet_id.append(i['twitter_id'])
print(hashtags)

for i in hashtags:
    new_string = i.strip('#')
    new_string = new_string.strip(',.!?:;')
    result.append(new_string)

mapped_hashtags = [(tweet_id[i], result[i]) for i in range(0, len(tweet_id))]
print(mapped_hashtags)
print(tweet_id)
