import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    # html.Img(
                    #     src=app.get_asset_url("addYOURLOGOHERE.png"),
                    #     className="logo",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H1("Main Title")],
                        className="seven columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Page 1",
                href="/page1",
                className="tab first",
            ),
            dcc.Link(
                "Page 2",
                href="/page2",
                className="tab",
            ),
            dcc.Link(
                "Page 3",
                href="/page3",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu
