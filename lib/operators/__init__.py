from bpy.utils import register_class, unregister_class
from . import flip 

__cls__ = [
    flip.FlipOperator
]

def register():
    for cls in __cls__:
        register_class(cls)

def unregister():
    for cls in reversed(__cls__):
        unregister_class(cls)

