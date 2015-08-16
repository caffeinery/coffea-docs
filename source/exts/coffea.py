def setup(app):
    app.add_object_type('coffeaevent', 'cevent', '%s (coffea event)')
    app.add_object_type('coffeafunction', 'cfunction', '%s (coffea function)')
    return {'version': '1.0'}
