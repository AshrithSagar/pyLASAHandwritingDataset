"""
Downloader utils
"""
# src/pyLASAHandwritingDataset/downloader.py

import shutil
import zipfile
from pathlib import Path

import platformdirs
import pooch  # type: ignore[import-untyped]

PKG_NAME = "pyLASAHandwritingDataset"
COMMIT_FULLHASH = "38304f7c0ac4708b0fd38331d94d02095ad0ccfd" or "master"
REPO_URL = (
    f"https://bitbucket.org/khansari/lasahandwritingdataset/get/{COMMIT_FULLHASH}.zip"
)
CHECKSUM = "sha256:3a0fd4e26e042828f65a507891bfb558b93defaae3580d711c66321d59ecd2b0"

_CACHE_ROOT = Path(platformdirs.user_cache_dir(PKG_NAME))
DATASET_ROOT = _CACHE_ROOT / "DataSet"
_ZIP_NAME = "lasahandwritingdataset.zip"


def get_dataset_dir() -> Path:
    """
    Returns path to the DataSet folder with all .mat files.
    Downloads + extracts + moves DataSet up one level on first run.
    """
    if DATASET_ROOT.is_dir() and list(DATASET_ROOT.glob("*.mat")):
        return DATASET_ROOT

    _CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    zip_path = _CACHE_ROOT / _ZIP_NAME

    pooch.retrieve(  # pyright: ignore[reportUnknownMemberType]
        url=REPO_URL,
        known_hash=CHECKSUM,
        fname=zip_path.name,
        path=_CACHE_ROOT,
        progressbar=True,
    )

    # Temporary extraction root
    temp_extract = _CACHE_ROOT / "temp_extract"
    if temp_extract.exists():
        shutil.rmtree(temp_extract)
    temp_extract.mkdir()
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(path=temp_extract)

    # The zip creates exactly one top-level folder
    top_level_dirs = [d for d in temp_extract.iterdir() if d.is_dir()]
    if len(top_level_dirs) != 1:
        raise RuntimeError(
            f"Expected one top-level folder in zip, found {len(top_level_dirs)}"
        )
    repo_dir = top_level_dirs[0]  # "khansari-lasahandwritingdataset-38304f7c0ac4"

    source_dataset = repo_dir / "DataSet"
    if not source_dataset.is_dir():
        raise RuntimeError("DataSet folder not found inside extracted repo directory")

    if DATASET_ROOT.exists():
        shutil.rmtree(DATASET_ROOT)  # clean any previous partial state
    shutil.move(str(source_dataset), str(DATASET_ROOT))

    # Clean up everything else
    shutil.rmtree(temp_extract)
    zip_path.unlink(missing_ok=True)

    mat_count = len(list(DATASET_ROOT.glob("*.mat")))
    if mat_count != 30:
        raise RuntimeError(
            f"Expected 30 .mat files in {DATASET_ROOT}, found {mat_count}"
        )

    print(f"Successfully extracted {mat_count} .mat files to {DATASET_ROOT}")
    return DATASET_ROOT
