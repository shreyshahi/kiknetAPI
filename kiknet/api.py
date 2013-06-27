'''

The kiknet API

The python API for the kiknet database exposes these functions.
All functions returns a list of list. Where each individual list contains data for a single ground-motion record.

:copyright: (c) 2013 by Shrey K. Shahi, Haitham Dawood, and Adrian Rodriguez-Marek
:license: MIT, see LICENCE for more details.

'''

def paramEquals(paramName, paramValue, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter takes the value *paramValue*. A :func:`time.time` :py:mod:`list` of :py:mod:`dict` is returned by the function, where each :py:class:`dict` contains the parameter names and values for each ground-motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The method will only return the data for records where paramName == paramValue
    :type paramValue: float
    :param paramsRequested: A comma separated list of parameters that the function will return for each ground motion. The default value of this parameter ( empty string) returns .... for each ground motion. The string '*' can be used to request all available metadata.
    :type paramsRequested: str
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: boolean

    Usage:
        >>> paramEquals('Mw',7.0)
        [{.....},{.....}]
        >>> paramEquals('Mw',7.0,'Mw,Repi')
        [{.....},{.....}]
    '''

    return []
