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