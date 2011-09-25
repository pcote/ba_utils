"""
ba_utils.py
A collection of short utilities that have proven useful on a number of
my Blender scripting projects.
"""
import bpy
import re

"""
MODULE SEARCH LAMBDAS
"""

"""
fdir (filtered dir)
does a filtered search of a module but with pattern filtering for
the returned listings.
"""
fdir = lambda mod, patt : [ x for x in dir( mod ) 
                                if re.match( patt, x, re.IGNORECASE ) ]

"""
nudir (no underscore dir)
A dir command that omits everything that starts with an underscore.
"""
nudir = lambda mod : [ x for x in dir( mod ) if not x.startswith( "_" ) ]


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
    TODO: This might be tweaked to take into account the users attribute.
    """    
    for submod in submods:
        d_obs = eval( "bpy.data." + submod )
        for ob in d_obs:
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
        
