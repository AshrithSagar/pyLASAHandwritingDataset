"""
Dataset core
"""
# src/pyLASAHandwritingDataset/dataset.py

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, TypeGuard

import numpy as np
from scipy.io import loadmat

from pyLASAHandwritingDataset._downloader import get_dataset_dir
from pyLASAHandwritingDataset.motions import ALL_HANDWRITING_MOTIONS, HandwritingMotion

__all__ = ["DataSet", "LASADemonstration", "LASAPattern"]


def is_handwriting_motion(name: str) -> TypeGuard[HandwritingMotion]:
    return name in ALL_HANDWRITING_MOTIONS


@dataclass(frozen=True)
class LASADemonstration:
    """A container for a single demonstration of some handwriting motion in the LASA Handwriting Dataset."""

    pos: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    """
    2 x 1000 matrix representing the motion in 2D space.
    The first and second rows correspond to x and y axes in the Cartesian space, respectively.
    """

    t: np.ndarray[tuple[Literal[1], Literal[1000]], np.dtype[np.float64]]
    """
    1 x 1000 vector indicating the corresponding time for each datapoint (i.e. each column of demos{n}.pos).
    """

    vel: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    """
    2 x 1000 matrix representing the velocity of the motion.
    """

    acc: np.ndarray[tuple[Literal[2], Literal[1000]], np.dtype[np.float64]]
    """
    2 x 1000 matrix representing the acceleration of the motion.
    """


@dataclass(frozen=True)
class LASAPattern:
    """A container for a handwriting motion pattern in the LASA Handwriting Dataset."""

    name: HandwritingMotion

    dt: float
    """
    The average time steps across all demonstrations.
    """

    demos: tuple[
        LASADemonstration,
        LASADemonstration,
        LASADemonstration,
        LASADemonstration,
        LASADemonstration,
        LASADemonstration,
        LASADemonstration,
    ]  # 7
    """
    A structure variable containing necessary information about all demonstrations.
    """

    def __post_init__(self) -> None:
        if self.name not in ALL_HANDWRITING_MOTIONS:
            raise ValueError(f"Unknown shape {self.name!r}")

    def __repr__(self) -> str:
        return f"LASAPattern({self.name!r}, {len(self.demos)} demos, dt={self.dt:.4g})"


class LASAHandwritingDataset:
    _data: dict[HandwritingMotion, LASAPattern] | None = None
    _root: Path | None = None

    @classmethod
    def _load(cls) -> None:
        if cls._data is not None:
            return

        root = get_dataset_dir()
        cls._root = root

        data: dict[HandwritingMotion, LASAPattern] = {}
        for mat_path in root.glob("*.mat"):
            name = mat_path.stem
            if not is_handwriting_motion(name):
                continue

            mat: dict[str, Any] = loadmat(str(mat_path))
            dt: float = mat["dt"].item()

            _demos: list[LASADemonstration] = []
            for demo_struct in mat["demos"][0]:
                demo = demo_struct[0][0]
                pos = np.asarray(demo["pos"], dtype=np.float64)
                t = np.asarray(demo["t"], dtype=np.float64)
                vel = np.asarray(demo["vel"], dtype=np.float64)
                acc = np.asarray(demo["acc"], dtype=np.float64)

                _demos.append(LASADemonstration(pos=pos, t=t, vel=vel, acc=acc))

            demos = tuple(_demos)
            assert len(demos) == 7
            data[name] = LASAPattern(name=name, dt=dt, demos=demos)

        cls._data = data

    @classmethod
    def handwriting_motions(cls) -> tuple[HandwritingMotion, ...]:
        cls._load()
        assert cls._data is not None
        return tuple(sorted(cls._data))

    def __getitem__(self, name: HandwritingMotion) -> LASAPattern:
        if name not in ALL_HANDWRITING_MOTIONS:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}.\n"
                f"Available shapes: {', '.join(ALL_HANDWRITING_MOTIONS)}."
            )
        self._load()
        assert self._data is not None
        return self._data[name]

    # This is only provided in case one prefers attribute access, although risky.
    def __getattr__(self, name: HandwritingMotion) -> LASAPattern:  # type: ignore[misc]
        return self.__getitem__(name)


DataSet = LASAHandwritingDataset()
