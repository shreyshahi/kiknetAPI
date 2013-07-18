import kiknet
from itertools import izip

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

def check_range_returnsData(Mlow,Mhigh):
	range = '%f to %f'%(Mlow,Mhigh)
	data = kiknet.paramInRange('MwFnet',range,['gmNo' , 'MwFnet'])
	assert len(data) > 0

def test_range_returnsData():
	Mlows = [4.0,4.5,5.0,5.5,6.0]
	Mhighs = [4.5 , 5.0 , 5.5 , 6.0 , 7]
	for Mlow,Mhigh in izip(Mlows,Mhighs):
		yield 'check_range_returnsData',Mlow,Mhigh

def check_paramInRange(Mlow,Mhigh):
	range = '%f to %f'%(Mlow,Mhigh)
	data = kiknet.paramInRange('MwFnet',range,['gmNo' , 'MwFnet'])
	Ms_greaterThan = [d['MwFnet'] > Mhigh for d in data]
	Ms_lessThan = [d['MwFnet'] < Mlow for d in data]
	Ms_999 = [d['MwFnet'] == -999 for d in data]
	assert not any(Ms_greaterThan)
	assert not any(Ms_lessThan)
	assert not any(Ms_999)

def test_paramInRange():
	Mlows = [4.0,4.5,5.0,5.5,float('-inf')]
	Mhighs = [4.5 , 5.0 , float('inf') , 6.0 , 7]
	for Mlow,Mhigh in izip(Mlows,Mhighs):
		yield 'check_paramInRange',Mlow,Mhigh

def check_multiParamsInRange_returnsData(Mlow,Mhigh,Rlow,Rhigh):
	ranges = ['%s to %s'%(Mlow,Mhigh) , '%s to %s'%(Rlow,Rhigh)]
	data = kiknet.multiParamsInRange(['MwFnet','RhypFnetMtDepth'],ranges,['gmNo','MwFnet','RhypFnetMtDepth'])
	assert len(data) > 0

def test_multiParamsInRange_returnsData():
	Rlows = ['0','-1','50','200','-inf']
	Rhighs = ['10' , '100' , '100' , 'inf' , '100']
	Mlows = ['0' , '5', '-inf', '6' , '7']
	Mhighs = ['inf' , '6' , '4' ,'7' , '100']
	for Mlow,Mhigh,Rlow,Rhigh in izip(Mlows,Mhighs,Rlows,Rhighs):
		yield 'check_multiParamsInRange_returnsData',Mlow,Mhigh,Rlow,Rhigh

def check_multiParamsInRange(Mlow,Mhigh,Rlow,Rhigh):
	ranges = ['%s to %s'%(Mlow,Mhigh) , '%s to %s'%(Rlow,Rhigh)]
	data = kiknet.multiParamsInRange(['MwFnet','RhypFnetMtDepth'],ranges,['gmNo','MwFnet','RhypFnetMtDepth'])
	Ms_lessThan = [d['MwFnet'] < float(Mlow) for d in data]
	Ms_greaterThan = [d['MwFnet'] > float(Mhigh) for d in data]
	Rs_lessThan = [d['RhypFnetMtDepth'] < float(Rlow) for d in data]
	Rs_greaterThan = [d['RhypFnetMtDepth'] > float(Rhigh) for d in data]
	Ms_999 = [d['MwFnet'] == -999 for d in data]
	Rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
	assert not any(Ms_lessThan)
	assert not any(Ms_greaterThan)
	assert not any(Rs_lessThan)
	assert not any(Rs_greaterThan)
	assert not any(Ms_999)
	assert not any(Rs_999)

def test_multiParamsInRange():
	Rlows = ['0','-1','50','200','-inf']
	Rhighs = ['10' , '100' , '100' , 'inf' , '100']
	Mlows = ['0' , '5', '-inf', '6' , '7']
	Mhighs = ['inf' , '6' , '4' ,'7' , '100']
	for Mlow,Mhigh,Rlow,Rhigh in izip(Mlows,Mhighs,Rlows,Rhighs):
		yield 'check_multiParamsInRange',Mlow,Mhigh,Rlow,Rhigh