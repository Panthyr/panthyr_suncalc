===============================
Panthyr Suncalc example code
===============================

Example code:

.. code:: python

    >>> from datetime import datetime as dt
    >>> from panthyr_suncalc import p_suncalc as ps

    >>> t = dt.utcnow()

    >>> ps.get_sun_zenith(51,3,t)
    -20.6
    >>> ps.get_sun_azimuth(51,3,t)
    284.94