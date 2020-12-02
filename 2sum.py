def twosum(total):
	d = collections.defaultdict(int)
	for i in arr:
		i = int(i)

		if d[i] == 1:
			return i
		d[total-i] = 1
	return -1
  
