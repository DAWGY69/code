import maya.cmds as cmds

def rename_hierarchy(root, prefix, index=1, padding=2):
    """
    Renames objects in the hierarchy based on a desired naming convention.
    
    Args:
        root (str): The root object in the hierarchy.
        prefix (str): The desired prefix for the new names.
        index (int): The starting index for the suffix.
        padding (int): The number of digits for the suffix padding.
    """
    children = cmds.listRelatives(root, allDescendents=True, fullPath=True)
    objects = [root] + children if children else [root]

    for obj in objects:
        # Generate the new name
        suffix = str(index).zfill(padding)
        new_name = f"{prefix}_{suffix}"

        # Rename the object
        cmds.rename(obj, new_name)

        # Increment the index
        index += 1

# Example usage
root_object = cmds.ls(selection=True)[0]  # Get the currently selected root object
rename_hierarchy(root_object, "MyObject", index=1, padding=3)
