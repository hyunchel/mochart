from datetime import datetime, timedelta

import pytest

from mochart import (melon, mnet, naver, gaon, oricon)


PROVIDERS = [melon, mnet, naver, gaon, oricon]


@pytest.mark.integration
def test_sanity_checks():
    """Assert some ranks are fetched."""
    two_days_ago = datetime.now() - timedelta(days=2)
    for provider in PROVIDERS:
        try:
            assert len(provider.day(two_days_ago)) > 5
        except TypeError:
            assert len(provider.day()) > 5
        except AttributeError:
            assert len(provider.week(two_days_ago)) > 5
