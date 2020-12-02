def threesum():
	for i in arr:
		i = int(i)
		if i > 2020:
			continue
		ret = twosum(2020-i)
		if ret != -1:
			print(i,(2020-i-ret),ret)
			
