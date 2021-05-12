import json
import os

from blind_watermark import WaterMark
from django.http import HttpResponse
from django.shortcuts import render
import cv2 as cv


def hello(request):
    return HttpResponse("Hello world!!")


def index(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'index.html', context)


def upload(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'upload.html', context)


def savefile(request):
    if request.method == 'POST':
        print(request)
        print(request.FILES)
        file_obj = request.FILES.get('img')
        print(file_obj)
        file_path = os.path.join('static/uploadfiles/', file_obj.name)
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        # return HttpResponse(file_path)

        bwm1 = WaterMark(password_img=1, password_wm=1)
        bwm1.read_img('static/uploadfiles/' + file_obj.name)
        wm = '@zipu888 大神万岁！'
        bwm1.read_wm(wm, mode='str')
        bwm1.embed('static/uploadfiles/bwfiles/' + file_obj.name)
        len_wm = len(bwm1.wm_bit)
        print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
        img = cv.imread('static/uploadfiles/bwfiles/' + file_obj.name)
       # 降噪处理
        dst = cv.fastNlMeansDenoisingColored(img, None, 7, 7, 7, 21)
        cv.imwrite('static/uploadfiles/sfiles/' + file_obj.name, dst, params=None)

        data = {
            'srcImg': '/static/uploadfiles/' + file_obj.name,
            'desImg': '/static/uploadfiles/bwfiles/' + file_obj.name
        }
    return HttpResponse(json.dumps(data), content_type="application/json")
