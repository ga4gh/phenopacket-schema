import os

import pytest


@pytest.fixture(scope="session")
def fpath_python_src_dir(
    fpath_test_dir: str,
) -> str:
    return os.path.realpath(
        os.path.join(
            fpath_test_dir,
            os.pardir,
        )
    )


@pytest.fixture(scope='session')
def fpath_test_dir() -> str:
    # When running `pytest` from the top-level Python folder (`phenopacket-schema/python`)
    # this path will evaluate to the `tests` folder.
    return os.path.dirname(__file__)


@pytest.fixture(scope="session")
def fpath_test_data_dir(
    fpath_python_src_dir: str,
) -> str:
    # When running `pytest` from the top-level Python folder (`phenopacket-schema/python`)
    # this path will evaluate to the `data` folder.
    return os.path.join(fpath_python_src_dir, "data")
