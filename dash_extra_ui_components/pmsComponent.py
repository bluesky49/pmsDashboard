# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class pmsComponent(Component):
    """A pmsComponent component.


Keyword arguments:
- value (list; optional)"""
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['value']
        self._type = 'pmsComponent'
        self._namespace = 'dash_extra_ui_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(pmsComponent, self).__init__(**args)
