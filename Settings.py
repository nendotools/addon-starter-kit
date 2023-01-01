import bpy
from bpy.types import Context
from bpy.props import BoolProperty, CollectionProperty, FloatVectorProperty, EnumProperty, FloatProperty, IntProperty, StringProperty


class OverlaySettings( bpy.types.AddonPreferences ):
  ##
  # Name used to access settings
  ##
  bl_idname = __package__

  ##
  # Settings for the addon
  ##
  is_enabled: BoolProperty( name="Enable Controls", default=True )

  ##
  # Preferences UI for Addon Menu
  ##
  def draw( self, context: Context ):
    pass
