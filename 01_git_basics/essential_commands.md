# Essential Git Commands (Radiology‑Safe Minimal Set)

These are the **only commands** most learners need day‑to‑day.

---

## 0) Configure (one‑time per machine)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
(Use your GitHub email for best results.)

---

## 1) Get the Latest Before You Start
```bash
git pull
```
Pulls the newest changes from GitHub to your computer.

---

## 2) See What Changed
```bash
git status
```
Shows new/modified files and your current branch.

Optional detailed view:
```bash
git diff
```

---

## 3) Save Your Work Locally (Stage → Commit)
```bash
git add .
git commit -m "Clear, short message in plain English"
```
**Message tips:** What did you change? Why? (e.g., "Update IR outcomes figure caption")

---

## 4) Publish to GitHub
```bash
git push
```
Uploads your commit so your other PC (or collaborators) can pull it.

---

## 5) Switch Branches (Optional)
```bash
git checkout -b my-change     # create & switch to new branch
# ...work...
git checkout main              # return to main
```

Merge when ready:
```bash
git checkout main
git pull
git merge my-change
git push
```

Delete a finished local branch:
```bash
git branch -d my-change
```

---

## 6) Fix Common Issues Quickly

**Accidentally modified a file—discard local edits** (if not needed):
```bash
git checkout -- path/to/file
```

**Reset your entire local copy to match GitHub's main** (⚠️ deletes local uncommitted changes):
```bash
git checkout main
git reset --hard origin/main
```

**See where you are and what remote is configured:**
```bash
git branch
git remote -v
```

---

## 7) Daily Pattern to Memorize
```bash
git pull
# work
git add .
git commit -m "Meaningful message"
git push
```

That’s it. Repeat on home and work machines.
