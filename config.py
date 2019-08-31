import os


class Config(object):
    '''This class carries all of note_app configuration.'''
    SECRET_KEY = os.environ.get("SECRET_KEY") or "I_am _the_baddest_and_the_toughest" 