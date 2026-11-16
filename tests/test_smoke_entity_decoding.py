"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_entity_decoding() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('a&amp;b', algorithm="modern") == 'a-b'
    assert slugify('a&#32;b', algorithm="modern") == 'a-b'
