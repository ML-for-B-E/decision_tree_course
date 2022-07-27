import numpy as np
import pytest


@pytest.mark.ut
def test_entropy_for_binary_variable_returns_correct_values():
    # Given
    from summer.model.tree import entropy_for_binary_variable

    probability = 1 / 4
    expected_entropy = 0.8112781244591328

    # When
    entropy = entropy_for_binary_variable(probability)

    # Then
    np.testing.assert_allclose(entropy, expected_entropy)
