import pytest
from pro_filer.actions.main_actions import show_preview

def create_context(files, dirs):
    return {
        "all_files": files,
        "all_dirs": dirs,
    }

def test_show_preview_response_with_valid_context(capsys):
    context = create_context(
        ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        ["src", "src/utils"],
    )
    show_preview(context)
    captured = capsys.readouterr()

    expected_output = """
Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']
    """

    # Use strip() para remover espaços em branco e quebras de linha extras
    assert captured.out.strip() == expected_output.strip()
