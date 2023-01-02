from bpy.types import Operator, Context

class VIEW3D_OT_FlipOperator(Operator):
    """Flip the selected object"""
    bl_idname = "object.flip"
    bl_label = "Flip Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context: Context):
        obj = context.object
        obj.scale[0] *= -1
        return {'FINISHED'}

    @classmethod
    def poll(cls, context: Context):
        return context.area.type == 'VIEW_3D'
