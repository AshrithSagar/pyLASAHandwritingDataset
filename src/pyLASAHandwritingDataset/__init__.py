"""
LASA Handwriting Dataset, version 2.0\n
See https://bitbucket.org/khansari/lasahandwritingdataset/src/master/Readme.txt
"""
# src/pyLASAHandwritingDataset/__init__.py

from pyLASAHandwritingDataset.dataset import (
    DataSet,
    LASADemonstration,
    LASAPattern,
)
from pyLASAHandwritingDataset.motions import (
    ALL_HANDWRITING_MOTIONS,
    ALL_MULTI_MODEL_MOTIONS,
    ALL_SINGLE_PATTERN_MOTIONS,
    HandwritingMotion,
    MultiModelMotion,
    SinglePatternMotion,
)

__version__ = "0.1.0"
__all__ = [
    "__version__",
    #
    "DataSet",
    "LASADemonstration",
    "LASAPattern",
    #
    "ALL_HANDWRITING_MOTIONS",
    "ALL_MULTI_MODEL_MOTIONS",
    "ALL_SINGLE_PATTERN_MOTIONS",
    "HandwritingMotion",
    "MultiModelMotion",
    "SinglePatternMotion",
]
