import bpy
import mathutils
import os
import typing


def sq_criss_cross_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize SQ Criss-Cross.001 node group"""
    sq_criss_cross_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="SQ Criss-Cross.001")

    sq_criss_cross_001_1.color_tag = 'NONE'
    sq_criss_cross_001_1.description = "Basket weave pattern with smooth over/under curves"
    sq_criss_cross_001_1.default_group_node_width = 140
    sq_criss_cross_001_1.show_modifier_manage_panel = True

    # sq_criss_cross_001_1 interface

    # Socket Geometry
    geometry_socket = sq_criss_cross_001_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Weave Height
    weave_height_socket = sq_criss_cross_001_1.interface.new_socket(name="Weave Height", in_out='INPUT', socket_type='NodeSocketFloat')
    weave_height_socket.default_value = 0.10000000149011612
    weave_height_socket.min_value = 0.0
    weave_height_socket.max_value = 1.0
    weave_height_socket.subtype = 'NONE'
    weave_height_socket.attribute_domain = 'POINT'
    weave_height_socket.default_input = 'VALUE'
    weave_height_socket.structure_type = 'AUTO'

    # Initialize sq_criss_cross_001_1 nodes

    # Node Group Input
    group_input = sq_criss_cross_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = sq_criss_cross_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node H1 Seg2
    h1_seg2 = sq_criss_cross_001_1.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    h1_seg2.label = "H1 Seg2"
    h1_seg2.name = "H1 Seg2"
    h1_seg2.mode = 'OFFSET'
    # Resolution
    h1_seg2.inputs[0].default_value = 8
    # Start
    h1_seg2.inputs[1].default_value = (0.0, 0.25, 0.0)
    # Start Handle
    h1_seg2.inputs[2].default_value = (0.0, 0.0, -0.20000000298023224)
    # End Handle
    h1_seg2.inputs[3].default_value = (0.0, 0.0, -0.20000000298023224)
    # End
    h1_seg2.inputs[4].default_value = (0.5, 0.25, 0.0)

    # Node Join Curves
    join_curves = sq_criss_cross_001_1.nodes.new("GeometryNodeJoinGeometry")
    join_curves.label = "Join Curves"
    join_curves.name = "Join Curves"

    # Node Weave Height Doubled
    weave_height_doubled = sq_criss_cross_001_1.nodes.new("ShaderNodeMath")
    weave_height_doubled.label = "Weave Height * 2"
    weave_height_doubled.name = "Weave Height Doubled"
    weave_height_doubled.operation = 'MULTIPLY'
    weave_height_doubled.use_clamp = False
    # Value_001
    weave_height_doubled.inputs[1].default_value = 2.0

    # Node Transform Geometry
    transform_geometry = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Tile Scale.001
    tile_scale_001 = sq_criss_cross_001_1.nodes.new("ShaderNodeCombineXYZ")
    tile_scale_001.label = "Tile Scale"
    tile_scale_001.name = "Tile Scale.001"
    # X
    tile_scale_001.inputs[0].default_value = 1.0
    # Y
    tile_scale_001.inputs[1].default_value = 1.0

    # Node Join Curves.004
    join_curves_004 = sq_criss_cross_001_1.nodes.new("GeometryNodeJoinGeometry")
    join_curves_004.label = "H1"
    join_curves_004.name = "Join Curves.004"

    # Node Join Curves.005
    join_curves_005 = sq_criss_cross_001_1.nodes.new("GeometryNodeJoinGeometry")
    join_curves_005.label = "Join Curves"
    join_curves_005.name = "Join Curves.005"

    # Node Set Material
    set_material = sq_criss_cross_001_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    if "Blue" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["Blue"]

    # Node Join Geometry
    join_geometry = sq_criss_cross_001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Viewer
    viewer = sq_criss_cross_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")

    # Node Transform Geometry.001
    transform_geometry_001 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    transform_geometry_001.inputs[5].hide = True
    # Mode
    transform_geometry_001.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[3].default_value = (0.0, 3.1415927410125732, 0.0)
    # Scale
    transform_geometry_001.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.002
    transform_geometry_002 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.inputs[1].hide = True
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[4].hide = True
    transform_geometry_002.inputs[5].hide = True
    # Mode
    transform_geometry_002.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_002.inputs[3].default_value = (0.0, 0.0, 3.1415927410125732)
    # Scale
    transform_geometry_002.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.003
    transform_geometry_003 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.inputs[1].hide = True
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[4].hide = True
    transform_geometry_003.inputs[5].hide = True
    # Mode
    transform_geometry_003.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_003.inputs[3].default_value = (0.0, 3.1415927410125732, 3.1415927410125732)
    # Scale
    transform_geometry_003.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.004
    transform_geometry_004 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[4].hide = True
    transform_geometry_004.inputs[5].hide = True
    # Mode
    transform_geometry_004.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_004.inputs[3].default_value = (0.0, 0.0, 1.5707963705062866)
    # Scale
    transform_geometry_004.inputs[4].default_value = (-0.9999998807907104, -1.0, 1.0)

    # Node Transform Geometry.005
    transform_geometry_005 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.inputs[1].hide = True
    transform_geometry_005.inputs[2].hide = True
    transform_geometry_005.inputs[3].hide = True
    transform_geometry_005.inputs[4].hide = True
    transform_geometry_005.inputs[5].hide = True
    # Mode
    transform_geometry_005.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_005.inputs[3].default_value = (0.0, 3.1415927410125732, 1.5707963705062866)
    # Scale
    transform_geometry_005.inputs[4].default_value = (-1.0, -1.0, 1.0)

    # Node Transform Geometry.006
    transform_geometry_006 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_006.name = "Transform Geometry.006"
    transform_geometry_006.inputs[1].hide = True
    transform_geometry_006.inputs[2].hide = True
    transform_geometry_006.inputs[3].hide = True
    transform_geometry_006.inputs[4].hide = True
    transform_geometry_006.inputs[5].hide = True
    # Mode
    transform_geometry_006.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_006.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_006.inputs[3].default_value = (3.1415927410125732, 0.0, 1.5707963705062866)
    # Scale
    transform_geometry_006.inputs[4].default_value = (-1.0, -1.0, 1.0)

    # Node Transform Geometry.007
    transform_geometry_007 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_007.name = "Transform Geometry.007"
    transform_geometry_007.inputs[1].hide = True
    transform_geometry_007.inputs[2].hide = True
    transform_geometry_007.inputs[3].hide = True
    transform_geometry_007.inputs[4].hide = True
    transform_geometry_007.inputs[5].hide = True
    # Mode
    transform_geometry_007.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_007.inputs[3].default_value = (3.1415927410125732, 3.1415927410125732, 1.5707963705062866)
    # Scale
    transform_geometry_007.inputs[4].default_value = (-1.0, -1.0, 1.0)

    # Node Reroute
    reroute = sq_criss_cross_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.001
    reroute_001 = sq_criss_cross_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Curve to Mesh
    curve_to_mesh = sq_criss_cross_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Curve Circle
    curve_circle = sq_criss_cross_001_1.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    # Resolution
    curve_circle.inputs[0].default_value = 32
    # Radius
    curve_circle.inputs[4].default_value = 0.20000000298023224

    # Node Quadrilateral
    quadrilateral = sq_criss_cross_001_1.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    quadrilateral.name = "Quadrilateral"
    quadrilateral.mode = 'RECTANGLE'
    # Width
    quadrilateral.inputs[0].default_value = 0.10000000149011612
    # Height
    quadrilateral.inputs[1].default_value = 0.20000000298023224

    # Node Curve to Mesh.002
    curve_to_mesh_002 = sq_criss_cross_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_002.name = "Curve to Mesh.002"
    # Scale
    curve_to_mesh_002.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh_002.inputs[3].default_value = False

    # Node Transform Geometry.008
    transform_geometry_008 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_008.name = "Transform Geometry.008"
    # Mode
    transform_geometry_008.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_008.inputs[2].default_value = (-1.3999998569488525, 0.0, 0.0)
    # Rotation
    transform_geometry_008.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_008.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.009
    transform_geometry_009 = sq_criss_cross_001_1.nodes.new("GeometryNodeTransform")
    transform_geometry_009.name = "Transform Geometry.009"
    # Mode
    transform_geometry_009.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_009.inputs[2].default_value = (1.1999999284744263, 0.0, 0.0)
    # Rotation
    transform_geometry_009.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_009.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Set locations
    sq_criss_cross_001_1.nodes["Group Input"].location = (63.30665969848633, 25.757217407226562)
    sq_criss_cross_001_1.nodes["Group Output"].location = (1854.563232421875, 184.19508361816406)
    sq_criss_cross_001_1.nodes["H1 Seg2"].location = (-622.085205078125, 182.43138122558594)
    sq_criss_cross_001_1.nodes["Join Curves"].location = (443.30670166015625, 242.75721740722656)
    sq_criss_cross_001_1.nodes["Weave Height Doubled"].location = (253.30662536621094, 100.75721740722656)
    sq_criss_cross_001_1.nodes["Transform Geometry"].location = (633.306640625, 277.2572021484375)
    sq_criss_cross_001_1.nodes["Tile Scale.001"].location = (443.30670166015625, 100.75721740722656)
    sq_criss_cross_001_1.nodes["Join Curves.004"].location = (-117.08518981933594, 98.51309204101562)
    sq_criss_cross_001_1.nodes["Join Curves.005"].location = (63.30665969848633, 242.75721740722656)
    sq_criss_cross_001_1.nodes["Set Material"].location = (253.30662536621094, 242.75721740722656)
    sq_criss_cross_001_1.nodes["Join Geometry"].location = (1720.0855712890625, 221.73370361328125)
    sq_criss_cross_001_1.nodes["Viewer"].location = (1854.5640869140625, 306.34942626953125)
    sq_criss_cross_001_1.nodes["Transform Geometry.001"].location = (-369.585205078125, -30.123260498046875)
    sq_criss_cross_001_1.nodes["Transform Geometry.002"].location = (-369.585205078125, 67.87673950195312)
    sq_criss_cross_001_1.nodes["Transform Geometry.003"].location = (-369.585205078125, 263.8767395019531)
    sq_criss_cross_001_1.nodes["Transform Geometry.004"].location = (-369.585205078125, 361.876708984375)
    sq_criss_cross_001_1.nodes["Transform Geometry.005"].location = (-369.585205078125, 459.876708984375)
    sq_criss_cross_001_1.nodes["Transform Geometry.006"].location = (-369.585205078125, -128.123291015625)
    sq_criss_cross_001_1.nodes["Transform Geometry.007"].location = (-369.585205078125, 165.87673950195312)
    sq_criss_cross_001_1.nodes["Reroute"].location = (-369.585205078125, -226.12326049804688)
    sq_criss_cross_001_1.nodes["Reroute.001"].location = (-229.585205078125, -226.12326049804688)
    sq_criss_cross_001_1.nodes["Curve to Mesh"].location = (839.244384765625, 37.78522491455078)
    sq_criss_cross_001_1.nodes["Curve Circle"].location = (677.3756103515625, -94.2887954711914)
    sq_criss_cross_001_1.nodes["Quadrilateral"].location = (1184.712646484375, -47.154937744140625)
    sq_criss_cross_001_1.nodes["Curve to Mesh.002"].location = (1359.7564697265625, 37.824989318847656)
    sq_criss_cross_001_1.nodes["Transform Geometry.008"].location = (1000.8998413085938, 67.63076782226562)
    sq_criss_cross_001_1.nodes["Transform Geometry.009"].location = (1539.8919677734375, 124.18328094482422)

    # Set dimensions
    sq_criss_cross_001_1.nodes["Group Input"].width  = 140.0
    sq_criss_cross_001_1.nodes["Group Input"].height = 100.0

    sq_criss_cross_001_1.nodes["Group Output"].width  = 140.0
    sq_criss_cross_001_1.nodes["Group Output"].height = 100.0

    sq_criss_cross_001_1.nodes["H1 Seg2"].width  = 140.0
    sq_criss_cross_001_1.nodes["H1 Seg2"].height = 100.0

    sq_criss_cross_001_1.nodes["Join Curves"].width  = 140.0
    sq_criss_cross_001_1.nodes["Join Curves"].height = 100.0

    sq_criss_cross_001_1.nodes["Weave Height Doubled"].width  = 140.0
    sq_criss_cross_001_1.nodes["Weave Height Doubled"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry"].height = 100.0

    sq_criss_cross_001_1.nodes["Tile Scale.001"].width  = 140.0
    sq_criss_cross_001_1.nodes["Tile Scale.001"].height = 100.0

    sq_criss_cross_001_1.nodes["Join Curves.004"].width  = 140.0
    sq_criss_cross_001_1.nodes["Join Curves.004"].height = 100.0

    sq_criss_cross_001_1.nodes["Join Curves.005"].width  = 140.0
    sq_criss_cross_001_1.nodes["Join Curves.005"].height = 100.0

    sq_criss_cross_001_1.nodes["Set Material"].width  = 140.0
    sq_criss_cross_001_1.nodes["Set Material"].height = 100.0

    sq_criss_cross_001_1.nodes["Join Geometry"].width  = 101.418212890625
    sq_criss_cross_001_1.nodes["Join Geometry"].height = 100.0

    sq_criss_cross_001_1.nodes["Viewer"].width  = 140.0
    sq_criss_cross_001_1.nodes["Viewer"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.001"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.001"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.002"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.002"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.003"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.003"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.004"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.004"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.005"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.005"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.006"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.006"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.007"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.007"].height = 100.0

    sq_criss_cross_001_1.nodes["Reroute"].width  = 20.0
    sq_criss_cross_001_1.nodes["Reroute"].height = 100.0

    sq_criss_cross_001_1.nodes["Reroute.001"].width  = 20.0
    sq_criss_cross_001_1.nodes["Reroute.001"].height = 100.0

    sq_criss_cross_001_1.nodes["Curve to Mesh"].width  = 140.0
    sq_criss_cross_001_1.nodes["Curve to Mesh"].height = 100.0

    sq_criss_cross_001_1.nodes["Curve Circle"].width  = 140.0
    sq_criss_cross_001_1.nodes["Curve Circle"].height = 100.0

    sq_criss_cross_001_1.nodes["Quadrilateral"].width  = 140.0
    sq_criss_cross_001_1.nodes["Quadrilateral"].height = 100.0

    sq_criss_cross_001_1.nodes["Curve to Mesh.002"].width  = 140.0
    sq_criss_cross_001_1.nodes["Curve to Mesh.002"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.008"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.008"].height = 100.0

    sq_criss_cross_001_1.nodes["Transform Geometry.009"].width  = 140.0
    sq_criss_cross_001_1.nodes["Transform Geometry.009"].height = 100.0


    # Initialize sq_criss_cross_001_1 links

    # weave_height_doubled.Value -> tile_scale_001.Z
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Weave Height Doubled"].outputs[0],
        sq_criss_cross_001_1.nodes["Tile Scale.001"].inputs[2]
    )
    # tile_scale_001.Vector -> transform_geometry.Scale
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Tile Scale.001"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry"].inputs[4]
    )
    # group_input.Weave Height -> weave_height_doubled.Value
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Group Input"].outputs[0],
        sq_criss_cross_001_1.nodes["Weave Height Doubled"].inputs[0]
    )
    # join_curves.Geometry -> transform_geometry.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Join Curves"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry"].inputs[0]
    )
    # join_curves_004.Geometry -> join_curves_005.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Join Curves.004"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.005"].inputs[0]
    )
    # set_material.Geometry -> join_curves.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Set Material"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves"].inputs[0]
    )
    # join_curves_005.Geometry -> set_material.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Join Curves.005"].outputs[0],
        sq_criss_cross_001_1.nodes["Set Material"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Join Geometry"].outputs[0],
        sq_criss_cross_001_1.nodes["Group Output"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_001.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_002.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.002"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_003.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.003"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.004"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_005.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.005"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_006.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.006"].inputs[0]
    )
    # h1_seg2.Curve -> transform_geometry_007.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.007"].inputs[0]
    )
    # h1_seg2.Curve -> reroute.Input
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["H1 Seg2"].outputs[0],
        sq_criss_cross_001_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Reroute"].outputs[0],
        sq_criss_cross_001_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Reroute.001"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # join_geometry.Geometry -> viewer.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Join Geometry"].outputs[0],
        sq_criss_cross_001_1.nodes["Viewer"].inputs[0]
    )
    # transform_geometry.Geometry -> curve_to_mesh.Curve
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry"].outputs[0],
        sq_criss_cross_001_1.nodes["Curve to Mesh"].inputs[0]
    )
    # curve_circle.Curve -> curve_to_mesh.Profile Curve
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Curve Circle"].outputs[0],
        sq_criss_cross_001_1.nodes["Curve to Mesh"].inputs[1]
    )
    # transform_geometry_008.Geometry -> join_geometry.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.008"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Geometry"].inputs[0]
    )
    # quadrilateral.Curve -> curve_to_mesh_002.Profile Curve
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Quadrilateral"].outputs[0],
        sq_criss_cross_001_1.nodes["Curve to Mesh.002"].inputs[1]
    )
    # transform_geometry.Geometry -> curve_to_mesh_002.Curve
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry"].outputs[0],
        sq_criss_cross_001_1.nodes["Curve to Mesh.002"].inputs[0]
    )
    # curve_to_mesh.Mesh -> transform_geometry_008.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Curve to Mesh"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.008"].inputs[0]
    )
    # curve_to_mesh_002.Mesh -> transform_geometry_009.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Curve to Mesh.002"].outputs[0],
        sq_criss_cross_001_1.nodes["Transform Geometry.009"].inputs[0]
    )
    # transform_geometry_006.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.006"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_009.Geometry -> join_geometry.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.009"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Geometry"].inputs[0]
    )
    # transform_geometry.Geometry -> join_geometry.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Geometry"].inputs[0]
    )
    # transform_geometry_001.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.001"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_002.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.002"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_007.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.007"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_003.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.003"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_004.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.004"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    # transform_geometry_005.Geometry -> join_curves_004.Geometry
    sq_criss_cross_001_1.links.new(
        sq_criss_cross_001_1.nodes["Transform Geometry.005"].outputs[0],
        sq_criss_cross_001_1.nodes["Join Curves.004"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False

    return sq_criss_cross_001_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    sq_criss_cross_001 = sq_criss_cross_001_1_node_group(node_tree_names)
    node_tree_names[sq_criss_cross_001_1_node_group] = sq_criss_cross_001.name

