API documentation
=================

The API exposes two sets of functions to access the metadata, and the spectra for the ground motions in the database. This design naturally follows from the fact that the the spectra, and the rest of metadata are stored in two seperate databases. Further, for common use cases the metadata for a large number of ground motions is extracted first. A smaller subset of recordings is then selcted after examination of the metadata, for which the spectra is extracted. The current design supports this two step workflow as noted at the end of this page. 

.. module:: kiknet

Metadata Interface
------------------
The functions described below allows access to the metadata in the kiknet API.

.. autofunction:: paramEquals

.. note::
    Haitham and Prof. Adrian, I am currently using Mw, Repi, Rjb, Vs30 and Aftershock flag as the default parameters. Let me know if you think I should add or remove from this list. Basically think of some common use cases and what parameters you will need to extract from the database most often.

.. autofunction:: paramLessThan
.. autofunction:: paramLessThanEquals
.. autofunction:: paramGreaterThan
.. autofunction:: paramGreaterThanEquals
.. autofunction:: paramInRange
.. autofunction:: multiParamsInRange

Spectra Interface
------------------
The functions described below allow us to extract the response spectra for particular ground motions. Note that under the current design the metadata and the spectra cannot be queried at the same time.

.. autofunction:: spectraForGmNos

.. note::
    Haitham and Prof. Adrian, please let me know if you think that there may be situations where extracting metadata like magnitude, distance etc., and the response spectra at the same time may be needed. In the current setting if one needs the response spectra for all M > 6.0 and R < 10 recordings. One needs to first call ::

        kiknet.multiParamsInRange(['Mw','Repi'],['6 to 10','0 to 10'],['gmNo'])
    
    This will give the gmNos for such ground motions. This list of gmNos can then be used as input to the spectraForGmNos to extract the spectra. Is there any use case where this will not work ?


