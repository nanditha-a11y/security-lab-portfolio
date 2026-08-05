# OverTheWire Bandit — Level 0 → Level 1

## Level Goal

The password for the next level is stored in a file called `readme` in the home directory.

The password is used to log into `bandit1` using SSH on port `2220`.

## Commands Used

`ls`

`cat readme`

## Steps

1. Logged into the Bandit server as `bandit0`.
2. Used `ls` to list the files in the home directory.
3. Found a file called `readme`.
4. Used `cat readme` to display its contents.
5. The displayed value is the password for `bandit1`.
6. Used the password to log into the next level using SSH.

## What I Learned

- `ls` lists files and directories.
- `cat` displays the contents of a file.
- Files in Linux can be accessed from the command line.
- Bandit passwords need to be saved separately because they are not automatically stored.

## SSH to the Next Level

`ssh bandit1@bandit.labs.overthewire.org -p 2220`

## Security Relevance

Command-line file access is an important Linux skill in cybersecurity. Attackers and defenders may need to locate and inspect files while investigating or managing a system.

## Evidence

A screenshot showing the commands used to solve this level is included with this write-up. The password has been hidden.
