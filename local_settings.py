SECURE_SSL_REDIRECT = False 

# Time zone settings
TIME_ZONE = 'Asia/Tokyo'
USE_TZ = True 

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'tcms.kiwi_auth.backends.AnonymousViewBackend',
]

ANONYMOUS_USER_PERMISSIONS = (
    'view_testplan',
    'view_testcase',
    'view_testexecution',
    'view_product',
    'view_build',
    'view_environment',
)
