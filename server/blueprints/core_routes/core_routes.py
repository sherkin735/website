from flask import Blueprint, render_template


bp = Blueprint('core_routes', __name__, template_folder='templates', static_folder='static', static_url_path='/core-static')


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
