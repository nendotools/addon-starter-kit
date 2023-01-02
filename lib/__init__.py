from bpy.utils import register_class, unregister_class
from . import operators
from . import ui

__cls__ = [
]

def register():
    operators.register()
    for cls in __cls__:
        register_class(cls)

def unregister():
    operators.unregister()
    for cls in reversed(__cls__):
        unregister_class(cls)
