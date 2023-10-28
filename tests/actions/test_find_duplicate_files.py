from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_fail():

    file_paths = [
        ".gitignore",
        "src/app.py",
        "src/utils/_init_.py",
    ]
    context = {"all_files": file_paths}
    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)


def test_find_duplicate_files_expected():

    file_paths = [
        "./tests/_init_.py",
        "./tests/actions/_init_.py",
        "./pro_filer/_init_.py",
    ]
    context = {"all_files": file_paths}
    assert find_duplicate_files(context) == [
        ("./tests/_init.py", "./tests/actions/__init_.py"),
        ("./tests/_init.py", "./pro_filer/__init_.py"),
        ("./tests/actions/_init.py", "./pro_filer/__init_.py"),
    ]


def test_show_disk_usage_expected(monkeypatch, tmp_path, capsys):
    
    file1 = tmp_path / "teste.txt"
    file2 = tmp_path / "teste2.txt"
    file1.write_text("heloo")
    file2.write_text("hello word!")
    file1_path = str(file1)
    file2_path = str(file2)
    context = {"all_files": [file1_path, file2_path]}
    assert find_duplicate_files(context) == []