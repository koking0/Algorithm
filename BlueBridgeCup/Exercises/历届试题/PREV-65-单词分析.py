if __name__ == '__main__':
	string = input()
	cnt = [0] * 26
	for ch in string:
		cnt[ord(ch) - ord('a')] += 1
	
	max_idx = cnt.index(max(cnt))
	print(chr(max_idx + ord('a')))
	print(max(cnt))
