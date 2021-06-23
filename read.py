data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %用來求餘數，即若count能被1000整除的話，if就成立。
			print(len(data))
print(len(data))
print(data[0])