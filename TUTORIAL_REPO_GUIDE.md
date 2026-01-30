# Tutorial Repository: Git & R for Beginners

**Audience:** Learners, trainees, and researchers new to Git (Home vs Work setup), with a focus on academic and data‑science workflows (R).

This repository is designed to be **learner‑ready**: predictable structure, step‑by‑step tutorials, and safe workflows suitable for home and institutional (e.g., UNC) machines.

---

## Learning Goals

By the end of this tutorial, learners will be able to:

- Understand GitHub as a central hub with multiple local clones
- Use Git safely across **home and work PCs**
- Perform daily `pull → work → commit → push` workflows
- Resolve simple merge conflicts
- Set up **SSH authentication** for GitHub (recommended)

---

## Recommended Repository Structure (Polished & Learner‑Ready)

```
tutorial_for_beginners/
├── README.md                  # Start here (overview + setup)
├── 00_orientation/
│   └── how_this_repo_works.md
│
├── 01_git_basics/
│   ├── git_concepts.md        # What is Git? GitHub? Repo? Clone?
│   ├── essential_commands.md  # add / commit / push / pull
│   └── git_cheat_sheet.md
│
├── 02_multi_pc_workflow/
│   ├── home_vs_work.md        # Home vs UNC workstation workflow
│   ├── switching_machines.md
│   └── conflict_resolution.md
│
├── 03_ssh_setup/
│   └── ssh_step_by_step.md    # SSH keys tutorial (mirrors below)
│
├── 04_r_basics/
│   ├── r_project_structure.md
│   ├── r_stats_cheat_sheet.md
│   └── examples/
│       └── basic_analysis.R
│
├── figures/                   # Diagrams used in tutorials
├── data/                      # (gitignored in real projects)
├── .gitignore
└── LICENSE
```

**Design principles:**
- Numbered folders = learning path
- Markdown files = readable in browser
- No prior Git knowledge assumed

---

## Suggested Learning Path for Students

1. **Orientation** → `00_orientation/`
2. **Git fundamentals** → `01_git_basics/`
3. **Home vs work workflow** → `02_multi_pc_workflow/`
4. **SSH setup (recommended)** → `03_ssh_setup/`
5. **R + Git integration** → `04_r_basics/`

---

## Clean Daily Git Workflow (Recap)

### Before working (any machine)
```bash
git pull
git status
```

### After working
```bash
git add .
git commit -m "Describe what you changed"
git push
```

> **Rule:** GitHub is the hub. Every computer is disposable.

---

## Step‑by‑Step: SSH Key Setup for GitHub (Highly Recommended)

SSH avoids repeated passwords and works well across firewalls and institutional systems.

The steps below apply to **each machine** (Home PC and Work PC).

> **Windows note:** Use **PowerShell** or **Git Bash**. On macOS/Linux, use Terminal.

### Step 1: Check for Existing SSH Keys

```bash
ls ~/.ssh
```

If you see files like `id_ed25519` and `id_ed25519.pub`, you may already have a key.

---

### Step 2: Generate a New SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When prompted:
- **File location:** Press **Enter** (default is recommended)
- **Passphrase:** Optional but encouraged (especially on laptops)

✅ Creates:
- Private key: `~/.ssh/id_ed25519`
- Public key: `~/.ssh/id_ed25519.pub`

---

### Step 3: Start the SSH Agent

**Windows (PowerShell):**
```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE/.ssh/id_ed25519
```

**macOS/Linux:**
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

### Step 4: Copy the Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy **the entire line** (starts with `ssh-ed25519`).

---

### Step 5: Add SSH Key to GitHub

1. Go to **GitHub → Settings → SSH and GPG keys**
2. Click **New SSH key**
3. Title examples:
   - `Home PC`
   - `UNC Workstation`
4. Paste the public key
5. Save

---

### Step 6: Test the Connection

```bash
ssh -T git@github.com
```

Expected message:
```
Hi <username>! You've successfully authenticated.
```

---

### Step 7: Switch Repository to SSH (If Needed)

Inside your repo:
```bash
git remote -v
```

If it shows HTTPS, update it:
```bash
git remote set-url origin git@github.com:<username>/tutorial_for_beginners.git
```

✅ From now on: no passwords required.

---

## Common SSH Pitfalls (Quick Fixes)

- **Permission denied (publickey)** → key not added to GitHub or agent not running
- **Agent has no identities** → run `ssh-add ~/.ssh/id_ed25519`
- **Multiple GitHub accounts** → use one key per account
- **Institutional machine** → SSH usually works better than HTTPS

---

## Optional: Starter `.gitignore` for R/Data Projects

Create a file named `.gitignore` with the following:

```
# R/RStudio
.Rhistory
.Rproj.user/
.RData
.Ruserdata
.Rproj

# Data and outputs (adjust as needed)
data/
*.csv
*.tsv
*.rds
*.sav
*.xlsx

# OS / editor cruft
.DS_Store
Thumbs.db
*.tmp
```

> Adjust `data/` and file patterns if you intend to version small sample datasets.

---

## What to Do Next

- Save this file as `README.md` in the root of your repo **or** as `TUTORIAL_REPO_GUIDE.md` and link it from `README.md`.
- Create the folder structure above (you can start minimal and expand).
- Commit and push:

```bash
git add .
git commit -m "Add learner-ready tutorial structure and SSH setup guide"
git push
```

---

*Maintained by: Hyeon Yu, MD, Clinical Professor of Radiology (IR), UNC.*
