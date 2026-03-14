# pyLASAHandwritingDataset

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[LASA Handwriting dataset](https://bitbucket.org/khansari/lasahandwritingdataset) for Python3

This package provides a typed, lightweight Python interface for loading and accessing the dataset.

## Installation

Install the package from PyPI:

```shell
# Using uv
uv add pylasahandwritingdataset

# Or with pip
pip3 install pylasahandwritingdataset
```

To install from the latest commit:

```shell
uv add git+https://github.com/AshrithSagar/pyLASAHandwritingDataset.git@main
```

## Usage

```python
from pyLASAHandwritingDataset import DataSet

# List available motions
motions = DataSet.handwriting_motions()
print(motions)  # ('Angle', 'BendedLine', 'CShape', 'DoubleBendedLine', 'GShape', 'JShape', 'JShape_2', 'Khamesh', 'LShape', 'Leaf_1', 'Leaf_2', 'Line', 'Multi_Models_1', 'Multi_Models_2', 'Multi_Models_3', 'Multi_Models_4', 'NShape', 'PShape', 'RShape', 'Saeghe', 'Sharpc', 'Sine', 'Snake', 'Spoon', 'Sshape', 'Trapezoid', 'WShape', 'Worm', 'Zshape', 'heee')

# Load a motion pattern
pattern = DataSet["GShape"]
print(pattern.name)  # "GShape"
print(pattern.dt)
print(len(pattern.demos))  # 7

# Access demonstrations
demo = pattern.demos[0]
t   = demo.t    # shape (1, 1000)
pos = demo.pos  # shape (2, 1000)
vel = demo.vel  # shape (2, 1000)
acc = demo.acc  # shape (2, 1000)
```

For documentation, refer to the original dataset repo's [README](https://bitbucket.org/khansari/lasahandwritingdataset/src/master/Readme.txt).

## Reference

If you use this dataset in research, please cite the original author:

```
S. M. Khansari-Zadeh and A. Billard, "Learning Stable Non-Linear Dynamical
Systems with Gaussian Mixture Models", IEEE Transaction on Robotics, 2011.
```

## License

The LASA Handwriting Dataset is free for non-commercial academic use.

Please refer to the [original dataset repository](https://bitbucket.org/khansari/lasahandwritingdataset) for licensing details.
