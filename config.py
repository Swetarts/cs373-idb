# ---------------------------
# cs373-idb/config.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

class Config(object):
	DEBUG = False
	TESTING = False
    

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://swetard-reader:password123@104.239.165.88:5432/swetards'

class DevelopmentConfig(Config):
	# FOR THE LOVE OF GOD PLEASE DON'T PUSH CHANGES WITH THE PASSWORD. WE DON'T NEED THIS ON THE REPO
	SQLALCHEMY_DATABASE_URI = 'postgresql://swetard-modifier:EU?wQMHeZpDgX7LYi9@104.239.165.88:5432/swetards'
	DEBUG = True
	TESTING = True