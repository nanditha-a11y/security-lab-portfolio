# OverTheWire Bandit — Level 0

## Level Goal

The goal of Level 0 is to log into the Bandit game server using SSH.

## Connection Details

- Host: `bandit.labs.overthewire.org`
- Port: `2220`
- Username: `bandit0`
- Password: Provided by the Level 0 challenge

## Command Used

`ssh bandit0@bandit.labs.overthewire.org -p 2220`

## What I Did

I connected to the Bandit server using SSH on the non-standard port 2220.

After entering the provided credentials, I successfully logged into the remote Linux system.

The successful login displayed a prompt similar to:

`bandit0@bandit:~$`

## What I Learned

- SSH is used to securely connect to a remote computer.
- SSH normally uses port 22, but Bandit uses port 2220.
- The `-p` option specifies a different SSH port.
- The username identifies the account I am logging into.

## Cybersecurity Relevance

SSH is commonly used for remote administration of Linux systems. Understanding how SSH connections work is important for both system administration and cybersecurity.

## Evidence

A screenshot showing the successful Level 0 login is included with this write-up.
