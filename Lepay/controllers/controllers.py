# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request


class opencvStudentAttendance(http.Controller):

    @http.route('/student/attendance/main/', website=True, auth='public')
    def index(self, **kw):
        # img = cv2.imread(
        #     'C:/Program Files (x86)/Odoo 12.0/server/odoo/addons/opencv_attendance/static/src/img/watch.png',
        #     cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return "hello"

    @http.route('/student/attendance/facial/', website=True, auth='public')
    def opencv_attendance(self, **kw):
        return http.request.render('opencv_attendance.opencv_template', {})

# @http.route('/o3_library/o3_library/objects/<model("o3_library.o3_library"):obj>/', auth='public')
# def object(self, obj, **kw):
#     return http.request.render('o3_library.object', {
#         'object': obj
#     })
