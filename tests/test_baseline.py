import pytest

from baseline import tasks


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_absent_item():
    assert tasks.first_missing(["a", "b", "c"], ["a", "c"]) == "b"