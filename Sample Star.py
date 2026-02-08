import bpy
import mathutils
import os
import typing


def _4_way_mirror_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize 4 Way Mirror node group"""
    _4_way_mirror_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="4 Way Mirror")

    _4_way_mirror_1.color_tag = 'NONE'
    _4_way_mirror_1.description = "4-way mirror"
    _4_way_mirror_1.default_group_node_width = 140
    _4_way_mirror_1.show_modifier_manage_panel = True

    # _4_way_mirror_1 interface

    # Socket Mirrored Curve
    mirrored_curve_socket = _4_way_mirror_1.interface.new_socket(name="Mirrored Curve", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    mirrored_curve_socket.attribute_domain = 'POINT'
    mirrored_curve_socket.default_input = 'VALUE'
    mirrored_curve_socket.structure_type = 'AUTO'

    # Socket Base Curve
    base_curve_socket = _4_way_mirror_1.interface.new_socket(name="Base Curve", in_out='INPUT', socket_type='NodeSocketGeometry')
    base_curve_socket.attribute_domain = 'POINT'
    base_curve_socket.description = "Geometry to transform"
    base_curve_socket.default_input = 'VALUE'
    base_curve_socket.structure_type = 'AUTO'

    # Initialize _4_way_mirror_1 nodes

    # Node Group Output
    group_output = _4_way_mirror_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = _4_way_mirror_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Join Geometry.002
    join_geometry_002 = _4_way_mirror_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # Node Transform Geometry
    transform_geometry = _4_way_mirror_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.hide = True
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 3.1415927410125732)
    # Scale
    transform_geometry.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry.003
    join_geometry_003 = _4_way_mirror_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    # Node Transform Geometry.001
    transform_geometry_001 = _4_way_mirror_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.hide = True
    # Mode
    transform_geometry_001.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[3].default_value = (0.0, 0.0, 1.5707963705062866)
    # Scale
    transform_geometry_001.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Set locations
    _4_way_mirror_1.nodes["Group Output"].location = (292.815185546875, 0.0)
    _4_way_mirror_1.nodes["Group Input"].location = (-302.8150634765625, 0.0)
    _4_way_mirror_1.nodes["Join Geometry.002"].location = (99.0548095703125, -24.214248657226562)
    _4_way_mirror_1.nodes["Transform Geometry"].location = (-102.8150634765625, 25.172088623046875)
    _4_way_mirror_1.nodes["Join Geometry.003"].location = (-100.1497802734375, -27.291046142578125)
    _4_way_mirror_1.nodes["Transform Geometry.001"].location = (102.815185546875, 27.291046142578125)

    # Set dimensions
    _4_way_mirror_1.nodes["Group Output"].width  = 140.0
    _4_way_mirror_1.nodes["Group Output"].height = 100.0

    _4_way_mirror_1.nodes["Group Input"].width  = 140.0
    _4_way_mirror_1.nodes["Group Input"].height = 100.0

    _4_way_mirror_1.nodes["Join Geometry.002"].width  = 140.0
    _4_way_mirror_1.nodes["Join Geometry.002"].height = 100.0

    _4_way_mirror_1.nodes["Transform Geometry"].width  = 140.0
    _4_way_mirror_1.nodes["Transform Geometry"].height = 100.0

    _4_way_mirror_1.nodes["Join Geometry.003"].width  = 140.0
    _4_way_mirror_1.nodes["Join Geometry.003"].height = 100.0

    _4_way_mirror_1.nodes["Transform Geometry.001"].width  = 140.0
    _4_way_mirror_1.nodes["Transform Geometry.001"].height = 100.0


    # Initialize _4_way_mirror_1 links

    # join_geometry_003.Geometry -> transform_geometry_001.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Join Geometry.003"].outputs[0],
        _4_way_mirror_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # join_geometry_003.Geometry -> join_geometry_002.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Join Geometry.003"].outputs[0],
        _4_way_mirror_1.nodes["Join Geometry.002"].inputs[0]
    )
    # group_input.Base Curve -> transform_geometry.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Group Input"].outputs[0],
        _4_way_mirror_1.nodes["Transform Geometry"].inputs[0]
    )
    # group_input.Base Curve -> join_geometry_003.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Group Input"].outputs[0],
        _4_way_mirror_1.nodes["Join Geometry.003"].inputs[0]
    )
    # join_geometry_002.Geometry -> group_output.Mirrored Curve
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Join Geometry.002"].outputs[0],
        _4_way_mirror_1.nodes["Group Output"].inputs[0]
    )
    # transform_geometry.Geometry -> join_geometry_003.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Transform Geometry"].outputs[0],
        _4_way_mirror_1.nodes["Join Geometry.003"].inputs[0]
    )
    # transform_geometry_001.Geometry -> join_geometry_002.Geometry
    _4_way_mirror_1.links.new(
        _4_way_mirror_1.nodes["Transform Geometry.001"].outputs[0],
        _4_way_mirror_1.nodes["Join Geometry.002"].inputs[0]
    )

    return _4_way_mirror_1


def nodegroup_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize NodeGroup node group"""
    nodegroup_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="NodeGroup")

    nodegroup_1.color_tag = 'NONE'
    nodegroup_1.description = ""
    nodegroup_1.default_group_node_width = 140
    nodegroup_1.show_modifier_manage_panel = True

    # nodegroup_1 interface

    # Socket Geometry
    geometry_socket = nodegroup_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Initialize nodegroup_1 nodes

    # Node Group Output
    group_output = nodegroup_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_output.inputs[1].hide = True

    # Node Curve Line.002
    curve_line_002 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_002.name = "Curve Line.002"
    curve_line_002.mode = 'POINTS'
    curve_line_002.inputs[1].hide = True
    curve_line_002.inputs[2].hide = True
    curve_line_002.inputs[3].hide = True
    # End
    curve_line_002.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Curve Line.006
    curve_line_006 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_006.name = "Curve Line.006"
    curve_line_006.mode = 'POINTS'
    curve_line_006.inputs[1].hide = True
    curve_line_006.inputs[2].hide = True
    curve_line_006.inputs[3].hide = True
    # End
    curve_line_006.inputs[1].default_value = (1.0, 0.0, 0.0)

    # Node Curve Line.007
    curve_line_007 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_007.name = "Curve Line.007"
    curve_line_007.mode = 'POINTS'
    curve_line_007.inputs[1].hide = True
    curve_line_007.inputs[2].hide = True
    curve_line_007.inputs[3].hide = True
    # End
    curve_line_007.inputs[1].default_value = (1.0, 1.0, 0.0)

    # Node Curve Line.003
    curve_line_003 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_003.name = "Curve Line.003"
    curve_line_003.mode = 'POINTS'
    curve_line_003.inputs[1].hide = True
    curve_line_003.inputs[2].hide = True
    curve_line_003.inputs[3].hide = True
    # End
    curve_line_003.inputs[1].default_value = (1.0, 1.0, 0.0)

    # Node Curve Line.008
    curve_line_008 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_008.name = "Curve Line.008"
    curve_line_008.mode = 'POINTS'
    curve_line_008.inputs[1].hide = True
    curve_line_008.inputs[2].hide = True
    curve_line_008.inputs[3].hide = True
    # End
    curve_line_008.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Curve Line.009
    curve_line_009 = nodegroup_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_009.name = "Curve Line.009"
    curve_line_009.mode = 'POINTS'
    curve_line_009.inputs[1].hide = True
    curve_line_009.inputs[2].hide = True
    curve_line_009.inputs[3].hide = True
    # End
    curve_line_009.inputs[1].default_value = (0.0, 1.0, 0.0)

    # Node Join Geometry.002
    join_geometry_002 = nodegroup_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # Node Math.013
    math_013 = nodegroup_1.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'DIVIDE'
    math_013.use_clamp = False
    math_013.inputs[0].hide = True
    math_013.inputs[1].hide = True
    math_013.inputs[2].hide = True
    # Value
    math_013.inputs[0].default_value = 0.800000011920929
    # Value_001
    math_013.inputs[1].default_value = 3.0

    # Node Combine XYZ.006
    combine_xyz_006 = nodegroup_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[2].hide = True
    # Z
    combine_xyz_006.inputs[2].default_value = 0.0

    # Node Math.014
    math_014 = nodegroup_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'DIVIDE'
    math_014.use_clamp = False
    math_014.inputs[0].hide = True
    math_014.inputs[1].hide = True
    math_014.inputs[2].hide = True
    # Value
    math_014.inputs[0].default_value = 2.0
    # Value_001
    math_014.inputs[1].default_value = 3.0

    # Node Combine XYZ.007
    combine_xyz_007 = nodegroup_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.inputs[2].hide = True
    # Z
    combine_xyz_007.inputs[2].default_value = 0.0

    # Set locations
    nodegroup_1.nodes["Group Output"].location = (186.1131591796875, 367.1404724121094)
    nodegroup_1.nodes["Curve Line.002"].location = (-243.8868408203125, -14.359527587890625)
    nodegroup_1.nodes["Curve Line.006"].location = (-243.8868408203125, 289.6404724121094)
    nodegroup_1.nodes["Curve Line.007"].location = (-243.8868408203125, 137.64047241210938)
    nodegroup_1.nodes["Curve Line.003"].location = (-243.8868408203125, 441.6404724121094)
    nodegroup_1.nodes["Curve Line.008"].location = (-243.8868408203125, 593.6405029296875)
    nodegroup_1.nodes["Curve Line.009"].location = (-243.8868408203125, 745.6405029296875)
    nodegroup_1.nodes["Join Geometry.002"].location = (-3.8868408203125, 367.1404724121094)
    nodegroup_1.nodes["Math.013"].location = (-673.8868408203125, 137.64047241210938)
    nodegroup_1.nodes["Combine XYZ.006"].location = (-458.8868408203125, 593.6405029296875)
    nodegroup_1.nodes["Math.014"].location = (-673.8868408203125, 593.6405029296875)
    nodegroup_1.nodes["Combine XYZ.007"].location = (-458.8868408203125, 137.64047241210938)

    # Set dimensions
    nodegroup_1.nodes["Group Output"].width  = 140.0
    nodegroup_1.nodes["Group Output"].height = 100.0

    nodegroup_1.nodes["Curve Line.002"].width  = 140.0
    nodegroup_1.nodes["Curve Line.002"].height = 100.0

    nodegroup_1.nodes["Curve Line.006"].width  = 140.0
    nodegroup_1.nodes["Curve Line.006"].height = 100.0

    nodegroup_1.nodes["Curve Line.007"].width  = 140.0
    nodegroup_1.nodes["Curve Line.007"].height = 100.0

    nodegroup_1.nodes["Curve Line.003"].width  = 140.0
    nodegroup_1.nodes["Curve Line.003"].height = 100.0

    nodegroup_1.nodes["Curve Line.008"].width  = 140.0
    nodegroup_1.nodes["Curve Line.008"].height = 100.0

    nodegroup_1.nodes["Curve Line.009"].width  = 140.0
    nodegroup_1.nodes["Curve Line.009"].height = 100.0

    nodegroup_1.nodes["Join Geometry.002"].width  = 140.0
    nodegroup_1.nodes["Join Geometry.002"].height = 100.0

    nodegroup_1.nodes["Math.013"].width  = 140.0
    nodegroup_1.nodes["Math.013"].height = 100.0

    nodegroup_1.nodes["Combine XYZ.006"].width  = 140.0
    nodegroup_1.nodes["Combine XYZ.006"].height = 100.0

    nodegroup_1.nodes["Math.014"].width  = 140.0
    nodegroup_1.nodes["Math.014"].height = 100.0

    nodegroup_1.nodes["Combine XYZ.007"].width  = 140.0
    nodegroup_1.nodes["Combine XYZ.007"].height = 100.0


    # Initialize nodegroup_1 links

    # math_013.Value -> combine_xyz_006.X
    nodegroup_1.links.new(
        nodegroup_1.nodes["Math.013"].outputs[0],
        nodegroup_1.nodes["Combine XYZ.006"].inputs[0]
    )
    # math_014.Value -> combine_xyz_006.Y
    nodegroup_1.links.new(
        nodegroup_1.nodes["Math.014"].outputs[0],
        nodegroup_1.nodes["Combine XYZ.006"].inputs[1]
    )
    # curve_line_002.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.002"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )
    # combine_xyz_006.Vector -> curve_line_008.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.006"].outputs[0],
        nodegroup_1.nodes["Curve Line.008"].inputs[0]
    )
    # combine_xyz_006.Vector -> curve_line_009.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.006"].outputs[0],
        nodegroup_1.nodes["Curve Line.009"].inputs[0]
    )
    # combine_xyz_006.Vector -> curve_line_003.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.006"].outputs[0],
        nodegroup_1.nodes["Curve Line.003"].inputs[0]
    )
    # math_013.Value -> combine_xyz_007.Y
    nodegroup_1.links.new(
        nodegroup_1.nodes["Math.013"].outputs[0],
        nodegroup_1.nodes["Combine XYZ.007"].inputs[1]
    )
    # math_014.Value -> combine_xyz_007.X
    nodegroup_1.links.new(
        nodegroup_1.nodes["Math.014"].outputs[0],
        nodegroup_1.nodes["Combine XYZ.007"].inputs[0]
    )
    # combine_xyz_007.Vector -> curve_line_006.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.007"].outputs[0],
        nodegroup_1.nodes["Curve Line.006"].inputs[0]
    )
    # combine_xyz_007.Vector -> curve_line_007.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.007"].outputs[0],
        nodegroup_1.nodes["Curve Line.007"].inputs[0]
    )
    # combine_xyz_007.Vector -> curve_line_002.Start
    nodegroup_1.links.new(
        nodegroup_1.nodes["Combine XYZ.007"].outputs[0],
        nodegroup_1.nodes["Curve Line.002"].inputs[0]
    )
    # join_geometry_002.Geometry -> group_output.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Join Geometry.002"].outputs[0],
        nodegroup_1.nodes["Group Output"].inputs[0]
    )
    # curve_line_007.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.007"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )
    # curve_line_006.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.006"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )
    # curve_line_003.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.003"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )
    # curve_line_008.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.008"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )
    # curve_line_009.Curve -> join_geometry_002.Geometry
    nodegroup_1.links.new(
        nodegroup_1.nodes["Curve Line.009"].outputs[0],
        nodegroup_1.nodes["Join Geometry.002"].inputs[0]
    )

    return nodegroup_1


def kakuasa_no_ha_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Kakuasa-no-ha node group"""
    kakuasa_no_ha_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Kakuasa-no-ha")

    kakuasa_no_ha_1.color_tag = 'NONE'
    kakuasa_no_ha_1.description = ""
    kakuasa_no_ha_1.default_group_node_width = 140
    kakuasa_no_ha_1.show_modifier_manage_panel = True

    # kakuasa_no_ha_1 interface

    # Socket Geometry
    geometry_socket = kakuasa_no_ha_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Initialize kakuasa_no_ha_1 nodes

    # Node Group Output
    group_output = kakuasa_no_ha_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Curve Line.003
    curve_line_003 = kakuasa_no_ha_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_003.name = "Curve Line.003"
    curve_line_003.mode = 'POINTS'
    curve_line_003.inputs[0].hide = True
    curve_line_003.inputs[1].hide = True
    curve_line_003.inputs[2].hide = True
    curve_line_003.inputs[3].hide = True
    # Start
    curve_line_003.inputs[0].default_value = (0.10000000149011612, 0.0, 0.0)
    # End
    curve_line_003.inputs[1].default_value = (-0.10000000149011612, 0.0, 0.0)

    # Node Join Geometry.002
    join_geometry_002 = kakuasa_no_ha_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # Node Math
    math = kakuasa_no_ha_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SQRT'
    math.use_clamp = False
    math.inputs[0].hide = True
    math.inputs[1].hide = True
    math.inputs[2].hide = True
    # Value
    math.inputs[0].default_value = 2.000000476837158

    # Node Transform Geometry
    transform_geometry = kakuasa_no_ha_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[4].hide = True
    transform_geometry.inputs[5].hide = True
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.7853981852531433)
    # Scale
    transform_geometry.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Mesh Circle
    mesh_circle = kakuasa_no_ha_1.nodes.new("GeometryNodeMeshCircle")
    mesh_circle.name = "Mesh Circle"
    mesh_circle.fill_type = 'NONE'
    mesh_circle.inputs[0].hide = True
    # Vertices
    mesh_circle.inputs[0].default_value = 4

    # Node Mesh to Curve
    mesh_to_curve = kakuasa_no_ha_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'
    mesh_to_curve.inputs[1].hide = True
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # Node Curve Line.002
    curve_line_002 = kakuasa_no_ha_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_002.name = "Curve Line.002"
    curve_line_002.mode = 'POINTS'
    curve_line_002.inputs[0].hide = True
    curve_line_002.inputs[1].hide = True
    curve_line_002.inputs[2].hide = True
    curve_line_002.inputs[3].hide = True
    # Start
    curve_line_002.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_002.inputs[1].default_value = (1.0, 1.0, 0.0)

    # Node Curve Line.007
    curve_line_007 = kakuasa_no_ha_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_007.name = "Curve Line.007"
    curve_line_007.mode = 'POINTS'
    curve_line_007.inputs[0].hide = True
    curve_line_007.inputs[1].hide = True
    curve_line_007.inputs[2].hide = True
    curve_line_007.inputs[3].hide = True
    # Start
    curve_line_007.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_007.inputs[1].default_value = (1.0, 0.0, 0.0)

    # Node 4WayMirror.004
    _4waymirror_004 = kakuasa_no_ha_1.nodes.new("GeometryNodeGroup")
    _4waymirror_004.name = "4WayMirror.004"
    _4waymirror_004.node_tree = bpy.data.node_groups[node_tree_names[_4_way_mirror_1_node_group]]

    # Node InnerSpokes
    innerspokes = kakuasa_no_ha_1.nodes.new("GeometryNodeGroup")
    innerspokes.label = "Inner Spokes"
    innerspokes.name = "InnerSpokes"
    innerspokes.node_tree = bpy.data.node_groups[node_tree_names[nodegroup_1_node_group]]

    # Node 4WayMirror.005
    _4waymirror_005 = kakuasa_no_ha_1.nodes.new("GeometryNodeGroup")
    _4waymirror_005.name = "4WayMirror.005"
    _4waymirror_005.node_tree = bpy.data.node_groups[node_tree_names[_4_way_mirror_1_node_group]]

    # Node Curve Line.008
    curve_line_008 = kakuasa_no_ha_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_008.name = "Curve Line.008"
    curve_line_008.mode = 'POINTS'
    curve_line_008.inputs[0].hide = True
    curve_line_008.inputs[1].hide = True
    curve_line_008.inputs[2].hide = True
    curve_line_008.inputs[3].hide = True
    # Start
    curve_line_008.inputs[0].default_value = (0.05000000074505806, 0.0, 0.0)
    # End
    curve_line_008.inputs[1].default_value = (-0.05000000074505806, 0.0, 0.0)

    # Node Join Geometry
    join_geometry = kakuasa_no_ha_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Extrude Mesh.004
    extrude_mesh_004 = kakuasa_no_ha_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_004.name = "Extrude Mesh.004"
    extrude_mesh_004.mode = 'FACES'
    extrude_mesh_004.inputs[1].hide = True
    extrude_mesh_004.inputs[2].hide = True
    extrude_mesh_004.inputs[3].hide = True
    extrude_mesh_004.inputs[4].hide = True
    extrude_mesh_004.outputs[1].hide = True
    extrude_mesh_004.outputs[2].hide = True
    # Selection
    extrude_mesh_004.inputs[1].default_value = True
    # Offset
    extrude_mesh_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset Scale
    extrude_mesh_004.inputs[3].default_value = 0.5
    # Individual
    extrude_mesh_004.inputs[4].default_value = True

    # Node Join Geometry.007
    join_geometry_007 = kakuasa_no_ha_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_007.name = "Join Geometry.007"

    # Node Mesh Boolean.004
    mesh_boolean_004 = kakuasa_no_ha_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_004.name = "Mesh Boolean.004"
    mesh_boolean_004.operation = 'UNION'
    mesh_boolean_004.solver = 'EXACT'
    mesh_boolean_004.inputs[0].hide = True
    mesh_boolean_004.inputs[2].hide = True
    mesh_boolean_004.inputs[3].hide = True
    mesh_boolean_004.outputs[1].hide = True
    # Self Intersection
    mesh_boolean_004.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_004.inputs[3].default_value = False

    # Node Flip Faces.004
    flip_faces_004 = kakuasa_no_ha_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces_004.name = "Flip Faces.004"
    flip_faces_004.inputs[1].hide = True
    # Selection
    flip_faces_004.inputs[1].default_value = True

    # Node Merge by Distance.003
    merge_by_distance_003 = kakuasa_no_ha_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_003.name = "Merge by Distance.003"
    merge_by_distance_003.inputs[1].hide = True
    merge_by_distance_003.inputs[2].hide = True
    merge_by_distance_003.inputs[3].hide = True
    # Selection
    merge_by_distance_003.inputs[1].default_value = True
    # Mode
    merge_by_distance_003.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance_003.inputs[3].default_value = 0.0010000000474974513

    # Node Mesh Boolean.005
    mesh_boolean_005 = kakuasa_no_ha_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_005.name = "Mesh Boolean.005"
    mesh_boolean_005.operation = 'UNION'
    mesh_boolean_005.solver = 'EXACT'
    mesh_boolean_005.inputs[0].hide = True
    mesh_boolean_005.inputs[2].hide = True
    mesh_boolean_005.inputs[3].hide = True
    mesh_boolean_005.outputs[1].hide = True
    # Self Intersection
    mesh_boolean_005.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_005.inputs[3].default_value = False

    # Node Join Geometry.001
    join_geometry_001 = kakuasa_no_ha_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # Node Merge by Distance
    merge_by_distance = kakuasa_no_ha_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Compare
    compare = kakuasa_no_ha_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_THAN'
    # B_INT
    compare.inputs[3].default_value = 4

    # Node Face Neighbors
    face_neighbors = kakuasa_no_ha_1.nodes.new("GeometryNodeInputMeshFaceNeighbors")
    face_neighbors.name = "Face Neighbors"

    # Node Delete Geometry
    delete_geometry = kakuasa_no_ha_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'EDGE'
    delete_geometry.mode = 'ALL'

    # Node Curve to Mesh
    curve_to_mesh = kakuasa_no_ha_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Curve to Mesh.001
    curve_to_mesh_001 = kakuasa_no_ha_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    # Scale
    curve_to_mesh_001.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh_001.inputs[3].default_value = False

    # Set locations
    kakuasa_no_ha_1.nodes["Group Output"].location = (143.50439453125, -750.9984741210938)
    kakuasa_no_ha_1.nodes["Curve Line.003"].location = (-46.49560546875, -614.0617065429688)
    kakuasa_no_ha_1.nodes["Join Geometry.002"].location = (-46.49560546875, -516.0617065429688)
    kakuasa_no_ha_1.nodes["Math"].location = (-806.49560546875, -567.0617065429688)
    kakuasa_no_ha_1.nodes["Transform Geometry"].location = (-426.49560546875, -567.0617065429688)
    kakuasa_no_ha_1.nodes["Mesh Circle"].location = (-616.49560546875, -567.0617065429688)
    kakuasa_no_ha_1.nodes["Mesh to Curve"].location = (-236.49560546875, -516.0617065429688)
    kakuasa_no_ha_1.nodes["Curve Line.002"].location = (-2136.49560546875, -906.5505981445312)
    kakuasa_no_ha_1.nodes["Curve Line.007"].location = (-2136.49560546875, -776.5505981445312)
    kakuasa_no_ha_1.nodes["4WayMirror.004"].location = (-1756.49560546875, -793.5436401367188)
    kakuasa_no_ha_1.nodes["InnerSpokes"].location = (-1946.49560546875, -647.5436401367188)
    kakuasa_no_ha_1.nodes["4WayMirror.005"].location = (-1756.49560546875, -647.5436401367188)
    kakuasa_no_ha_1.nodes["Curve Line.008"].location = (-1566.49560546875, -818.5436401367188)
    kakuasa_no_ha_1.nodes["Join Geometry"].location = (-1566.49560546875, -720.5436401367188)
    kakuasa_no_ha_1.nodes["Extrude Mesh.004"].location = (-996.49560546875, -877.8458862304688)
    kakuasa_no_ha_1.nodes["Join Geometry.007"].location = (-806.49560546875, -828.8458862304688)
    kakuasa_no_ha_1.nodes["Mesh Boolean.004"].location = (-426.49560546875, -750.9984741210938)
    kakuasa_no_ha_1.nodes["Flip Faces.004"].location = (-996.49560546875, -779.8458862304688)
    kakuasa_no_ha_1.nodes["Merge by Distance.003"].location = (-616.49560546875, -828.8458862304688)
    kakuasa_no_ha_1.nodes["Mesh Boolean.005"].location = (-46.49560546875, -750.9984741210938)
    kakuasa_no_ha_1.nodes["Join Geometry.001"].location = (-1946.49560546875, -841.5505981445312)
    kakuasa_no_ha_1.nodes["Merge by Distance"].location = (-236.49560546875, -750.9984741210938)
    kakuasa_no_ha_1.nodes["Compare"].location = (-1376.49560546875, -929.0991821289062)
    kakuasa_no_ha_1.nodes["Face Neighbors"].location = (-1566.49560546875, -982.2903442382812)
    kakuasa_no_ha_1.nodes["Delete Geometry"].location = (-1186.49560546875, -828.8458862304688)
    kakuasa_no_ha_1.nodes["Curve to Mesh"].location = (143.50439453125, -528.4352416992188)
    kakuasa_no_ha_1.nodes["Curve to Mesh.001"].location = (-1376.49560546875, -733.3458862304688)

    # Set dimensions
    kakuasa_no_ha_1.nodes["Group Output"].width  = 140.0
    kakuasa_no_ha_1.nodes["Group Output"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve Line.003"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve Line.003"].height = 100.0

    kakuasa_no_ha_1.nodes["Join Geometry.002"].width  = 140.0
    kakuasa_no_ha_1.nodes["Join Geometry.002"].height = 100.0

    kakuasa_no_ha_1.nodes["Math"].width  = 140.0
    kakuasa_no_ha_1.nodes["Math"].height = 100.0

    kakuasa_no_ha_1.nodes["Transform Geometry"].width  = 140.0
    kakuasa_no_ha_1.nodes["Transform Geometry"].height = 100.0

    kakuasa_no_ha_1.nodes["Mesh Circle"].width  = 140.0
    kakuasa_no_ha_1.nodes["Mesh Circle"].height = 100.0

    kakuasa_no_ha_1.nodes["Mesh to Curve"].width  = 140.0
    kakuasa_no_ha_1.nodes["Mesh to Curve"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve Line.002"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve Line.002"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve Line.007"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve Line.007"].height = 100.0

    kakuasa_no_ha_1.nodes["4WayMirror.004"].width  = 140.0
    kakuasa_no_ha_1.nodes["4WayMirror.004"].height = 100.0

    kakuasa_no_ha_1.nodes["InnerSpokes"].width  = 140.0
    kakuasa_no_ha_1.nodes["InnerSpokes"].height = 100.0

    kakuasa_no_ha_1.nodes["4WayMirror.005"].width  = 140.0
    kakuasa_no_ha_1.nodes["4WayMirror.005"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve Line.008"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve Line.008"].height = 100.0

    kakuasa_no_ha_1.nodes["Join Geometry"].width  = 140.0
    kakuasa_no_ha_1.nodes["Join Geometry"].height = 100.0

    kakuasa_no_ha_1.nodes["Extrude Mesh.004"].width  = 140.0
    kakuasa_no_ha_1.nodes["Extrude Mesh.004"].height = 100.0

    kakuasa_no_ha_1.nodes["Join Geometry.007"].width  = 140.0
    kakuasa_no_ha_1.nodes["Join Geometry.007"].height = 100.0

    kakuasa_no_ha_1.nodes["Mesh Boolean.004"].width  = 140.0
    kakuasa_no_ha_1.nodes["Mesh Boolean.004"].height = 100.0

    kakuasa_no_ha_1.nodes["Flip Faces.004"].width  = 140.0
    kakuasa_no_ha_1.nodes["Flip Faces.004"].height = 100.0

    kakuasa_no_ha_1.nodes["Merge by Distance.003"].width  = 140.0
    kakuasa_no_ha_1.nodes["Merge by Distance.003"].height = 100.0

    kakuasa_no_ha_1.nodes["Mesh Boolean.005"].width  = 140.0
    kakuasa_no_ha_1.nodes["Mesh Boolean.005"].height = 100.0

    kakuasa_no_ha_1.nodes["Join Geometry.001"].width  = 140.0
    kakuasa_no_ha_1.nodes["Join Geometry.001"].height = 100.0

    kakuasa_no_ha_1.nodes["Merge by Distance"].width  = 140.0
    kakuasa_no_ha_1.nodes["Merge by Distance"].height = 100.0

    kakuasa_no_ha_1.nodes["Compare"].width  = 140.0
    kakuasa_no_ha_1.nodes["Compare"].height = 100.0

    kakuasa_no_ha_1.nodes["Face Neighbors"].width  = 140.0
    kakuasa_no_ha_1.nodes["Face Neighbors"].height = 100.0

    kakuasa_no_ha_1.nodes["Delete Geometry"].width  = 140.0
    kakuasa_no_ha_1.nodes["Delete Geometry"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve to Mesh"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve to Mesh"].height = 100.0

    kakuasa_no_ha_1.nodes["Curve to Mesh.001"].width  = 140.0
    kakuasa_no_ha_1.nodes["Curve to Mesh.001"].height = 100.0


    # Initialize kakuasa_no_ha_1 links

    # transform_geometry.Geometry -> mesh_to_curve.Mesh
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Transform Geometry"].outputs[0],
        kakuasa_no_ha_1.nodes["Mesh to Curve"].inputs[0]
    )
    # mesh_to_curve.Curve -> join_geometry_002.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Mesh to Curve"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry.002"].inputs[0]
    )
    # math.Value -> mesh_circle.Radius
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Math"].outputs[0],
        kakuasa_no_ha_1.nodes["Mesh Circle"].inputs[1]
    )
    # mesh_circle.Mesh -> transform_geometry.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Mesh Circle"].outputs[0],
        kakuasa_no_ha_1.nodes["Transform Geometry"].inputs[0]
    )
    # innerspokes.Geometry -> _4waymirror_005.Base Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["InnerSpokes"].outputs[0],
        kakuasa_no_ha_1.nodes["4WayMirror.005"].inputs[0]
    )
    # join_geometry_001.Geometry -> _4waymirror_004.Base Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Join Geometry.001"].outputs[0],
        kakuasa_no_ha_1.nodes["4WayMirror.004"].inputs[0]
    )
    # join_geometry_007.Geometry -> merge_by_distance_003.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Join Geometry.007"].outputs[0],
        kakuasa_no_ha_1.nodes["Merge by Distance.003"].inputs[0]
    )
    # extrude_mesh_004.Mesh -> join_geometry_007.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Extrude Mesh.004"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry.007"].inputs[0]
    )
    # merge_by_distance_003.Geometry -> mesh_boolean_004.Mesh
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Merge by Distance.003"].outputs[0],
        kakuasa_no_ha_1.nodes["Mesh Boolean.004"].inputs[1]
    )
    # _4waymirror_004.Mirrored Curve -> join_geometry.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["4WayMirror.004"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry"].inputs[0]
    )
    # mesh_boolean_005.Mesh -> group_output.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Mesh Boolean.005"].outputs[0],
        kakuasa_no_ha_1.nodes["Group Output"].inputs[0]
    )
    # curve_line_002.Curve -> join_geometry_001.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Curve Line.002"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry.001"].inputs[0]
    )
    # delete_geometry.Geometry -> flip_faces_004.Mesh
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Delete Geometry"].outputs[0],
        kakuasa_no_ha_1.nodes["Flip Faces.004"].inputs[0]
    )
    # delete_geometry.Geometry -> extrude_mesh_004.Mesh
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Delete Geometry"].outputs[0],
        kakuasa_no_ha_1.nodes["Extrude Mesh.004"].inputs[0]
    )
    # merge_by_distance.Geometry -> mesh_boolean_005.Mesh
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Merge by Distance"].outputs[0],
        kakuasa_no_ha_1.nodes["Mesh Boolean.005"].inputs[1]
    )
    # mesh_boolean_004.Mesh -> merge_by_distance.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Mesh Boolean.004"].outputs[0],
        kakuasa_no_ha_1.nodes["Merge by Distance"].inputs[0]
    )
    # curve_to_mesh_001.Mesh -> delete_geometry.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Curve to Mesh.001"].outputs[0],
        kakuasa_no_ha_1.nodes["Delete Geometry"].inputs[0]
    )
    # compare.Result -> delete_geometry.Selection
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Compare"].outputs[0],
        kakuasa_no_ha_1.nodes["Delete Geometry"].inputs[1]
    )
    # face_neighbors.Face Count -> compare.A
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Face Neighbors"].outputs[1],
        kakuasa_no_ha_1.nodes["Compare"].inputs[2]
    )
    # join_geometry_002.Geometry -> curve_to_mesh.Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Join Geometry.002"].outputs[0],
        kakuasa_no_ha_1.nodes["Curve to Mesh"].inputs[0]
    )
    # join_geometry.Geometry -> curve_to_mesh_001.Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Join Geometry"].outputs[0],
        kakuasa_no_ha_1.nodes["Curve to Mesh.001"].inputs[0]
    )
    # curve_line_008.Curve -> curve_to_mesh_001.Profile Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Curve Line.008"].outputs[0],
        kakuasa_no_ha_1.nodes["Curve to Mesh.001"].inputs[1]
    )
    # curve_line_003.Curve -> curve_to_mesh.Profile Curve
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Curve Line.003"].outputs[0],
        kakuasa_no_ha_1.nodes["Curve to Mesh"].inputs[1]
    )
    # _4waymirror_005.Mirrored Curve -> join_geometry.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["4WayMirror.005"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry"].inputs[0]
    )
    # flip_faces_004.Mesh -> join_geometry_007.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Flip Faces.004"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry.007"].inputs[0]
    )
    # curve_line_007.Curve -> join_geometry_001.Geometry
    kakuasa_no_ha_1.links.new(
        kakuasa_no_ha_1.nodes["Curve Line.007"].outputs[0],
        kakuasa_no_ha_1.nodes["Join Geometry.001"].inputs[0]
    )

    return kakuasa_no_ha_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    _4_way_mirror = _4_way_mirror_1_node_group(node_tree_names)
    node_tree_names[_4_way_mirror_1_node_group] = _4_way_mirror.name

    nodegroup = nodegroup_1_node_group(node_tree_names)
    node_tree_names[nodegroup_1_node_group] = nodegroup.name

    kakuasa_no_ha = kakuasa_no_ha_1_node_group(node_tree_names)
    node_tree_names[kakuasa_no_ha_1_node_group] = kakuasa_no_ha.name

