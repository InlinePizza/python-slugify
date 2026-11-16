"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_length_limits() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('alpha beta', algorithm="modern", max_length=5) == 'alpha'
    assert slugify('alpha beta', algorithm="modern", max_length=0) == 'alpha-beta'
