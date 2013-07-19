import query

'''

The kiknet API

The python API for the kiknet database exposes these functions.
All functions returns a list of list. Where each individual list contains data for a single ground-motion record.

:copyright: (c) 2013 by Shrey K. Shahi, Haitham Dawood, and Adrian Rodriguez-Marek
:license: MIT, see LICENCE for more details.

TODO : 
1) Add a function to select spectra based on IM
'''

def paramEquals(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter is equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value that *paramName* must equal.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, hypocentral depth, epicentral distance, hypocentral distance, Rrup, Vs30, aftershock flag, and event type for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramEquals('Mw',7.0)
        [{'gmNo':1, 'Mw':7.0, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw == 7.0
        >>> paramEquals('Mw',7.0,['Mw','Repi'])
        [{'Mw':7.0 , 'Repi':10.0}, ... ,{.....}] # Only Mw and Repi for all ground motions with Mw == 7.0
        >>> paramEquals('Mw',7.0,['*'])
        [{'gmNo':1, 'Mw':7.0, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0 ......}, .... , {............}] # All available parameters for all ground motions with Mw == 7.0
        
    '''
    
    return multiParamsInRange([paramName] , ['%f to %f'%(paramValue,paramValue)] , paramsRequested , filterNoisy)

def paramLessThan(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value less than *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value *paramName* should be less than.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramLessThan('Mw',7.0)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw < 7.0
        >>> paramLessThan('Mw',7.0,[],False)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw < 7.0, including low signal to noise ground motions
    '''
    
    return multiParamsInRange([paramName] , ['-inf to %f'%(paramValue - 1e-100)] , paramsRequested , filterNoisy)

def paramLessThanEquals(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value less than or equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value *paramName* should be less than or equal to.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramLessThanEquals('Mw',7.0)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw <= 7.0
        >>> paramLessThanEquals('Mw',7.0,['*'],False)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0, ............}, .... , {............}] # All available parameters for all ground motions with Mw <= 7.0, including low signal to noise ground motions.
    '''
    
    return multiParamsInRange([paramName] , ['-inf to %f'%(paramValue)] , paramsRequested , filterNoisy)

def paramGreaterThan(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value greater than *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value *paramName* should be greater than.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramGreaterThan('Mw',7.0)
        [{'gmNo':1, 'Mw':7.1, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw > 7.0
    '''
    
    return multiParamsInRange([paramName] , ['%f to inf'%(paramValue + 1e-100)] , paramsRequested , filterNoisy)

def paramGreaterThanEquals(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value greater than or equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value *paramName* should be greater than or equal to.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramGreaterThanEquals('Mw',7.0)
        [{'gmNo':1, 'Mw':7.1, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw >= 7.0
    '''
    
    return multiParamsInRange([paramName] , ['%f to inf'%(paramValue)] , paramsRequested , filterNoisy)

def paramInRange(paramName, paramRange, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter takes a value within the range *paramRange*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramRange: A string following the format 'lowerLimit to upperLimit', where lowerLimit and upperLimit are real numbers (or '-inf'/'inf'). The method will only return the data for records where paramName is within the paramRange.
    :type paramRange: str
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramInRange('Mw','6.0 to 7.0')
        [{.....},{.....}] # Info for all ground motions with 6.0 <= Mw <= 7.0
    '''
    
    return multiParamsInRange([paramName] , [paramRange] , paramsRequested , filterNoisy)

def multiParamsInRange(paramNames, paramRanges, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where each parameter in the *paramNames* variable takes a value within the ranges defined by *paramRanges* (i\ :sup:`th` *paramNames* will be within i\ :sup:`th` *paramRanges*). A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramNames: A list of the names of the parameters used to filter the records.
    :type paramNames: list(str)
    :param paramRanges: A list of strings following the format ['lowerLimit1 to upperLimit1' , 'lowerLimit2 to upperLimit2' , ... , 'lowerLimitN to upperLimitN'], where lowerLimits and upperLimits are real numbers or '-inf'/'inf'. 
    :type paramRanges: list(str)
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> multiParamsInRange(['Mw' , 'Repi'],['7.0 to inf' , '0 to 10'])
        [{.....},{.....}] # Info for all ground motions recorded within 10 km of the epicenter and from events with magnitudes greater than 7.0
    '''
    
    return query.multiParamsInRange(paramNames, paramRanges, paramsRequested, filterNoisy)

def spectraForGmNos(gmNos, periods = [] , components = []):
    '''
    Returns the 5% damped linear elastic response spectra for the list of ground motions specified by *gmNo* variable. The spectra is returned in a dictionary which contain the componentName:spectra pairs. componentName can take one of the following values:
        
        #. MS - Geometric mean of the horizontal component.
        #. MB - Geometric mean of the borehole component.
        #. S1 - EW component of the surface record.
        #. S2 - NS component of the surface record.
        #. S3 - Vertical component of the surface record.
        #. B1 - EW component of the borehole record.
        #. B2 - NS component of the borehole record.
        #. B3 - Vertical component of the borehole record.

    The spectra for each component is represent by a list of list. Where each individual list contains the spectral ordinates for each ground motion. The spectral values follow the order of the periods in the *periods* variable. Also the spectra lists follow the order of ground motions in the *gmNo* list.

    :param gmNos: A list of ground-motion numbers for which the spectra is needed.
    :type gmNos: list(int)
    :param periods: A list of periods at which the spectra is computed. The default value is an empty list, this results in spectra being calculated at T = [0.01 , 0.02 , 0.03 , 0.04 , 0.05 , 0.075 , 0.1 , 0.15 , 0.2 , 0.25 , 0.3 , 0.4 , 0.5 , 0.6 , 0.75 , 1 , 1.5 , 2 , 3 , 4 , 5 , 6 , 7.5 , 10] . A list with -1 as first element returns the spectra at all 105 available periods.
    :type periods: list(float)
    :param components: A list of components for which the spectra is needed. The user select any combination of S1, S2, S3, B1, B2, B3. The meaning of these names are described in the list above. The default value of this parameter is an empty list, which returns the sqrt(EW * NS) of the surface motion.
    :type components: list(str)

    Usage:
        >>> spectraForGmNos([1,5])
        {'S1':[[ ... the EW surface spectra for gmNo 1 ...],[ ... the EW surface spectra for gmNo 5 ...]] , 'S2':[[ ... the NS surface spectra for gmNo 1 ...],[ ... the NS surface spectra for gmNo 5 ...]]}
    '''
    
    return query.spectraForGmNos(gmNos,periods,components)
