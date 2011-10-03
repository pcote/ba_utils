# ba_utils.py (c) 2011 Phil Cote (cotejrp1)
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****
"""
ba_utils.py
A collection of short utilities that have proven useful on a number of
my Blender scripting projects.
"""
import bpy
import re

"""
MODULE SEARCH FUNCTIONS
"""


def fdir( mod, patt ):
    """
    fdir (filtered dir)
    does a filtered search of a module but with pattern filtering for
    the returned listings.
    """
    res = [ x for x in dir( mod ) if re.match( patt, x, re.IGNORECASE ) ]
    return res
    

def nudir( mod ):
    """
    nudir (no underscore dir)
    A dir command that omits everything that starts with an underscore.
    """
    return [ x for x in dir( mod ) if not x.startswith( "_" ) ]


"""
DATA DELETION FUNCTIONS
"""

def clear_scene_obs( scn ):
    """
    Remove all objects from the scene
    """
    for ob in scn.objects:
        scn.objects.unlink( ob )



def clear_data_obs( *submods ):
    """
    Clear out all the objects from the specified bpy.data modules.
    submods - a string list of the modules to have emptied.
    """    
    for submod in submods:
        d_obs = eval( "bpy.data." + submod )
        for ob in d_obs:
            if ob.users == 0:
                d_obs.remove( ob )


"""
MATERIAL FUNCTIONS
"""

def split_mats_by_link( ob ):
    """
    Splits the materials by link type.
    Returns a tuple of separated object and data linked materials
    """    
    mat_filter = lambda link_type : [ mat_slot.material for mat_slot in
                       ob.material_slots if mat_slot.link == link_type ]
    
    return mat_filter( "OBJECT"), mat_filter( "DATA" )


def set_all_mat_levels( ob, mat_level ):
    """
    Sets all materials associated with a given object to the specified
    material link level of either OBJECT or DATA.
    """
    for mat_slot in ob.material_slots:
        mat_slot.link = mat_level
        
