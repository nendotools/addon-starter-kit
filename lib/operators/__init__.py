from bpy.utils import register_class, unregister_class
from . import VIEW3D_OT_FlipOperator

__cls__ = [
    VIEW3D_OT_FlipOperator,
]

def register():
    for cls in __cls__:
        register_class(cls)

def unregister():
    for cls in reversed(__cls__):
        unregister_class(cls)

