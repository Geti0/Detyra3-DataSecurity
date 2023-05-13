def index(x):
	msb = x >> 5  # most significant bit - biti me peshen me te madhe
	lsb = x & 1  # least significant bit - biti me peshen me te vogel
	row = (msb << 1) ^ lsb  # dy bitat e jashtem te x-it
	col = (x >> 1) & 0xf  # kater bitat e brendshem te x-it
	return row * 16 + col  # indeksi i listes
