import dash_html_components as html
from utils import Header

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # overview
        ],
    )
