# SSH Setup (Windows/macOS/Linux) for GitHub

**Why:** Password‑free, reliable authentication across home and institutional networks.

> Perform these steps **on each machine** (Home PC and UNC workstation).

---

## 1) Check for existing keys
```bash
ls ~/.ssh
```
Look for `id_ed25519` and `id_ed25519.pub`.

---

## 2) Generate a key (recommended: ed25519)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
- Press **Enter** to accept the default location
- Optional passphrase (recommended on laptops)

---

## 3) Start the SSH agent and add your key

**Windows PowerShell:**
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

## 4) Add the public key to GitHub
```bash
cat ~/.ssh/id_ed25519.pub
```
- Copy the entire line (starts with `ssh-ed25519`)
- GitHub → **Settings → SSH and GPG keys → New SSH key** → paste → **Save**

---

## 5) Test the connection
```bash
ssh -T git@github.com
```
Expected: greeting with your username.

---

## 6) Switch your repo to SSH (if currently HTTPS)
```bash
git remote -v
# If https:// is shown, set SSH URL:
git remote set-url origin git@github.com:<username>/tutorial_for_beginners.git
```

---

## Troubleshooting
- **Permission denied (publickey)** → key not added to GitHub or agent not running
- **Agent has no identities** → `ssh-add ~/.ssh/id_ed25519`
- **Multiple GitHub accounts** → one key per account
- **Institutional firewalls** → SSH is typically more reliable than HTTPS
