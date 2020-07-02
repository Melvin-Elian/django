SECRET_KEY='u=#gre%c92(v5j&$&cvwd6=0g@t3xjkjz3zeye1y5=ifxjrqi-'

DEBUG =True
ALLOMED_HOSTS=[]

INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]
MIDDLEWARE=[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfviewMiddleware',
    'django.contrib.auth.middleware.Authentication',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF='telusko.url'
TEMPLATES=[
    'BACKEND: django.template.backends.django.DjangoTemplates',
    'OIRS':[os.path.join(BASE_DIR,'templates')],
    'APP_DIRS':True,
    'OPTIONS':{
        'context_processors':[
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',

        ]
    }
]
WSGI_APPLICATION='telusko.wsgi.application'
DATABASES={
    'default':{
        'ENGINE':'django.bd.backends.postgresql',
        'NAME':'telusko',
        'USER':'postgres',
        'PASSWORD':'3456',
        'HOST':'localhost',
    }
}