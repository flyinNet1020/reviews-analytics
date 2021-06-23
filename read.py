# 讀取留言檔，算出留言筆數(長度)，並印出第0筆留言。

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
#		count += 1
#		if count % 1000 == 0: # %用來求餘數，即若count能被1000整除的話，if就成立。
#			print(len(data))
#print('檔案讀取完畢，總共有', len(data), '筆資料')

# 算出每筆留言的平均長度
# 算出所有留言字元/len

summary = 0
for d in data:
	summary += len(d)
print('平均每筆留言的長度為', summary/len(data))