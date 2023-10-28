from pro_filer.actions.main_actions import show_details
import pytest
from datetime import datetime
import os


@pytest.mark.parametrize(
    "context, expected_output",
    [
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details_file_not_found(context, expected_output, capsys):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


@pytest.mark.parametrize(
    "context, expected_exception",
    [
        ({}, KeyError),
        ({"base_path": 1}, AttributeError),
    ],
)
def test_show_details_exceptions(context, expected_exception):
    with pytest.raises(expected_exception):
        show_details(context)


def test_show_details_temp_file_details(monkeypatch, tmp_path, capsys):
    new_path = tmp_path / "teste"
    new_path2 = tmp_path / "teste2.txt"
    new_path.write_text("hello")
    new_path2.write_text("hello word!")

    context = {"base_path": str(new_path)}
    show_details(context)
    captured = capsys.readouterr()

    last_modified_date = os.stat(new_path).st_mtime
    last_modified_date = datetime.fromtimestamp(last_modified_date)
    last_modified_date_str = last_modified_date.strftime('%Y-%m-%d')
    
    expected_output = (
        "File name: teste\n"
        "File size in bytes: 5\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: {}\n".format(last_modified_date_str)
    )
    assert captured.out == expected_output

    context = {"base_path": str(new_path2)}
    show_details(context)
    captured = capsys.readouterr()

    last_modified_date = os.stat(new_path2).st_mtime
    last_modified_date = datetime.fromtimestamp(last_modified_date)
    last_modified_date_str = last_modified_date.strftime('%Y-%m-%d')
    
    expected_output = (
        "File name: teste2.txt\n"
        "File size in bytes: 11\n"
        "File type: file\n"
        "File extension: .txt\n"
        "Last modified date: {}\n".format(last_modified_date_str)
    )
    assert captured.out == expected_output