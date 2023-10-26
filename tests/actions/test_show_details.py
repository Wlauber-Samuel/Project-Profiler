from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
from datetime import datetime
import os


def get_last_modified_date(file_path):
    """Obtém a data de modificação de um arquivo.

    Args:
        file_path: O caminho para o arquivo.

    Returns:
        Um objeto datetime representando a data de modificação do arquivo.
    """

    last_modified_date = os.stat(file_path).st_mtime
    return datetime.fromtimestamp(last_modified_date)


@pytest.mark.parametrize(
    "file_info, expect",
    [
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details_expect_response(file_info, expect, capsys):
    """Testa se a função `show_details()` retorna a saída esperada para um arquivo inexistente."""

    show_details(file_info)
    captured = capsys.readouterr()
    assert captured.out == expect


@pytest.mark.parametrize(
    "file_info, expect",
    [
        ({}, KeyError),
        ({"base_path": 1}, AttributeError),
    ],
)
def test_show_details_expect_fail(file_info, expect):
    """Testa se a função `show_details()` lança a exceção esperada para um arquivo inválido."""

    with pytest.raises(expect):
        show_details(file_info)


def test_show_details_expect_expected_tmp_path(monkeypatch, tmp_path, capsys):
    """Testa se a função `show_details()` retorna a saída esperada para um arquivo válido."""

    new_path = tmp_path / "teste"
    new_path2 = tmp_path / "teste2.txt"
    new_path.write_text("hey")
    new_path2.write_text("hello word!")

    file_info = {"base_path": str(new_path)}
    show_details(file_info)
    captured = capsys.readouterr()

    last_modified_date_str = get_last_modified_date(new_path).strftime('%Y-%m-%d')

    expected_output = (
        "File name: teste\n"
        "File size in bytes: 28\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: {}\n".format(last_modified_date_str)
    )
    assert captured.out == expected_output

    file_info = {"base_path": str(new_path2)}
    show_details(file_info)
    captured = capsys.readouterr()

    last_modified_date_str = get_last_modified_date(new_path2).strftime('%Y-%m-%d')

    expected_output = (
        "File name: teste2.txt\n"
        "File size in bytes: 40\n"
        "File type: file\n"
        "File extension: .txt\n"
        "Last modified date: {}\n".format(last_modified_date_str)
    )
    assert captured.out == expected_output
