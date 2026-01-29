# Git: From Zero to Confident Collaboration (with GitHub)
## A concise, practical reference for daily use.
### 1) One-time setup

```
# Install git (macOS: brew install git; Ubuntu: sudo apt-get install git)
git --version

# Identify yourself (global)
git config --global user.name "Your Name"
git config --global user.email "you@unc.edu"

# Optional: helpful defaults
git config --global init.defaultBranch main
git config --global pull.rebase false   # or true if you prefer a cleaner history
git config --global core.autocrlf input # mac/Linux; on Windows: true

# SSH (recommended for GitHub)
ssh-keygen -t ed25519 -C "you@unc.edu"
# Add the public key (~/.ssh/id_ed25519.pub) to GitHub > Settings > SSH keys
```
### 2) Start a repository
```
# New local repo
mkdir tutorial_for_beginners && cd $_
git init

# Add a README
echo "# Tutorial for Beginners" > README.md
git add README.md
git commit -m "Initialize repository with README"
```
Or clone an existing repo:
```
git clone git@github.com:<username>/tutorial_for_beginners.git
cd tutorial_for_beginners
```
### 3) Daily work: status -> add -> commit -> push
```
git status                # what's changed?
git add <file> ...        # stage changes
git commit -m "Meaningful summary: what & why"
git log --oneline --graph --decorate --all  # quick history
git push origin main
```
### 4) Branching and merging
```
# Create / switch
git switch -c feature/r-cheatsheet  # or: git checkout -b feature/r-cheatsheet
git switch main

# Merge feature into main
git switch main
git merge feature/r-cheatsheet

# Delete merged branch
git branch -d feature/r-cheatsheet
```
### 5) Sync with remote
```
git fetch origin                # updates remote tracking branches
git pull origin main            # fetch + merge into current branch
git push origin <branch>
```
### 6) Stash (quickly shelve WIP)
```
git stash push -m "WIP: partial work on X"
git stash list
git stash pop    # apply latest and drop
git stash apply  # apply but keep in stash
```
### 7) Undo / recover safely
```
git restore <file>                 # discard unstaged changes in file
git restore --staged <file>        # unstage

git commit --amend                 # fix last commit message or add files
git reset --soft HEAD~1            # move HEAD back 1, keep changes staged
git reset --mixed HEAD~1           # keep changes in working tree
git reset --hard HEAD~1            # ⚠️ discards changes

# Create a new commit that reverses a specific commit (safe for shared branches)
git revert <commit_sha>
```
### 8) Tags (versions)
```
git tag -a v1.0 -m "Initial version"
git push origin v1.0
git tag
```
### 9) Collaboration via GitHub Pull Requests
```
# Create branch locally
git switch -c fix/typo-readme
# edit files...
git add .
git commit -m "Fix typos in Git README"
git push -u origin fix/typo-readme

# Then open a Pull Request on GitHub comparing fix/typo-readme -> main
```
Review tips:
- Keep PRs small and focused.
- Use draft PRs for early feedback.
- Require at least one reviewer for main (GitHub branch protection).
### 10) Rebase (optional, advanced)
```
# Rebase your feature branch onto updated main
git switch feature/r-cheatsheet
git fetch origin
git rebase origin/main
# Resolve conflicts -> git add <fixed files> -> git rebase --continue
```
### 11) .gitignore for R & data science
create .gitignore in the repo root:
```# R / RStudio
.Rhistory
.Rproj.user/
.RData
.Ruserdata
.Rproj.user
.Rproj.user/*
*.Rproj

# Python (if any)
__pycache__/
*.py[cod]

# OS
.DS_Store
Thumbs.db

# Data / outputs
data/raw/
outputs/
*.html
*.pdf

# Quarto/Rmd caches
_cache/
*_cache/

# Virtual envs
.venv/
```
### 12) Large files & data
- Avoid committing PHI/PII or large raw datasets.
- Use Git LFS if you must track large non-sensitive binaries:
```
git lfs install
git lfs track "*.csv"
git add .gitattributes
git add <large files>
git commit -m "Track CSV via LFS"
git push origin main
```
### 13) Helpful aliases
```
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.st "status"
git config --global alias.lg "log --oneline --graph --decorate --all"
```
### 14) Bisect (find the bad commit)
```
git bisect start
git bisect bad                  # current is bad
git bisect good <good_sha>      # known good
# test, mark 'good' or 'bad' until found
git bisect reset
```