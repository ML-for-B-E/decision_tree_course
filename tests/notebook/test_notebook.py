import pytest
from testing_tools.notebook import (
    assert_notebook_is_without_outputs,
    assert_notebook_runs_without_errors,
)
from testing_tools.notebook import list_notebooks
from summer.tools.common_path import NOTEBOOK_PATH


@pytest.mark.tuto
@pytest.mark.parametrize("notebook", list_notebooks(NOTEBOOK_PATH))
def test_tuto_are_without_output(notebook: str) -> None:
    assert_notebook_is_without_outputs(NOTEBOOK_PATH / notebook)


@pytest.mark.timeout(5 * 40)
@pytest.mark.tuto
@pytest.mark.parametrize("notebook", list_notebooks(NOTEBOOK_PATH))
def test_stencil_runs_without_error_SLOW_SLOW_SLOW(notebook: str) -> None:
    assert_notebook_runs_without_errors(NOTEBOOK_PATH / notebook)
