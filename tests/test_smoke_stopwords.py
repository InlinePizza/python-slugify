"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_stopwords() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('the quick brown fox', algorithm="modern", stopwords=['the', 'brown']) == 'quick-fox'
    assert slugify('THE fox', algorithm="modern", stopwords=['the']) == 'fox'
