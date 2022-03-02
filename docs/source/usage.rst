===============================
Panthyr Suncalc example code
===============================

Example code:

.. code:: python

    >>> from panthyr_flir_ptu_d48e.d48e_connections import PTHeadIPConnection


    >>> p = PTHeadIPConnection(ip = '192.168.100.190')
    >>> h = PTHead(p, has_slipring = False, do_reset = True)

    >>> h.initialize()
    True

    >>> h.send_cmd('PP4002')  # move pan to position 4002
    >>> h.send_query('PP')  # query pan position
    '4002'

    >>> h.show_parameters()  # show voltage and temperature at body and axis
    {'voltage': '13.2', 'temp_head': 25.6, 'temp_pan': 23.9, 'temp_tilt': 26.1}