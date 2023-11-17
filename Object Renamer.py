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
    # Get the list of all descendants of the root object, including the root itself
    children = cmds.listRelatives(root, allDescendents=True, fullPath=True)
    objects = [root] + children if children else [root]

    # Iterate through each object in the hierarchy
    for obj in objects:
        # Generate the new name with the specified prefix and index
        suffix = str(index).zfill(padding)  # Convert the index to a string with zero-padding
        new_name = f"{prefix}_{suffix}"  # Combine the prefix and suffix to create the new name

        # Rename the object using Maya's rename command
        cmds.rename(obj, new_name)

        # Increment the index for the next object
        index += 1

# Example usage
# Get the currently selected root object
root_object = cmds.ls(selection=True)[0]
# Rename the hierarchy starting with the specified prefix, index, and padding
rename_hierarchy(root_object, "MyObject", index=1, padding=3)
