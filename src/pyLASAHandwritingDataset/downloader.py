"""
Downloader utils
"""
# src/pyLASAHandwritingDataset/downloader.py

import hashlib
import shutil
from pathlib import Path
from zipfile import ZipFile

import platformdirs
import requests

PKG_NAME = "pyLASAHandwritingDataset"
COMMIT_FULLHASH = "38304f7c0ac4708b0fd38331d94d02095ad0ccfd" or "master"
REPO_ZIP_URL = (
    f"https://bitbucket.org/khansari/lasahandwritingdataset/get/{COMMIT_FULLHASH}.zip"
)
CHECKSUM = "sha256:3a0fd4e26e042828f65a507891bfb558b93defaae3580d711c66321d59ecd2b0"

_CACHE_ROOT = Path(platformdirs.user_cache_dir(PKG_NAME))
DATASET_ROOT = _CACHE_ROOT / "DataSet"
_ZIP_NAME = "lasahandwritingdataset.zip"
EXPECTED_MAT_COUNT = 30


def _download(url: str, dest: Path) -> None:
    hasher = hashlib.sha256()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if not chunk:
                    continue
                f.write(chunk)
                hasher.update(chunk)

    digest = hasher.hexdigest()
    if digest != CHECKSUM.split(":", 1)[1]:
        dest.unlink(missing_ok=True)
        raise ValueError(
            f"SHA256 hash of downloaded file ({_ZIP_NAME}) does not match the known hash: expected {CHECKSUM} but got {digest}. "
            "Deleted download for safety. The downloaded file may have been corrupted or the known hash may be outdated."
        )


def get_dataset_dir() -> Path:
    """
    Returns path to the DataSet folder with all .mat files.
    Downloads + extracts + moves DataSet up one level on first run.
    """
    if DATASET_ROOT.is_dir() and list(DATASET_ROOT.glob("*.mat")):
        return DATASET_ROOT

    _CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    zip_path = _CACHE_ROOT / _ZIP_NAME

    if not zip_path.exists():
        _download(REPO_ZIP_URL, zip_path)

    # Temporary extraction root
    temp_extract = _CACHE_ROOT / "temp_extract"
    if temp_extract.exists():
        shutil.rmtree(temp_extract)
    temp_extract.mkdir()
    with ZipFile(zip_path) as zf:
        zf.extractall(path=temp_extract)

    repo_dir = next(
        temp_extract.iterdir()
    )  # "khansari-lasahandwritingdataset-38304f7c0ac4"
    source_dataset = repo_dir / "DataSet"

    if DATASET_ROOT.exists():
        shutil.rmtree(DATASET_ROOT)  # Clean any previous partial state
    shutil.move(str(source_dataset), str(DATASET_ROOT))

    # Clean up everything else
    shutil.rmtree(temp_extract)
    zip_path.unlink(missing_ok=True)

    mat_count = len(list(DATASET_ROOT.glob("*.mat")))
    if mat_count != EXPECTED_MAT_COUNT:
        raise RuntimeError(
            f"Expected {EXPECTED_MAT_COUNT} .mat files in {DATASET_ROOT}, found {mat_count}"
        )

    return DATASET_ROOT
