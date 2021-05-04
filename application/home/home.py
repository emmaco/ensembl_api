from flask import Blueprint, render_template

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates'
)


@home_bp.route('/', methods=['GET'])
def home():
    """
    Renders the home page
    :rtype: str
    """
    return render_template('index.html')
