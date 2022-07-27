from pathlib import Path
import pytest

import matplotlib.pyplot as plt

from summer.tools.common_path import NOTEBOOK_PATH


@pytest.mark.tuto
def test_tuto_are_without_output(dir_path=NOTEBOOK_PATH) -> None:
    # Given
    from boar.linting import lint_notebook

    # When
    lint_kwargs = dict(inline=False, verbose=False, recursion_level=-1000)
    bad_lint_paths = lint_notebook(dir_path, **lint_kwargs)

    # Then
    if len(bad_lint_paths) != 0:
        bad_lint_files = [Path(bad_lint_path).name for bad_lint_path in bad_lint_paths]
        msg = f"Clear output in: {bad_lint_files}"
        raise Exception(msg)


@pytest.mark.tuto
@pytest.mark.parametrize(
    "notebook_name",
    [
        "1-simple_linear_regression.ipynb",
        "2-infer_decision_tree_from_data.ipynb",
        "3-logistic_regression.ipynb",
        "5-deep-learning/classifieur_cancerSein.ipynb",
        "5-deep-learning/convolution_image.ipynb",
    ],
)
def test_tuto_runs_without_error(
    notebook_name: str,
    dir_path=NOTEBOOK_PATH,
) -> None:
    # Given
    from boar.testing import assert_notebook

    notebook_path = Path(dir_path, notebook_name)

    # When / Then
    assert notebook_path.exists()
    assert_notebook(notebook_path, verbose=True)

    # Finally
    plt.close("all")
