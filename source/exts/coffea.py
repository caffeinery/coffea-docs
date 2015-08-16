from sphinx.locale import l_, _
from sphinx.domains.javascript import JSObject, JSCallable
from docutils import nodes
from docutils.parsers.rst import directives

class EventDirective(JSObject):
    def get_index_text(self, objectname, name_obj):
        name, obj = name_obj
        return _('%s (coffea event)') % name

class FunctionDirective(JSCallable):
    def add_target_and_index(self, name_obj, sig, signode):
        if not name_obj[1]:
            name, obj = name_obj
        else:
            name = name_obj
        if self.objtype is None:
            obj = ''
        else:
            obj = self.objtype

        targetname = obj + '-' + name
        indextext = self.get_index_text(obj, name)
        self.indexnode['entries'].append(('single', indextext,
                                          targetname, ''))
    def get_index_text(self, objectname, name_obj):
        if not name_obj[1]:
            name, obj = name_obj
        else:
            name = name_obj
            obj = False
        if not obj:
            return _('%s() (coffea function)') % name
        return _('%s() (%s method)') % (name, obj)

def setup(app):
    app.add_directive('coffeaevent', EventDirective)
    app.add_directive('coffeafunction', FunctionDirective)
    return {'version': '1.0'}
