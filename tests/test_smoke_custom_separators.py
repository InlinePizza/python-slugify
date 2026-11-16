"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_custom_separators() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('one two three', algorithm="modern", separator='_') == 'one_two_three'
    assert slugify('one two', algorithm="modern", separator='::') == 'one::two'
