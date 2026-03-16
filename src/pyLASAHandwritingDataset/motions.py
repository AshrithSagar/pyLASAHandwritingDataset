"""
Handwriting motions (shapes) in the LASA Handwriting Dataset
"""
# src/pyLASAHandwritingDataset/motions.py

from typing import Final, Literal, TypeAlias, TypeGuard

SinglePatternMotion: TypeAlias = Literal[
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

MultiModelMotion: TypeAlias = Literal[
    "Multi_Models_1",
    "Multi_Models_2",
    "Multi_Models_3",
    "Multi_Models_4",
]

HandwritingMotion: TypeAlias = SinglePatternMotion | MultiModelMotion


ALL_SINGLE_PATTERN_MOTIONS: Final = (
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

ALL_MULTI_MODEL_MOTIONS: Final = (
    "Multi_Models_1",
    "Multi_Models_2",
    "Multi_Models_3",
    "Multi_Models_4",
)

ALL_HANDWRITING_MOTIONS: Final = ALL_SINGLE_PATTERN_MOTIONS + ALL_MULTI_MODEL_MOTIONS


def is_single_pattern_motion(pattern_name: str) -> TypeGuard[SinglePatternMotion]:
    return pattern_name in ALL_SINGLE_PATTERN_MOTIONS


def is_multi_model_motion(pattern_name: str) -> TypeGuard[MultiModelMotion]:
    return pattern_name in ALL_MULTI_MODEL_MOTIONS


def is_handwriting_motion(pattern_name: str) -> TypeGuard[HandwritingMotion]:
    return pattern_name in ALL_HANDWRITING_MOTIONS
