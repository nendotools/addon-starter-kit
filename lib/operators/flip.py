from bpy.types import Operator, Context

class VIEW3D_OT_FlipOperator(Operator):
    """Flip the selected object"""
    bl_idname = "object.flip"
    bl_label = "Flip Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context: Context):
        obj = context.object
        # you may see an error when editing an array like this:
        obj.scale[0] *= -1
        # fake_bpy_module defines it as a Tuple, which is immutable
        # technically, it should be changed like this:
        #   obj.scale = [obj.scale[0]*-1, obj.scale[1], obj.scale[2]]
        # however, this is just an error with the package. The uncommented
        # line above works just fine.
        return {'FINISHED'}

    @classmethod
    def poll(cls, context: Context):
        return context.area.type == 'VIEW_3D'
