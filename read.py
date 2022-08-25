# coding=UTF-8
data = []
count = 0 #計數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # if count/1000 remainder is 0
			print(len(data)) #print when read every 1000 data

print(len(data)) #print how many reviews
print(data[0]) #print first review
print('---------------------------------')
print(data[1])