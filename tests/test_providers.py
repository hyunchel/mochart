import pytest

from mochart import (melon, mnet, naver, gaon, oricon)


PROVIDERS = [melon, mnet, naver, gaon, oricon]


@pytest.mark.integration
def test_sanity_checks():
    """Assert some ranks are fetched."""
    for provider in PROVIDERS:
        try:
            assert len(provider.day()) > 5
        except AttributeError:
            assert len(provider.week()) > 5
