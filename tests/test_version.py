import pytest


def test_version():
    import deplodocker

    assert deplodocker.__version__ == "0.1.0"
