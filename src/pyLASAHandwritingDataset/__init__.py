"""
LASA Handwriting Dataset, version 2.0\n
See https://bitbucket.org/khansari/lasahandwritingdataset/src/master/Readme.txt
"""
# src/pyLASAHandwritingDataset/__init__.py

from pyLASAHandwritingDataset.dataset import (
    DataSet,
    LASADemonstration,
    LASAPattern,
    ShapeName,
)
from pyLASAHandwritingDataset.shapes import ALL_SHAPES

__version__ = "0.1.0"
__all__ = [
    "__version__",
    "DataSet",
    "LASADemonstration",
    "LASAPattern",
    "ShapeName",
    "ALL_SHAPES",
]
