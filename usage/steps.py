import dash
import dash_html_components as html
from dash.dependencies import Input, Output

import extra_dash_ui_components as ex


app = dash.Dash(__name__)
steps_items = [
    {
        'label': 'Personal',
    },
    {
        'label': 'Seat',
    },
    {
        'label': 'Payment',
    },
    {
        'label': 'Confirmation',
    },
]

panel_items = [
    {
        'label': 'File',
        'icon': 'pi pi-fw pi-file',
        'items': [
            {
                'label': 'New',
                'icon': 'pi pi-fw pi-plus',
                'items': [
                    {
                        'label': 'Bookmark',
                        'icon': 'pi pi-fw pi-bookmark',
                    },
                    {
                        'label': 'Video',
                        'icon': 'pi pi-fw pi-video',
                    },
                ],
            },
            {
                'label': 'Delete',
                'icon': 'pi pi-fw pi-trash',
            },
            {
                'label': 'Export',
                'icon': 'pi pi-fw pi-external-link',
            },
        ],
    },
    {
        'label': 'Edit',
        'icon': 'pi pi-fw pi-pencil',
        'items': [
            {
                'label': 'Left',
                'icon': 'pi pi-fw pi-align-left',
            },
            {
                'label': 'Right',
                'icon': 'pi pi-fw pi-align-right',
            },
            {
                'label': 'Center',
                'icon': 'pi pi-fw pi-align-center',
            },
            {
                'label': 'Justify',
                'icon': 'pi pi-fw pi-align-justify',
            },
        ],
    },
    {
        'label': 'Users',
        'icon': 'pi pi-fw pi-user',
        'items': [
            {
                'label': 'New',
                'icon': 'pi pi-fw pi-user-plus',
            },
            {
                'label': 'Delete',
                'icon': 'pi pi-fw pi-user-minus',
            },
            {
                'label': 'Search',
                'icon': 'pi pi-fw pi-users',
                'items': [
                    {
                        'label': 'Filter',
                        'icon': 'pi pi-fw pi-filter',
                        'items': [
                            {
                                'label': 'Print',
                                'icon': 'pi pi-fw pi-print',
                            },
                        ],
                    },
                    {
                        'icon': 'pi pi-fw pi-bars',
                        'label': 'List',
                    },
                ],
            },
        ],
    },
    {
        'label': 'Events',
        'icon': 'pi pi-fw pi-calendar',
        'items': [
            {
                'label': 'Edit',
                'icon': 'pi pi-fw pi-pencil',
                'items': [
                    {
                        'label': 'Save',
                        'icon': 'pi pi-fw pi-calendar-plus',
                    },
                    {
                        'label': 'Delete',
                        'icon': 'pi pi-fw pi-calendar-minus',
                    },
                ],
            },
            {
                'label': 'Archieve',
                'icon': 'pi pi-fw pi-calendar-times',
                'items': [
                    {
                        'label': 'Remove',
                        'icon': 'pi pi-fw pi-calendar-minus',
                    },
                ],
            },
        ],
    },
]


app.layout = html.Div(children=[
    html.H4('Steps'),
    ex.StepsComponent(
        id='steps',
        model=steps_items,
        readOnly=False,
        # activeIndex=0,
        # style={},
        # className='',
    ),
    html.Div(id='steps-output'),

    html.H4('Panel Menu'),
    ex.PanelMenuComponent(
        id='panelmenu',
        model=panel_items,
        # style={},
        # className='',
    ),
    html.Div(id='panelmenu-output'),
    html.Div(id='panelmenu-output1'),


]
)


@app.callback(Output('steps-output', 'children'), [Input('steps', 'activeIndex')])
def steps_output(current_index):
    return 'Current Index: {}'.format(current_index)


@app.callback(Output('panelmenu-output', 'children'), [Input('panelmenu', 'menuitem')])
def panelmenu_out(current_menu):
    return f"Current Menu: {current_menu}"


@app.callback(Output('panelmenu-output1', 'children'), [Input('panelmenu', 'submenu')])
def panelmenu_out1(current_submenu):
    return f"Current SubMenu: {current_submenu}"


if __name__ == '__main__':
    app.run_server(debug=True)
