import requests
import os
import telegram
from keys import token ,channelID
import json 
import sys
import time
def post_in_tm(num):

	with open('pic','wb') as output:
		output.write(requests.get(posts[num]['content'], allow_redirects=True).content)

	bot = telegram.Bot(token=token)
	bot.send_photo(chat_id=channelID, photo=open('pic', 'rb'), caption=posts[num]['title'] + '\n' + "by\t" + posts[num]['author'] )

def find_current(dict_list):
	for i,d in enumerate(dict_list):
		if d['current'] == True:
			return i
	return 0
	
with open("memes.json", "r") as read_file:
	posts = json.load(read_file)
if len(sys.argv) > 1:
	if sys.argv[1] == 'all':
		for i in range (len(posts)):
			post_in_tm(i)
			time.sleep(5)
	elif sys.argv[1] == 'top':
		for i in range (5):
			post_in_tm(i)
	else:
		n = int(sys.argv[1]) 
		post_in_tm(n)
else:
	pos = find_current(posts)
	post_in_tm(pos)
	posts[pos]['current'] = False
	print(pos)
	print(len(posts))
	if len(posts) == pos:
		posts[0]['current'] = True
	else:
		posts[pos + 1]['current'] = True
	with open("memes.json", "w") as f:
		json.dump(posts, f)

'''
	if os.path.exists('./counter'):
		with open("counter", "r") as f:
			counter = int(f.readline())
			print(counter)
			post_in_tm(counter)
		counter += 1
		if len(posts) == counter:
			counter = 0
			with open("counter", 'w') as f:
				f.write(counter)	
	else:	
		counter = 0
		with open("counter", 'w') as f:
			f.write(counter)'''	


