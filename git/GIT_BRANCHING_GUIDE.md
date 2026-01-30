# Main vs Branches in Git: A Practical Guide for Your Tutorial Repo

**Author:** Hyeon Yu (Clinical Professor of Radiology, IR)  
**Use case:** Solo or small‑team academic workflows across **Home** and **UNC workstation** clones.

---

## 1) The One‑Sentence Definition

> **A branch is an alternate timeline of your project.**

- `main` = the trusted, shareable timeline (what learners see)
- other branches = safe places to experiment without touching `main`

---

## 2) What `main` Means

`main` is the **default branch** and the version you want others to rely on:
- ✅ stable
- ✅ ready to teach from
- ✅ what GitHub shows by default

> **Rule of thumb:** If you’d present it in a lecture, it belongs on `main`.

---

## 3) What a Branch Is (Exactly)

A branch is just a **pointer** that moves as you commit. It lets you diverge from `main` and work independently.

```
main:      A──B──C──D
                 \
feature-x:         E──F
```

- Commits `E` and `F` exist on `feature-x`
- `main` stays at `D` until you merge

No overwriting, no danger—just parallel timelines.

---

## 4) Why Branches Exist (Real Benefits)

1. **Safe experimentation**  
   Try big changes (restructure notes, reorganize modules). If you like it, merge; if not, delete the branch.

2. **Parallel work** (even for a solo researcher)  
   Park one idea on a branch, continue another, return later.

3. **Collaboration**  
   Multiple people can contribute without stepping on each other, then integrate when ready.

---

## 5) What Does `origin` Mean?

`origin` is just a **nickname** for the GitHub remote repository.

- `main` → your **local** main branch
- `origin/main` → the **GitHub** copy of main
- `experiment` → your local branch
- `origin/experiment` → that branch on GitHub

---

## 6) Why `git push` Sometimes Says `origin main` and Sometimes a Branch

- If you are **on `main`** and run `git push`, you push `main` to `origin/main`.
- If you are **on `feature-x`** and run `git push`, you push `feature-x` to `origin/feature-x`.

> You can only push the branch you are **currently on**. Check with:
```bash
git branch
```
The `*` marks the current branch.

---

## 7) Minimal, Safe Branching Strategy (Tailored for You)

### Strategy A — **Main‑Only** (perfectly acceptable)
If your changes are incremental and low‑risk, you can ignore branching:
```bash
git pull
# do work
git add .
git commit -m "Clarify SSH steps in README"
git push
```

### Strategy B — **Occasional Safe Branch** (recommended for bigger edits)
Use a branch when trying something large or potentially disruptive.
```bash
# create and switch to a branch
git checkout -b restructure-tutorial

# do work and commit as usual
git add .
git commit -m "Reorganize modules and update navigation"

# bring main up-to-date from GitHub before merging
git checkout main
git pull

# merge the branch into main
git merge restructure-tutorial

# publish
git push

# optional: delete the branch locally when done
git branch -d restructure-tutorial
```

If you decide the experiment wasn’t good:
```bash
git checkout main
git branch -D restructure-tutorial   # force delete the experimental branch
```

---

## 8) Typical Solo Flow with a Temporary Branch

```bash
# start on main
git pull

# branch for a contained task
git checkout -b add-conflict-resolution-module

# work and commit in small logical steps
git add 02_multi_pc_workflow/conflict_resolution.md
git commit -m "Add minimal conflict resolution walkthrough"

# finish the task, then integrate
git checkout main
git pull
git merge add-conflict-resolution-module

# publish and clean up
git push
git branch -d add-conflict-resolution-module
```

---

## 9) How Merging Works (Fast‑Forward vs Merge Commit)

- **Fast‑forward**: if `main` hasn’t moved, Git just advances `main` to the branch tip (no extra commit).
- **Merge commit**: if both moved, Git creates a new commit tying histories together.

You don’t need to micromanage this—`git merge` chooses appropriately.

---

## 10) What If There’s a Conflict?

Git will mark the file with conflict markers:
```
<<<<<<< HEAD
content from main
=======
content from your branch
>>>>>>> branch-name
```
Resolve by choosing/combining the right lines, deleting the markers, then:
```bash
git add <file>
git commit -m "Resolve merge conflict in <file>"
```

> Conflicts are normal—they mean Git needs your judgment.

---

## 11) Naming and Conventions (Keep It Simple)

- Keep branch names short and descriptive: `restructure-tutorial`, `update-ssh-guide`, `figures-cleanup`
- One task per branch
- Merge or delete branches when done to keep history clean

---

## 12) Quick Reference (Copy/Paste)

**Create and switch to a new branch**
```bash
git checkout -b my-idea
```

**Switch back to main**
```bash
git checkout main
```

**Update your local main from GitHub**
```bash
git pull
```

**Merge a finished branch into main**
```bash
git checkout main
git pull
git merge my-idea
git push
```

**Delete a merged branch (local)**
```bash
git branch -d my-idea
```

**Publish your current branch for the first time**
```bash
git push -u origin my-idea
```
(After the first time, `git push` is enough.)

---

## 13) FAQ

**Q: Do I need branches if I’m the only person using this repo?**  
A: Not strictly. Branches become valuable when you attempt bigger edits or want a safety net.

**Q: Why does GitHub show a “Compare & pull request” banner after I push a branch?**  
A: GitHub detected a branch on the remote. A Pull Request (PR) is just a formal way to merge branches with review. For solo work, you can merge locally or create a PR for history and comments.

**Q: Can I work on two branches at once on two different PCs?**  
A: Yes, but keep discipline: **`pull` before you start, `push` when you’re done**, and avoid editing the same files on different branches simultaneously.

---

## 14) Where to Place This File in Your Repo

Suggested path (matches your request):
```
./git/GIT_BRANCHING_GUIDE.md
```
Then link it from your `README.md` for learners:
```markdown
See [Main vs Branches: A Practical Guide](git/GIT_BRANCHING_GUIDE.md) for when and how to branch.
```

---

## 15) Mental Model to Remember

> **`main` is what you trust. Branches are where you think.**

Keep `main` clean for teaching; think freely on branches.
