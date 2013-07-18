import kiknet

def test_equals_M():
	data = kiknet.paramEquals('MwFnet',4.1,['gmNo' , 'MwFnet' , 'gmStatus4Components'])
	mags = [d['MwFnet'] - 4.1 for d in data]
	assert sum(mags) == 0
	
