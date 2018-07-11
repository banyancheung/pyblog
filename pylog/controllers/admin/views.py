from . import admin
from flask_login import login_required


@admin.route('/')
@login_required
def index():
    return 'hello world'
