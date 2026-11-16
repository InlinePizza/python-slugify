"""Regression coverage for existing modern slug behavior."""

from slugify import slugify


def test_unicode_normalization() -> None:
    """Preserve the existing outputs for representative inputs."""
    assert slugify('Ｃａｆｅ', algorithm="modern", allow_unicode=True) == 'cafe'
    assert slugify('影師嗎', algorithm="modern", allow_unicode=True) == '影師嗎'
