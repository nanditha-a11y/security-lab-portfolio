# OverTheWire Bandit — Level 1 → Level 2

## Level Goal

The password for the next level is stored in a file called `-` in the home directory.

## Commands Used

`ls`

`cat ./-`

## Steps

1. Logged into the Bandit Level 1 account.
2. Used `ls` to list the files in the home directory.
3. Found a file named `-`.
4. `cat -` cannot be used normally because `-` has a special meaning in many Linux commands.
5. Used `cat ./-` to explicitly specify that `-` is a file in the current directory.
6. The command displayed the password for `bandit2`.

## What I Learned

- Linux commands can give special meanings to characters such as `-`.
- `./` can be used to explicitly refer to a file in the current directory.
- A filename beginning with or consisting of `-` can cause problems with command-line tools.
- Understanding how Linux interprets command arguments is important when working with files.

## SSH to the Next Level

`ssh bandit2@bandit.labs.overthewire.org -p 2220`

## Security Relevance

Understanding command-line argument handling is useful in cybersecurity because unusual filenames and special characters can affect how commands are interpreted. Correctly handling them is important when analysing files and working safely in Linux environments.

## Evidence

A screenshot showing the solution is included with this write-up. The password has been hidden.
