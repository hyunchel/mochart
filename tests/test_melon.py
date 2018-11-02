import pytest

from mochart import melon


@pytest.mark.integration
def test_top_100():
    """Assert total of 100 ranks are fetched."""
    assert len(melon.realtime()) == 100
