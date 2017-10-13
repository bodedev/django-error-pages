=======================
Bode Django Error Pages
=======================

Objective
===============
This is a simple django app to handle error pages on a Django Project. Obvious, with some Bode flavor.

How to use
===============
You must configure your root urls.py to handle errors.

* In settings.py, add the 'bode_error_pages' to INSTALLED_APPS;

* In your root urls.py file, add:

.. code-block:: python

    from bode_error_pages.views import Error403View, Error404View, Error500View

    handler403 = Error403View.as_view()
    handler404 = Error404View.as_view()
    handler500 = Error500View.as_view()
