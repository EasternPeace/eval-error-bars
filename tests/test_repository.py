"""Checks that only make sense in this repository, not in the cookbook copy of the recipe."""

import base64
import sys
from pathlib import Path

import nbformat
import pytest

ROOT = Path(__file__).resolve().parent.parent
RECIPE = ROOT / "evals/prompt_comparison_error_bars"
sys.path.insert(0, str(RECIPE / "tests"))
sys.path.insert(0, str(RECIPE))

from test_reported_numbers import headline_figures  # noqa: E402

README = " ".join((ROOT / "README.md").read_text().split())


@pytest.mark.parametrize("figure", headline_figures())
def test_repository_readme_quotes_the_recorded_results(figure: str) -> None:
    assert figure in README


def test_readme_chart_is_the_one_the_notebook_drew() -> None:
    notebook = nbformat.read(RECIPE / "guide.ipynb", as_version=4)
    drawn = [
        base64.b64decode(output.data["image/png"])
        for cell in notebook.cells
        if cell.cell_type == "code"
        for output in cell.outputs
        if "image/png" in output.get("data", {})
    ]
    assert drawn == [(ROOT / "assets" / "two_changes.png").read_bytes()]
