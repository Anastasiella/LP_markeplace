from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "grgdfposi09845dfgdfgd4564KLfj%&^$#LFDKFDSMBk;ldk"

REMEMBER_COOKIE_DURATION = timedelta(days=5)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False