SECRET_KEY = 'sehr-sicher'
SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite'

SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = b'\x00BZ\xe3\x1a\xbb\xe0\xad\xbbm\xd3\xd3\x91\x1f\xea\x8d\xc7\x82\x81\xe7n\xfdJ`\x88h\x15:\xa8\x12+ '
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_POST_LOGIN_VIEW = '/malen'
SECURITY_POST_REGISTER_VIEW = '/malen'

SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'


