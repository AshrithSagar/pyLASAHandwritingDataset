"""
LASA Handwriting Dataset
"""
# src/pyLASAHandwritingDataset/dataset.py

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.io import loadmat

from pyLASAHandwritingDataset.downloader import get_dataset_dir
from pyLASAHandwritingDataset.shapes import ALL_SHAPES, ShapeName


@dataclass(frozen=True)
class Demo:
    pos: np.ndarray  # (2, N) float64
    vel: np.ndarray  # (2, N)
    acc: np.ndarray  # (2, N)
    t: np.ndarray  # (1, N) or (N,)
    dt: float  # time step used for numerical diff (approx)


@dataclass(frozen=True)
class Pattern:
    name: ShapeName
    dt: float
    demos: tuple[Demo, ...]  # 7

    def __post_init__(self):
        if self.name not in ALL_SHAPES:
            raise ValueError(f"Unknown shape {self.name!r}")

    def __repr__(self):
        return f"Pattern({self.name!r}, {len(self.demos)} demos, dt={self.dt:.4g})"


class LASAHandwritingDataset:
    _data: dict[ShapeName, Pattern] | None = None
    _root: Path | None = None

    @classmethod
    def _load(cls) -> None:
        if cls._data is not None:
            return

        root = get_dataset_dir()
        cls._root = root

        data: dict[ShapeName, Pattern] = {}
        for mat_path in root.glob("*.mat"):
            name = mat_path.stem
            if name not in ALL_SHAPES:
                continue

            mat = loadmat(str(mat_path))
            dt = float(mat["dt"].item())

            demos: list[Demo] = []
            for demo_struct in mat["demos"][0]:
                d = demo_struct[0][0]
                pos = np.asarray(d["pos"], dtype=np.float64)  # (2,N)
                vel = np.asarray(d["vel"], dtype=np.float64)
                acc = np.asarray(d["acc"], dtype=np.float64)
                t = np.asarray(d["t"], dtype=np.float64).ravel()

                demos.append(Demo(pos=pos, vel=vel, acc=acc, t=t, dt=dt))

            data[name] = Pattern(name=name, dt=dt, demos=tuple(demos))

        cls._data = data

    @classmethod
    def shapes(cls) -> tuple[ShapeName, ...]:
        cls._load()
        assert cls._data is not None
        return tuple(sorted(cls._data))

    def __getattr__(self, name: ShapeName) -> Pattern:
        if name not in ALL_SHAPES:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}. "
                f"Available shapes: {', '.join(ALL_SHAPES)}"
            )
        self._load()
        assert self._data is not None
        return self._data[name]

    def __dir__(self) -> list[str]:
        return sorted(set(ALL_SHAPES) | {"shapes"})


DataSet = LASAHandwritingDataset()
