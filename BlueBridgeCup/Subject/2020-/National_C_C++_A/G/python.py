if __name__ == '__main__':
	tian_gan = ["jia", "yi", "bing", "ding", "wu", "ji", "geng", "xin", "ren", "gui"]
	di_zhi = ["zi", "chou", "yin", "mao", "chen", "si", "wu", "wei", "shen", "you", "xu", "hai"]
	start_year = 2020
	tian_gan_index, di_zhi_index = 6, 0
	target_year = int(input())
	diff = target_year - start_year
	tian_gan_index = (tian_gan_index + diff) % len(tian_gan)
	di_zhi_index = (di_zhi_index + diff) % len(di_zhi)
	print(f"{tian_gan[tian_gan_index]}{di_zhi[di_zhi_index]}")
