# Home vs Work PC Workflow (Radiology‑Safe)

**Goal:** Keep a clean, synchronized repo between your **home PC** and **UNC workstation** without conflicts.

---

## Golden Loop

1) **Before work (any machine)**
```bash
git pull
git status
```
2) **Do your work** (R scripts, figures, Markdown)
3) **Save & publish**
```bash
git add .
git commit -m "<concise clinical/analytic change>"
git push
```

> Tip: If you switch machines in the same day, run `git pull` immediately on the other machine before editing.

---

## Common Scenarios

### A) Added files at home; continue at work
- Home: commit & `git push`
- Work: `git pull` → continue

### B) Edited the same file on both machines
- Work: try `git pull`
- If conflict: open the file and resolve (see **Conflict Resolution**), then `git add` + `git commit`

### C) Unsure what changed on the other machine
```bash
git fetch
git log --oneline --graph --decorate --all | head -n 20
```

---

## Do / Don’t

**Do**
- Pull before starting
- Commit small, logical chunks
- Write clear messages

**Don’t**
- Edit the same file on two machines without syncing
- Panic on conflicts—resolve calmly (see below)
