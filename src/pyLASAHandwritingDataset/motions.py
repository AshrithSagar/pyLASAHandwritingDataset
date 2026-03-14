"""
Handwriting motions (shapes) in the LASA Handwriting Dataset
"""
# src/pyLASAHandwritingDataset/motions.py

from typing import Literal

SinglePatternMotion = Literal[
    "Angle",
    "BendedLine",
    "CShape",
    "DoubleBendedLine",
    "GShape",
    "heee",
    "JShape_2",
    "JShape",
    "Khamesh",
    "Leaf_1",
    "Leaf_2",
    "Line",
    "LShape",
    "NShape",
    "PShape",
    "RShape",
    "Saeghe",
    "Sharpc",
    "Sine",
    "Snake",
    "Spoon",
    "Sshape",
    "Trapezoid",
    "Worm",
    "WShape",
    "Zshape",
]

MultiModelMotion = Literal[
    "Multi_Models_1",
    "Multi_Models_2",
    "Multi_Models_3",
    "Multi_Models_4",
]

HandwritingMotion = SinglePatternMotion | MultiModelMotion


ALL_SINGLE_PATTERN_MOTIONS = (
    "Angle",
    "BendedLine",
    "CShape",
    "DoubleBendedLine",
    "GShape",
    "heee",
    "JShape_2",
    "JShape",
    "Khamesh",
    "Leaf_1",
    "Leaf_2",
    "Line",
    "LShape",
    "NShape",
    "PShape",
    "RShape",
    "Saeghe",
    "Sharpc",
    "Sine",
    "Snake",
    "Spoon",
    "Sshape",
    "Trapezoid",
    "Worm",
    "WShape",
    "Zshape",
)

ALL_MULTI_MODEL_MOTIONS = (
    "Multi_Models_1",
    "Multi_Models_2",
    "Multi_Models_3",
    "Multi_Models_4",
)

ALL_HANDWRITING_MOTIONS = ALL_SINGLE_PATTERN_MOTIONS + ALL_MULTI_MODEL_MOTIONS
