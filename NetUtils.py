# -*- coding: utf-8 -*-
import Params
import requests,sys
from Params import px, pxP, pxB, pxG, pxY, pxR, pxBLD, pxUND
def checknet(url='http://archlinux.org/', timeout=500):
    px('İnternet bağlantısı kontrol ediliyor...')
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        pxG('İnternet bağlantısı var.')

        return True
    except requests.HTTPError as e:
        pxY("Bağlantı hatası! Hata kodu: {0}.".format + (e.response.status_code))
    except requests.ConnectionError:
        pxR("İnternet bağlantısı yok.")
    return False

