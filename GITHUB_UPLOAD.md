# Uploading ComponentLife Engine to GitHub

## Option 1 — GitHub website

1. Create a new repository named `componentlife-engine`.
2. Choose **Public** only if you are comfortable exposing the demonstration code under the repository's proprietary evaluation licence; otherwise choose **Private**.
3. Do not add a GitHub-generated README or licence because this package already contains both.
4. Extract `componentlife-engine-v0.1-github-ready.zip`.
5. Upload the contents of the `componentlife-engine/` folder to the repository root.
6. Commit the files.
7. Open **Actions** and confirm the test workflow passes.

## Option 2 — Git command line

```bash
git init
git branch -M main
git add .
git commit -m "Initial ComponentLife Engine v0.1 proof of concept"
git remote add origin https://github.com/YOUR-USERNAME/componentlife-engine.git
git push -u origin main
```

## Before making the repository public

Review `NOTICE.md`, `LICENSE`, and `SECURITY.md`. Do not add real customer data, validated production thresholds, proprietary field-outcome data, production model weights, or confidential adaptive-test rules.
