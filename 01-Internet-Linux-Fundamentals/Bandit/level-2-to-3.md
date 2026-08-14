# OverTheWire Bandit — Level 2 → Level 3

## Level Goal

The password for the next level is stored in a file called `--spaces in this filename--` in the home directory.

## Commands Used

`ls`

`cat "./--spaces in this filename--"`

## Steps

1. Logged into the Bandit Level 2 account.
2. Used `ls` to list the files in the home directory.
3. Found a filename containing multiple spaces.
4. Quoted the filename so that the shell treats the entire filename as one argument.
5. Used `cat` to display the contents of the file.
6. The output was the password for `bandit3`.

## What I Learned

- Spaces normally separate arguments in the Linux shell.
- A filename containing spaces should be quoted or otherwise escaped when used in commands.
- Double quotes can preserve spaces within a filename.
- The shell processes command arguments before the command itself receives them.

## SSH to the Next Level

`ssh bandit3@bandit.labs.overthewire.org -p 2220`

## Security Relevance

Understanding how the shell interprets filenames and command arguments is important when working with Linux systems. Incorrect handling of special filenames can cause commands to behave unexpectedly.

## Evidence

A screenshot showing the solution is included with this write-up. The password has been hidden.
