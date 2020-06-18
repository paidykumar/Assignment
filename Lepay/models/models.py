# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api
import cv2

class opencv_attendance(models.Model):
    # _name = 'opencv_attendance.opencv_attendance'
    _inherit = 'op.attendance.line'

    @api.multi
    def method_webcam_trigger(self):
        img = cv2.imread(
            'C:/Program Files (x86)/Odoo 12.0/server/odoo/addons/opencv_attendance/static/src/img/watch.png',
            cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        super(opencv_attendance, self).method_webcam_trigger()


#         key = cv2.waitKey(1)
#         webcam = cv2.VideoCapture(0)
#         while True:
#             try:
#                 print("4")
#                 check, frame = webcam.read()
#                 print(webcam.isOpened(), check, frame)
#                 if check:
#                     cv2.imshow("Capturing", frame)
#                     print("*********")
#                     key = cv2.waitKey(1)
#                     # if key == ord('s'):
#                     #     print("SAVE IMAGE")
#                     #     cv2.imwrite(filename='product_image', img=frame)
#                     #     img = image.fromarray(frame, 'RGB')
#                     #     img.save('my.png')
#                     #     roiImg = img.crop()
#                     #     imgByteArr = io.BytesIO()
#                     #     roiImg.save(imgByteArr, format='PNG')
#                     #     imgByteArr = imgByteArr.getvalue()
#                     #     image_base64 = base64.b64encode(imgByteArr)
#                     #     cv2.waitKey(1650)
#                     #     cv2.destroyAllWindows()
#                     #     vals = {
#                     #         'image': image_base64,
#                     #     }
#                     #     self.write(vals)
#                     #     break
#                     # elif key == ord('q'):
#                     #     break
#             except(KeyboardInterrupt):
#                 webcam.release()
#                 cv2.destroyAllWindows()
#                 break
#         webcam.release()
#         cv2.destroyAllWindows()