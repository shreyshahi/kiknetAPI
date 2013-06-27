API documentation
=================

.. module:: kiknet

Metadata Interface
------------------
The functions described below allows access to the metadata in the kiknet API.

.. autofunction:: paramEquals
.. autofunction:: paramLessThan
.. autofunction:: paramLessThanEquals
.. autofunction:: paramGreaterThan
.. autofunction:: paramGreaterThanEquals
.. autofunction:: paramInRange
.. autofunction:: multiParamsInRange

Spectra Interface
------------------
The functions described below allow us to extract the response spectra for particular ground motions. Note that the metadata and the spectra are stored in separate databases so they cannot be queried at the same time.

.. autofunction:: spectraForGmNos

.. note::
    Haitham and Prof. Adrian, please let me know if you think that there may be situations where extracting metadata like magnitude, distance etc., and the response spectra at the same time may be needed. In the current setting if one needs the response spectra for all M > 6.0 and R < 10 recordings. One needs to first call ::

        kiknet.multiParamsInRange(['Mw','Repi'],['6 to 10','0 to 10'],['gmNo'])
    
    This will give the gmNos for such ground motions. This list of gmNos can then be used as input to the spectraForGmNos to extract the spectra. So this can be accomplished in two steps.


