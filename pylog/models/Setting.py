from pylog import db
from config import Config


class Setting(db.Model):
    __tablename__ = 'setting'
    key = db.Column(db.VARCHAR(36), unique=True, index=True)
    value = db.Column(db.TEXT())

    def __init__(self, **kwargs):
        super(Setting, self).__init__(**kwargs)

    @staticmethod
    def init_setting():

        pass
