import kiknet

def check_equals_returnsData(M):
	data = kiknet.paramEquals('MwFnet',M,['gmNo' , 'MwFnet' , 'gmStatus4Components'])
	assert len(data) > 0

def test_equals_returnsData():
	Ms = [4.0,4.5,5.1,5.5,6.1]
	for M in Ms:
		yield 'check_equals_returnsData',M

def check_equals_M(M):
	data = kiknet.paramEquals('MwFnet',M,['gmNo' , 'MwFnet' , 'gmStatus4Components'])
	mags = [ (d['MwFnet'] == M) for d in data]
	mags_999 = [(d['MwFnet'] == -999)]
	assert all(mags)
	assert not any(mags_999)

def test_equals_M():
	Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
	for M in Ms:
		yield 'check_equals_M' , M

def check_noiseFilter(M):
	data = kiknet.paramEquals('MwFnet',M,['gmNo' , 'MwFnet' , 'gmStatus4Components'])
	noiseStatus = [ (d['gmStatus4Components'] == 1) for d in data]
	assert all(noiseStatus)

def test_noiseFilter():
	Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
	for M in Ms:
		yield 'check_noiseFilter',M

def check_noiseyData(M):
	'''Test if we get back any noisy results if we switch the noise filter off'''
	data = kiknet.paramEquals('MwFnet',M,['gmNo' , 'MwFnet' , 'gmStatus4Components'] , False)
	noiseStatus = [ d['gmStatus4Components'] == 0 for d in data]
	assert any(noiseStatus)

def test_noiseyData():
	Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
	for M in Ms:
		yield 'check_noiseyData',M

def check_paramLessThan(R):
	data = kiknet.paramLessThan('RhypFnetMtDepth',R,['gmNo' , 'RhypFnetMtDepth'],False)
	Rs = [(d['RhypFnetMtDepth'] < R) for d in data]
	Rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
	assert all(Rs)
	assert not any(Rs_999)

def test_paramLessThan():
	Rs = [10 , 50 , 100 , 200 , 300]
	for R in Rs:
		yield 'check_paramLessThan',R

def check_paramGreaterThan(R):
	data = kiknet.paramGreaterThan('RhypFnetMtDepth',R,['gmNo' , 'RhypFnetMtDepth'],False)
	Rs = [(d['RhypFnetMtDepth'] > R) for d in data]
	Rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
	assert all(Rs)
	assert not any(Rs_999)

def test_paramGreaterThan():
	Rs = [10 , 50 , 100 , 200 , 300]
	for R in Rs:
		yield 'check_paramGreaterThan',R

def check_paramLessThanEquals(M):
	data = kiknet.paramLessThanEquals('MwFnet',M,['gmNo' , 'MwFnet'],False)
	Ms_lessThan = [(d['MwFnet'] <= M) for d in data]
	Ms_equals = [(d['MwFnet'] == M) for d in data]
	Ms_999 = [d['MwFnet'] == -999 for d in data]
	assert all(Ms_lessThan) 
	assert any(Ms_equals)
	assert not any(Ms_999)

def test_paramLessThanEquals():
	Ms = [4.5 , 5.5 , 5.7 , 6.5 ,7.5]
	for M in Ms:
		yield 'check_paramLessThanEquals',M

def check_paramGreaterThanEquals(M):
	data = kiknet.paramGreaterThanEquals('MwFnet',M,['gmNo' , 'MwFnet'],False)
	Ms_greaterThan = [(d['MwFnet'] >= M) for d in data]
	Ms_equals = [(d['MwFnet'] == M) for d in data]
	Ms_999 = [d['MwFnet'] == -999 for d in data]
	assert all(Ms_greaterThan) 
	assert any(Ms_equals)
	assert not any(Ms_999)

def test_paramGreaterThanEquals():
	Ms = [4.5 , 5.5 , 5.7 , 6.5 ,7.5]
	for M in Ms:
		yield 'check_paramGreaterThanEquals',M