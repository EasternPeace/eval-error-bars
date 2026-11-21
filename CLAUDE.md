# CLAUDE.md

## What this project is
One Claude Cookbook recipe: "Is the new prompt actually better? Evals with error bars."
The reader changed a prompt, saw the eval score move a few points, and needs to know if that
is signal or noise. The recipe is built to be merged into anthropics/claude-cookbooks and to
stand alone as a portfolio piece.

Done means: a reader runs the notebook top to bottom and can reuse the method on their own
eval, and a cookbook maintainer can verify the pull request in minutes.

The recipe lives in `evals/prompt_comparison_error_bars/`, the same path it will have in the
cookbook, so the pull request is a plain copy of that folder.

## Ownership
You are the owner and long-term maintainer of this codebase. Structure, naming and design
are your decisions; consolidate duplication and fix what you find. In every final summary,
list each change you made, including small ones nobody asked for.

The local fork of anthropics/claude-cookbooks is someone else's code. There, change only
the recipe folder, registry.yaml and authors.yaml.

## Finishing work
Carry each task to the end. When an ordinary obstacle appears (a failing test, a timeout,
an empty result, a batch that has not finished), diagnose it and work through it. Report
open decisions with your recommendation and keep going on everything that does not depend
on the answer.

These steps need no approval: editing files in this repository, running tests, linters and
the notebook, local commits, read-only `gh` calls, and API runs inside the budget below.

Ask for approval before: pushing; creating a repository; opening or commenting on an issue
or pull request; an API run estimated above $3, or one that takes total spend past $20;
deleting recorded files under results/. Commit signing and other security settings are set
up by the user; give them the exact commands.

## GitHub account
This project belongs to the `EasternPeace` account. `gh` may have a different account
active, so pass the token for each call instead of switching accounts:
`GH_TOKEN=$(gh auth token --user EasternPeace) gh ...`

## Recipe standards
- Follow the upstream CONTRIBUTING.md and .claude/skills/cookbook-audit/style_guide.md.
  The hard gates: the notebook is committed after a fresh-kernel Run All, with outputs;
  a MODEL constant holding a current undated model ID; `anthropic.Anthropic()` with the key
  loaded from .env; no new dependencies beyond the cookbook's own.
- Every number in prose comes from committed files under results/. A test enforces this,
  so write the prose after the final run and report what the data shows, even if it is a
  smaller effect than hoped.
- Synthetic data only, with labels correct by construction.

## Verification
- `uv run ruff check . && uv run ruff format --check .`
- `uv run pytest` (offline; `-m live` calls the API)
- In the fork: `make test-notebooks NOTEBOOK=evals/prompt_comparison_error_bars/guide.ipynb`

## Communicating
Write reports for a reader who has not seen the work and wants to spend little time on it:
the outcome first, then what is left and what you need from them. Use the language the
user writes in.
