import os
import logging
from logging.handlers import SMTPHandler
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'opcha'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# MAIL_SERVER = os.environ.get('MAIL_SERVER')
	# MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	# MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	# ADMIN = ['admin@example.com']
	# if not app.debug:
	# 	if app.config['MAIL_SERVER']:
	# 		auth = None
	# 		if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
	# 			auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PORT'])
	# 		secure = None
	# 		if app.config['MAIL_USE_TLS']:
	# 			secure = ()
	# 		mail_handler = SMTPHandler(
	# 			mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
	# 			fromaddr='no-reply@' + app.config['MAIL_PORT'],
	# 			toaddrs=app.config['ADMINS'], subject='Microblog Failure',
	# 			credentials=auth, secure=secure)
	# 		mail_handler.setLevel(logging.ERROR)
	# 		app.logger.addHandler(mail_handler)