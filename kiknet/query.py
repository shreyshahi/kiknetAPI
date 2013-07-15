import sqlite3

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
		with f as open('allParams.txt'):
			for line in f:
				params.append(line.strip())
		return ','.join(params)

	return ','.join(paramsRequested)

def multiParamsInRange(paramNames, paramRanges, paramsRequested, filterNoisy):
	conn = sqlite3.connect('./kiknet_flatfile.db')
	c = conn.cursor()

	requestedParams = getParamsRequested(paramsRequested)

	conditions = []
	for i , paramName in enumerate(paramNames):
		rangeText = paramRanges[i]
		rangeText = rangeText.split('to')
		ranges = [float(rangeText[0].strip()) , float(rangeText[1].strip())]
		queryText = '(%s BETWEEN %f AND %f)'%(paramName , ranges[0] , ranges[1])
		conditions.append(queryText)

	if filterNoisy:
		conditions.append('(gmStatus4Components == 1)')

	allConditions = ' AND '.join(conditions)

	queryText = 'SELECT ' + requestedParams + ' FROM tableName WHERE ' + allConditions
	c.execute(queryText)
	data = c.fetchAll()
	return processData(data , requestedParams)