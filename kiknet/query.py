import sqlite3
import os

def processData(data , requestedParams):
	processedData = []
	requestedParams = requestedParams.split(',')
	processedData = [dict(zip(requestedParams , d)) for d in data]
	return processedData


def getParamsRequested(paramsRequested):
	if len(paramsRequested) == 0:
		return 'gmno , MeFnet , Rrup1simulations , Rrup2simulations , RrupPublishedSource , RhypFnetMtDepth , RepiFnet , MTDepthFnet , eqCategory , Vs30 , foreAfterShockInClusterReasenberg'

	if paramsRequested[0] == "*":
		params = []
		with open('allParams.txt') as f:
			for line in f:
				params.append(line.strip())
		return ','.join(params)

	return ','.join(paramsRequested)

def multiParamsInRange(paramNames, paramRanges, paramsRequested, filterNoisy):
	this_dir, this_filename = os.path.split(__file__)
	dataPath = os.path.join(this_dir,'kiknet_flatfile.db')
	conn = sqlite3.connect(dataPath)
	c = conn.cursor()

	requestedParams = getParamsRequested(paramsRequested)

	conditions = []
	for i , paramName in enumerate(paramNames):
		rangeText = paramRanges[i]
		rangeText = rangeText.split('to')
		ranges = [float(rangeText[0].strip()) , float(rangeText[1].strip())]
		if ranges[0] == float('-inf'):
			queryText = '(%s <= %f) AND (%s != -999)'%(paramName , ranges[1] , paramName)
		elif ranges[1] == float('inf'):
			queryText = '(%s >= %f)'%(paramName , ranges[0])
		else:
			queryText = '(%s BETWEEN %f AND %f)'%(paramName , ranges[0] , ranges[1])
		conditions.append(queryText)

	if filterNoisy:
		conditions.append('(gmStatus4Components == 1)')

	allConditions = ' AND '.join(conditions)

	queryText = 'SELECT ' + requestedParams + ' FROM flatfile WHERE ' + allConditions
	c.execute(queryText)
	data = c.fetchall()
	return processData(data , requestedParams)

def getRequestedPeriods(periods):
	if len(periods) == 0:
		requestedPeriods = ['0.01' , '0.02' , '0.03' , '0.04' , '0.05' , '0.075' , '0.1' , '0.15' , '0.2' , '0.25' , '0.3' , '0.4' , '0.5' , '0.6' , '0.75' , '1' , '1.5' , '2' , '3' , '4' , '5' , '6' , '7.5' , '10']
	elif periods[0] == -1:
		requestedPeriods = ['0.01' , '0.02' , '0.022' , '0.025' , '0.029' , '0.03' , '0.032' , '0.035' , '0.036' , '0.04' , '0.042' , '0.044' , '0.045' , '0.046' , '0.048' , '0.05' , '0.055' , '0.06' , '0.065' , '0.067' , '0.07' , '0.075' , '0.08' , '0.085' , '0.09' , '0.095' , '0.1' , '0.11' , '0.12' , '0.13' , '0.133' , '0.14' , '0.15' , '0.16' , '0.17' , '0.18' , '0.19' , '0.2' , '0.22' , '0.24' , '0.25' , '0.26' , '0.28' , '0.29' , '0.3' , '0.32' , '0.34' , '0.35' , '0.36' , '0.38' , '0.4' , '0.42' , '0.44' , '0.45' , '0.46' , '0.48' , '0.5' , '0.55' , '0.6' , '0.65' , '0.667' , '0.7' , '0.75' , '0.8' , '0.85' , '0.9' , '0.95' , '1.0' , '1.1' , '1.2' , '1.3' , '1.4' , '1.5' , '1.6' , '1.7' , '1.8' , '1.9' , '2.0' , '2.2' , '2.4' , '2.5' , '2.6' , '2.8' , '3.0' , '3.2' , '3.4' , '3.5' , '3.6' , '3.8' , '4.0' , '4.2' , '4.4' , '4.6' , '4.8' , '5.0' , '5.5' , '6.0' , '6.5' , '7.0' , '7.5' , '8.0' , '8.5' , '9.0' , '9.5' , '10.0']
	else:
		requestedPeriods = [str(p) for p in periods]

	requestedPeriods = [p.replace('.','_') for p in requestedPeriods]
	return requestedPeriods

def buildGmNosCondition(gmNos):
	questionMarks = ','.join(['?']*len(gnNos))
	return 'WHERE gmNo IN ' + questionMarks

def buildSpectraForGmNos(gmNos,component,requestedPeriods,whereClause):
	if component == 'MS':
		# Find the EW and NS surface spectra and sort by gmNo 
		spec1 = buildSpectraForGmNos(gmNos,'S1',requestedPeriods,whereClause).sort(key = lambda x: x[0])
		spec2 = buildSpectraForGmNos(gmNos,'S2',requestedPeriods,whereClause).sort(key = lambda x: x[0])
		# return the geometric mean of the two spectra
		return [[ (spec1[i][j] * spec2[i][j])**0.5  for j in xrange(len(spec1[0]))] for i in xrange(len(spec1))]

	if component == 'MB':
		# Find the EW and NS borehole spectra and sort by gmNo 
		spec1 = buildSpectraForGmNos(gmNos,'B1',requestedPeriods,whereClause).sort(key = lambda x: x[0])
		spec2 = buildSpectraForGmNos(gmNos,'B2',requestedPeriods,whereClause).sort(key = lambda x: x[0])
		# return the geometric mean of the two spectra
		return [[ (spec1[i][j] * spec2[i][j])**0.5  for j in xrange(len(spec1[0]))] for i in xrange(len(spec1))]

def spectraForGmNos(gmNos , periods , components):
	this_dir, this_filename = os.path.split(__file__)
	dataPath = os.path.join(this_dir , 'kiknet_spectra.db')
	conn = sqlite3.connect(dataPath)
	c = conn.cursor()

	requestedPeriods = getRequestedPeriods(periods)
	whereClause = buildGmNosCondition(gmNos)

	if len(components) == 0:
		components = ['MS']

	spectra = {}
	for component in components:
		spectra[component] = buildSpectraForGmNos(gmNos,component,requestedPeriods , whereClause)

	return spectra

