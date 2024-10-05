"""
Test Main
"""

from main import main_result


def test_func():
    return main_result()


if __name__ == "__main__":
    assert test_func()["extract_to"] == "kickstarter_2018.csv"
    assert test_func()["transform_db"] == "KickstarterDB.db"
    assert test_func()["create"] == "Create Success"
    assert test_func()["read"] == "Read Success"
    assert test_func()["update"] == "Update Success"
    assert test_func()["delete"] == "Delete Success"
