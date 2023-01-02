# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "My Addon",
    "description": "My Blender Addon, doing some cool feature",
    "author": "YOU",
    "version": (0, 1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > My Addon",
    "tracker_url": "https://github.com/__UserOrTeam__/__Repository__/issues",
    "category": "3D View",
}

import bpy
from . import lib
from .Settings import ProjectSettings 


def register():
    bpy.utils.register_class(ProjectSettings)
    lib.register()


def unregister():
    lib.unregister()
    bpy.utils.unregister_class(ProjectSettings)
