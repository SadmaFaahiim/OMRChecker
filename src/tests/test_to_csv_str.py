from pathlib import Path, PurePosixPath, PureWindowsPath

from src.utils.file import to_csv_str


def test_to_csv_str_accepts_windows_path():
    """Windows paths must be normalized to forward slashes regardless of host OS."""
    path = PureWindowsPath(r"samples\answer-key\using-csv\adrian_omr.png")
    assert to_csv_str(path) == "samples/answer-key/using-csv/adrian_omr.png"


def test_to_csv_str_accepts_posix_path():
    """POSIX paths must pass through unchanged."""
    path = PurePosixPath("samples/answer-key/using-csv/adrian_omr.png")
    assert to_csv_str(path) == "samples/answer-key/using-csv/adrian_omr.png"


def test_to_csv_str_accepts_host_path():
    """A host-native Path must be normalized to forward slashes."""
    path = Path("outputs") / "CheckedOMRs" / "adrian_omr.png"
    assert to_csv_str(path) == "outputs/CheckedOMRs/adrian_omr.png"


def test_to_csv_str_accepts_string():
    """Plain string paths must also be normalized to forward slashes."""
    assert to_csv_str(r"outputs\Manual\ErrorFiles.csv") == "outputs/Manual/ErrorFiles.csv"