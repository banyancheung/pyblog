import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/blog'

    SECRET_KEY = '{SECRET_KEY}'
    WTF_CSRF_SECRET_KEY = '{CSRF_SECRET_KEY}'  # for csrf protection
    """Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', if you use the
    bootstrap extension to create a form, it is Ok to use 'SECRET_KEY',
    but when you use tha style like '{{ form.name.label }}:{{ form.name() }}',
    you must do this for yourself to use the wtf, more about this, you can
    take a reference to the book <<Flask Framework Cookbook>>.
    But the book only have the version of English."""

    DEFAULT_BLOG_SETTING = {
        'ARTICLES_PER_PAGE': 10,
        'COMMENTS_PER_PAGE': 6,
        'BLOG_NAME': 'PyLog - yet an other pylog',
        '': ''
    }


