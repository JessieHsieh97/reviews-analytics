# coding=UTF-8
data = []
count = 0 #計數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # if count/1000 remainder is 0
			print(len(data)) #print when read every 1000 data

print('Finish reading', len(data), 'data') #print how many reviews

sum_len = 0 #目前的留言總長度
for d in data:
	sum_len = sum_len + len(d) #目前已累積的留言總長度加上下一筆的留言長度
print('The average length of review is', sum_len/len(data)) #需離開for loop才不會每一次加總的平均都算出來


		