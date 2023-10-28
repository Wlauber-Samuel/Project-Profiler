from pro_filer.actions.main_actions import show_disk_usage
from unittest.mock import Mock


def test_show_disk_usage_expected(monkeypatch, tmp_path, capsys):
    mock = Mock(return_value='teste.txt')

    new_path = tmp_path / "teste.txt"

    new_path2 = tmp_path / "teste2.txt"

    new_path.write_text('heloo')

    new_path2.write_text('hello word!')

    context = {"all_files": [str(new_path), str(new_path2)]}
    monkeypatch.setattr(
        'pro_filer.actions.main_actions._get_printable_file_path', mock)
    show_disk_usage(context)

    assert capsys.readouterr().out == f''''teste.txt':{''.ljust(59)}11 (68%)
'teste.txt':{''.ljust(59)}5 (31%)
Total size: 16\n'''
    