# Conflict Resolution (Minimal, Calm)

Conflicts happen when the **same lines** changed in two places.

---

## How to Resolve

1) Open the conflicted file and look for markers:
```
<<<<<<< HEAD
content from your current branch
=======
content from incoming changes
>>>>>>> origin/main (or branch name)
```
2) Choose/merge the correct lines and **delete the markers**
3) Save the file
4) Mark resolved and commit:
```bash
git add <file>
git commit -m "Resolve conflict in <file>"
```

---

## Tips
- Read the surrounding context—keep the final text clinically accurate
- If unsure, create a **backup** of the file before editing markers
- Use an editor with Git integration (VS Code, RStudio) to ease merges
