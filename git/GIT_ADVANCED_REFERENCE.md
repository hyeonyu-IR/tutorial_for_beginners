
# Advanced Git Reference (Optional)

This document is an **optional reference** for users who are already comfortable
with the core workflows taught in this repository.

❗ Beginners: Start with
- 00_orientation/how_this_repo_works.md
- 01_git_basics/essential_commands.md

> A concise, practical reference for daily use.

## 1) One-time setup

```bash
git --version

git config --global user.name "Your Name"
git config --global user.email "you@unc.edu"

git config --global init.defaultBranch main
git config --global pull.rebase false
# Windows line endings:
git config --global core.autocrlf true

# SSH (recommended)
ssh-keygen -t ed25519 -C "you@unc.edu"
```

## 2) Start a repository

```bash
mkdir tutorial_for_beginners && cd $_
git init

echo "# Tutorial for Beginners" > README.md
git add README.md
git commit -m "Initialize repository with README"
```

Or clone an existing repo:

```bash
git clone git@github.com:<username>/tutorial_for_beginners.git
cd tutorial_for_beginners
```

## 3) Daily work: status → add → commit → push

```bash
git status
git add <file> ...
git commit -m "Meaningful summary: what & why"
git log --oneline --graph --decorate --all
git push origin main
```

## 4) Branching and merging

```bash
git switch -c feature/r-cheatsheet
git switch main

git switch main
git merge feature/r-cheatsheet
git branch -d feature/r-cheatsheet
```

## 5) Sync with remote

```bash
git fetch origin
git pull origin main
git push origin <branch>
```

## 6) Stash

```bash
git stash push -m "WIP: partial work on X"
git stash list
git stash pop
```

## 7) Undo / recover safely

```bash
git restore <file>
git restore --staged <file>

git commit --amend
git reset --soft HEAD~1
# git reset --hard HEAD~1  # ⚠️ discards changes

git revert <commit_sha>
```

## 8) Tags

```bash
git tag -a v1.0 -m "Initial version"
git push origin v1.0
git tag
```

## 9) Collaboration via Pull Requests

```bash
git switch -c fix/typo-readme
git add .
git commit -m "Fix typos in Git README"
git push -u origin fix/typo-readme
```

## 10) Rebase (optional)

```bash
git switch feature/r-cheatsheet
git fetch origin
git rebase origin/main
# resolve conflicts → git add <files> → git rebase --continue
```

## 11) .gitignore for R & data science

See repo root `.gitignore` for a Windows-friendly setup.

## 12) Large files

```bash
git lfs install
git lfs track "*.csv"
```

## 13) Helpful aliases

```bash
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.st "status"
git config --global alias.lg "log --oneline --graph --decorate --all"
```

## 14) Bisect

```bash
git bisect start
git bisect bad
git bisect good <good_sha>
git bisect reset
```
