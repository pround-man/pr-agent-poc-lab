# PR-Agent PoC Lab

This repository is a small lab for testing PR-Agent on GitHub pull requests.

The first experiment adds a discount calculation module with intentionally
imperfect logic, so PR-Agent can review a realistic diff and produce feedback.

## Experiment Goals

- Verify that PR-Agent can run through GitHub Actions.
- Verify that DeepSeek can be used as the backing model.
- Check whether the review finds boundary, business-rule, precision, and test gaps.
- Record the review quality, false positives, latency, and API cost.

## Manual Commands To Try In A Pull Request

```text
/review
/improve
```
