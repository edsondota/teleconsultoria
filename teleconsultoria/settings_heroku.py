from teleconsultoria.settings import *

ALLOWED_HOSTS = ['teleconsultoria.herokuapp.com',]

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'ec2-23-21-111-81.compute-1.amazonaws.com',
        'NAME': 'dcovfsd05b6gfg',
        'USER': 'blguriuehevnth',
        'PASSWORD': 'b1ff315293a2e29222d3d11104ca61cc81f76911b6bc374bf2411237eb043a13',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}