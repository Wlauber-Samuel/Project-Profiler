from pro_filer.actions.main_actions import show_preview
import pytest

mock = str([
    "src/__init__.py",
    "src/app.py",
    "src/app.py",
    "src/app.py",
    "src/app.py"
])


@pytest.mark.parametrize("context, expect", [
    ({"all_files": [], "all_dirs": []}, "Found 0 files and 0 directories\n"),
    ({
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }, """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']\n"""),
    ({
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/app.py",
            "src/app.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }, f"""Found 6 files and 2 directories
First 5 files: {mock}
First 5 directories: ['src', 'src/utils']\n"""),
])
def test_show_preview_response_ok(context, expect, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expect


@pytest.mark.parametrize("context2, expect", [
    ({"all_dirs": []}, KeyError),
    ({"all_files": []}, KeyError),
    ({}, KeyError),
])
def test_show_preview_response_fail(context2, expect):
    with pytest.raises(expect):
        show_preview(context2)