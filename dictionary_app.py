import re
import urllib.request

print('Welcome to online Dictionay App.\nEnter any word to get its definition or enter "q" to quit.')

while True:
	try:
		keyword = input("\nEnter your word: ")
		if keyword == "q":
			break
		
		else:
			url = "http://www.dictionary.com/browse/"
			url = url + keyword
			
			data = urllib.request.urlopen(url).read()
			data1 = data.decode("utf-8")
			
			content = re.search('<meta name="description" content="', data1)
			start = content.end()
			end = start + 500
			content1 = data1[start:end]
			
			content = re.search("definition, ", content1)
			start = content.end()
			content2 = content1[start:]
			
			content = re.search(' See more', content2)
			end = content.start()
			content3 = content2[:end]
			
			print(content3)
				
		
	except NameError:
		print('Sorry, The word "' + keyword + '" does not exist.')

	except:
		print('Sorry, Something went wrong. Please try again.')
