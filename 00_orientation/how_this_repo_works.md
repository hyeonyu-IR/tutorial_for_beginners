# How This Repository Works (Radiology‑Friendly Overview)

**Audience:** Radiology residents, fellows, and faculty

This repository is designed to help you use **Git** safely across **home** and **UNC workstation** environments, especially for R‑based analysis, figures, and teaching materials.

---

## Mental Model (Clinical Analogy)

- **GitHub** is like **PACS** (authoritative archive).
- Your **home** and **work** PCs are like **reading room workstations**.
- **`git pull`** = load the latest study before you read.
- **`git push`** = archive your approved changes so others (or your other PC) see them.

> If you remember one rule: **Pull before you start; push when you finish.**

---

## Repository Layout (What Lives Where)

```
./
├── README.md                 # Radiology‑focused overview (start here)
├── git/
│   └── GIT_BRANCHING_GUIDE.md  # Main vs branches explained simply
│
├── 00_orientation/
│   └── how_this_repo_works.md   # This file
│
├── 01_git_basics/
│   ├── essential_commands.md    # Minimal daily Git commands
│   └── git_cheat_sheet.md       # (Optional) one‑pager
│
├── 02_multi_pc_workflow/
│   ├── home_vs_work.md
│   ├── switching_machines.md
│   └── conflict_resolution.md
│
├── 03_ssh_setup/
│   └── ssh_step_by_step.md
│
├── 04_r_basics/
│   ├── r_project_structure.md
│   └── examples/
│       └── basic_analysis.R
└── .gitignore
```

**Why numbered folders?** They provide a linear path for learners and make it obvious what to do next.

---

## Home vs Work (Safe Daily Loop)

1. **Start of session** (any machine):
   ```bash
   git pull
   git status
   ```
2. **Work**: edit R scripts, README, figures, markdown.
3. **Save your progress**:
   ```bash
   git add .
   git commit -m "Brief clinical/analytic description"
   git push
   ```

> Avoid editing the **same file** on two machines at once without pushing/pulling in between.

---

## Branching (Optional but Useful)

- Keep `main` as the **trusted teaching version**.
- Create a branch for large or risky edits, then merge when satisfied.
- See: `git/GIT_BRANCHING_GUIDE.md`.

---

## SSH (Highly Recommended)

- Eliminates repeated password prompts.
- Works well behind institutional firewalls.
- Follow: `03_ssh_setup/ssh_step_by_step.md`.

---

## Troubleshooting

- **"Access is denied" (Windows deletion)**: close apps (VS Code/RStudio), then remove via elevated PowerShell.
- **Merge conflict**: open the file, choose the correct lines, remove conflict markers, then `git add` and `git commit`.
- **Unsure where you are**: `git status` and `git branch` tell you your state.

---

## Success Criteria for Learners

- You can move between **home** and **work** PCs without losing changes.
- Your repo history shows clear, small commits with meaningful messages.
- You can set up SSH and push/pull without passwords.

> *Git is not about perfection; it’s about not losing work.*
