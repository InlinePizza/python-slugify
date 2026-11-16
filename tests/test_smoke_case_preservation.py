"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_case_preservation() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('Hello WORLD', algorithm="modern", lowercase=False) == 'Hello-WORLD'
    assert slugify('Hello WORLD', algorithm="modern") == 'hello-world'
