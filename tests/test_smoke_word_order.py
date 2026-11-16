"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_word_order() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('alpha beta gamma', algorithm="modern", max_length=10, word_boundary=True, save_order=True) == 'alpha-beta'
    assert slugify('one two three', algorithm="modern", max_length=7, word_boundary=True) == 'one-two'
