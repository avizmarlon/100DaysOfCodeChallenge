nums = [2, 4, 5, 1, 8, 5, 9, 0, 2, 3, 43, 55, 21, 5, 243, 321, 241]

def mySort(nums_list):
	c1 = 0
	c2 = 0
	for n1 in nums_list:
		for n2 in nums_list:
			if n2 < n1:
				print(nums_list)
				nums_list[c1] = n2
				nums_list[c2] = n1
				print(nums_list)
				#print(c2)
				#print(n2)
			c2 += 1
		c1 += 1
	return nums_list

result = mySort(nums)
print(result)