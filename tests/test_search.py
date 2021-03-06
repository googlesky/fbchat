import pytest

pytestmark = pytest.mark.online


def test_search_for(client1):
    users = client1.search_for_users("Mark Zuckerberg")
    assert len(users) > 0

    u = users[0]

    assert u.id == "4"
    assert u.photo[:4] == "http"
    assert u.url[:4] == "http"
    assert u.name == "Mark Zuckerberg"
