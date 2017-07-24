import json
import chardet


def json_file_to_python_obj(f):
	with open(f, 'rb') as f:
		data = f.read()
		result = chardet.detect(data)
		s = data.decode(result['encoding'])
	
	python_obj = json.loads(s)
	return python_obj


def print_top_10(f):
	data = json_file_to_python_obj(f)

	items = data["rss"]["channel"]["items"]
	words = []
	for item in items:
		description = item["description"].split()
		title = item["title"].split()
		words.extend(description)
		words.extend(title)
	
	words_freq = [(words.count(word), word) for word in set (words) if len(word) > 6]
	words_freq.sort(reverse = True)
	for word in words_freq[:10]:
		print(word[1])
	print()


def main():
	print('newsit.json')
	print('____________')
	print_top_10('newsit.json')
	
	print('newsafr.json')
	print('____________')
	print_top_10('newsafr.json')
	
	print('newscy.json')
	print('____________')
	print_top_10('newscy.json')
	
	print('newsfr.json')
	print('____________')
	print_top_10('newsfr.json')


main()