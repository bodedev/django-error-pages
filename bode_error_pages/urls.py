# -*- coding: utf-8 -*-


from website.error_views import Error404View, Error403View, Error500View

handler403 = Error403View.as_view()
handler404 = Error404View.as_view()
handler500 = Error500View.as_view()
