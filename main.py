import fake_db


def main ():
	data = fake_db.load('data.json')
	print(data)
	fake_db.save(data, 'data2.json')

if __name__ == '__main__':
	main()
	