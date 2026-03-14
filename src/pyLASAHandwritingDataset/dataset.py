"""
LASA Handwriting Dataset
"""
# src/pyLASAHandwritingDataset/dataset.py

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, cast

import numpy as np
from scipy.io import loadmat

from pyLASAHandwritingDataset.downloader import get_dataset_dir
from pyLASAHandwritingDataset.shapes import ALL_SHAPES, ShapeName

__all__ = ["DataSet", "Demo", "Pattern", "ShapeName"]


@dataclass(frozen=True)
class Demo:
    pos: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    vel: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    acc: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    t: np.ndarray[tuple[Literal[1000]], np.dtype[np.float64]]
    dt: float  # Time step used for numerical diff (approx)


@dataclass(frozen=True)
class Pattern:
    name: ShapeName
    dt: float
    demos: tuple[Demo, Demo, Demo, Demo, Demo, Demo, Demo]  # 7

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
            dt: float = mat["dt"].item()

            _demos: list[Demo] = []
            for demo_struct in mat["demos"][0]:
                d = demo_struct[0][0]
                pos = np.asarray(d["pos"], dtype=np.float64)
                vel = np.asarray(d["vel"], dtype=np.float64)
                acc = np.asarray(d["acc"], dtype=np.float64)
                t = cast(
                    np.ndarray[tuple[Literal[1000]], np.dtype[np.float64]],
                    np.asarray(d["t"], dtype=np.float64).ravel(),
                )

                _demos.append(Demo(pos=pos, vel=vel, acc=acc, t=t, dt=dt))

            demos = tuple[Demo, Demo, Demo, Demo, Demo, Demo, Demo](_demos)
            data[name] = Pattern(name=name, dt=dt, demos=demos)

        cls._data = data

    @classmethod
    def shapes(cls) -> tuple[ShapeName, ...]:
        cls._load()
        assert cls._data is not None
        return tuple(sorted(cls._data))

    def __getitem__(self, name: ShapeName) -> Pattern:
        if name not in ALL_SHAPES:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}.\n"
                f"Available shapes: {', '.join(ALL_SHAPES)}."
            )
        self._load()
        assert self._data is not None
        return self._data[name]

    def __getattr__(self, name: ShapeName) -> Pattern:
        return self.__getitem__(name)


DataSet = LASAHandwritingDataset()
