import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    """Home route should return HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_content(client):
    """Home route should return the expected message."""
    response = client.get("/")
    assert b"Hello from Azure DevOps Pipeline + Flask!" in response.data


def test_home_content_type(client):
    """Home route should return plain text."""
    response = client.get("/")
    assert "text/html" in response.content_type


def test_unknown_route_returns_404(client):
    """Any undefined route should return HTTP 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404