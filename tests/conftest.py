import pytest
import os   
import logging

def pytest_addoption(parser):
    parser.addoption("--access_key", action="store", default=None, help="API access key")

@pytest.fixture(scope="session")
def access_key(request):
    key = request.config.getoption("--access_key")
    if not key:
        key = os.environ.get("WEATHERSTACK_KEY")
    if not key:
        pytest.fail("API access key not provided. Use --access_key or set WEATHERSTACK_KEY env var.")
    return key


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]  # StreamHandler outputs to console
    )


@pytest.fixture
def logger(request):
    name = request.node.name
    return logging.getLogger(name)