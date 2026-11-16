"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_replacements() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('cats and dogs', algorithm="modern", replacements=[('cats', 'birds')]) == 'birds-and-dogs'
    assert slugify('x y', algorithm="modern", replacements=[('x', 'first')]) == 'first-y'
