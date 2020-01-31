import bpy

class FirstOperator(bpy.types.Operator):
    bl_label = "First Operator"
    bl_idname = "myaddon.first_operator"
    bl_description = "A demo operator"

    def execute(self, context):
        print("hello world 1aaabbba")

        return {"FINISHED"}
        
class SecondOperator(bpy.types.Operator):
    bl_label = "Second Operator"
    bl_idname = "myaddon.second_operator"
    bl_description = "A demo operator"

    def execute(self, context):
        print("hello world")

        return {"FINISHED"}