# Switching Machines Checklist

Use this checklist when moving between **home** and **UNC workstation**.

---

## Leaving a machine
```bash
git status      # confirm no untracked surprises
git add .
git commit -m "Wrap up <task>"
git push        # publish to GitHub
```

## Arriving at the other machine
```bash
git pull        # bring changes down first
git status
```

> If `git pull` reports conflicts, open the file(s) and resolve (see guide).

---

## Quick Health Checks

**Which branch am I on?**
```bash
git branch
```

**What remote is configured?**
```bash
git remote -v
```

**What changed recently?**
```bash
git log --oneline -n 10
```
