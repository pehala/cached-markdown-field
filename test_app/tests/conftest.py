import pytest


@pytest.fixture(scope="function")
def use_runtime_cache(settings):
    settings.MARKDOWN_CACHE_RUNTIME = True


@pytest.fixture(scope="function")
def no_cache(settings):
    settings.MARKDOWN_CACHE = False
