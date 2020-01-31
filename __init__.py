bl_info = {
    "name": "MyAddon",
    "description": "A demo addo n",
    "author": "myname",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "wiki_url": "my github url here",
    "tracker_url": "my github url here/issues",
    "category": "Animation"
}

import bpy
import importlib

# When main is already in local, we know this is not the initial import...
if "main" in locals():    
    importlib.reload(main)    
    
from . import main

main.FirstOperator.doprint()

classes =   (
    main.FirstOperator,
    main.SecondOperator
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)    
        
if __name__ == "__main__":
    register()