import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from pages import (
    page1,
    page2,
    page3,
    overview
)

server = flask.Flask(__name__)

@server.route('/app')
def index():
    return 'Hello Flask app'

app = dash.Dash(
    __name__,
    server=server,
)

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)
app.config.suppress_callback_exceptions = True

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/page1":
        return page1.create_layout(app)
    elif pathname == "/page2":
        return page2.create_layout(app)
    elif pathname == "/page3":
        return page3.create_layout(app)
    else:
        return overview.create_layout(app)

# all callbacks for pages go here


if __name__ == '__main__':
    app.run_server(debug=False)