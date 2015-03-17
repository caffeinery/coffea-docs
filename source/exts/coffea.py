from sphinx.locale import l_, _
from sphinx.domains.javascript import JSObject, JSCallable

class EventDirective(JSObject):
    def get_index_text(self, objectname, name_obj):
        name, obj = name_obj
        return _('%s (coffea event)') % name

class FunctionDirective(JSCallable):
    def get_index_text(self, objectname, name_obj):
        name, obj = name_obj
        if not obj:
            return _('%s() (coffea function)') % name
        return _('%s() (%s method)') % (name, obj)

def setup(app):
    app.add_directive('coffeaevent', EventDirective)
    app.add_directive('coffeafunction', FunctionDirective)
    return {'version': '1.0'}
