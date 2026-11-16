"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_empty_inputs() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('', algorithm="modern") == ''
    assert slugify('   ', algorithm="modern") == ''
    assert slugify('!!!', algorithm="modern") == ''
