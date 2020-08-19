import dash_html_components as html
from utils import Header

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 2
            # add your UI here, and callbacks go at the bottom of app.py
            # assets and .js go in assets folder
            # csv or images go in data folder
        ],
    )