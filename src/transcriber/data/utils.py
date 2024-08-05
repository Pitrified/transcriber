"""Utility functions dealing with IO."""

from pathlib import Path
from typing import Literal


def get_resource(
    which_res: Literal[
        "root_fol",
        "data_fol",
        "sample_fol",
        "quant_model_fol",
        "cache_fol",
        "tmp_audio",
    ]
) -> Path:
    """Get the path of the requested resource."""
    # specific resources
    if which_res == "tmp_audio":
        return get_resource("cache_fol") / "temp_audio.mp3"

    # folders that are not in the package
    if which_res == "quant_model_fol":
        return Path.home() / "models" / "quantized"

    # folders that are in the package
    if which_res == "root_fol":
        return Path(__file__).absolute().parents[3]
    elif which_res == "data_fol":
        return get_resource("root_fol") / "data"
    elif which_res == "sample_fol":
        return get_resource("root_fol") / "data" / "sample"
    elif which_res == "cache_fol":
        return get_resource("root_fol") / ".cache"


def check_create_fol(
    fol: Path,
) -> None:
    """Check if folder exists, if not create it."""
    if not fol.exists():
        fol.mkdir(parents=True)
