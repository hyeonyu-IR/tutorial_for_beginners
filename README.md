# Git & R Tutorial for Radiology Trainees and Faculty

**Audience:** Radiology residents, fellows, clinical faculty, and research staff  
**Focus:** Safe, practical Git workflows for academic radiology projects (R, imaging research, teaching materials)

---

## Why This Repository Exists

Radiology projects increasingly involve:
- Data analysis in **R / Python**
- Collaborative manuscript and figure development
- Multi‑computer workflows (home laptop ↔ institutional workstation)
- Longitudinal teaching and quality‑improvement materials

Yet many radiologists are *not formally trained* in version control.

This repository provides a **low‑risk, clinically realistic introduction to Git**—structured for busy clinicians who want reproducibility without unnecessary technical burden.

---

## What You Will Learn

After completing this tutorial, learners will be able to:

- Understand Git and GitHub using **medical‑friendly mental models**
- Work safely across **home and hospital/UNC workstations**
- Avoid common pitfalls such as lost files or overwritten analyses
- Track changes in:
  - R scripts
  - Teaching slides
  - Figure generation code
  - Manuscript drafts (Markdown / LaTeX)
- Use Git as a **personal safety net**, not just a collaboration tool

---

## Core Clinical Analogy

> **Think of GitHub as the PACS archive, and each computer as a reading room workstation.**

- GitHub = authoritative archive
- Home PC / Work PC = local viewers/editors
- `git pull` = sync latest study
- `git push` = archive approved changes

Nothing is lost, and history is preserved.

---

## Repository Structure (Teaching‑Oriented)

```
tutorial_for_beginners/
├── README.md                  # You are here
├── git/
│   └── GIT_BRANCHING_GUIDE.md # Main vs branches explained
│
├── 00_orientation/
│   └── how_this_repo_works.md
│
├── 01_git_basics/
│   ├── git_concepts.md
│   ├── essential_commands.md
│   └── git_cheat_sheet.md
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
│
├── figures/
├── data/            # typically gitignored
└── .gitignore
```

---

## Suggested Learning Path for Radiology Trainees

1. **Orientation** – how Git fits into radiology research workflows  
2. **Git basics** – minimal command set for daily use  
3. **Home vs Work PC workflow** – the most common real‑world problem  
4. **SSH authentication** – password‑free and firewall‑friendly  
5. **R integration** – reproducible analysis structure

> Learners can stop after Step 3 and still work safely.

---

## Recommended Daily Workflow (Clinical‑Safe)

Before starting work on **any machine**:
```bash
git pull
git status
```

After finishing work:
```bash
git add .
git commit -m "Describe the clinical or analytic change"
git push
```

**Rule:** Never begin work without `git pull`, especially when switching locations.

---

## About Branching (Do I Really Need It?)

- **No**, for small incremental edits.
- **Yes**, when:
  - Reorganizing teaching materials
  - Refactoring analysis code
  - Attempting a risky or conceptual rewrite

A dedicated guide is available here:
```
git/GIT_BRANCHING_GUIDE.md
```

> **`main` = what you are comfortable teaching or sharing**

---

## What This Repo Is *Not*

This is **not**:
- A software engineering curriculum
- A DevOps or CI/CD tutorial
- A replacement for statistical or imaging education

It *is*:
- A practical safety framework
- A reproducibility tool
- A confidence‑builder for academic radiologists

---

## Intended Use Cases

- Resident or fellow research projects
- QI initiatives requiring traceable edits
- Educational content development
- Multi‑site or multi‑device collaboration
- Personal academic portfolios

---

## Maintainer

**Hyeon Yu, MD**  
Clinical Professor of Radiology,
Vascular and Interventional Radiology  
University of North Carolina at Chapel Hill  

This repository is maintained with an emphasis on **clarity, safety, and clinical realism**.

---

## Getting Started

1. Clone the repository
2. Read `00_orientation/how_this_repo_works.md`
3. Complete `01_git_basics/essential_commands.md`
4. Set up SSH using `03_ssh_setup/ssh_step_by_step.md`

No prior Git experience is assumed.

---

> *Git is not about perfection. It is about not losing work.*
