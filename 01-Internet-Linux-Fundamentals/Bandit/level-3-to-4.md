# OverTheWire Bandit — Level 3 → Level 4

## Level Goal

The password for the next level is stored in a hidden file inside the `inhere` directory.

## Commands Used

`ls`

`cd inhere`

`ls -la`

`cat ...Hiding-From-You`

## Steps

1. Logged into the Bandit Level 3 account.
2. Used `ls` to view the contents of the home directory.
3. Found the `inhere` directory.
4. Used `cd inhere` to enter the directory.
5. Used `ls -la` to display hidden files.
6. Found the hidden file containing the password.
7. Used `cat` to read the file.
8. The output was the password for `bandit4`.

## What I Learned

- Files beginning with `.` are normally hidden in Linux.
- `ls` does not normally display hidden files.
- `ls -la` displays hidden files as well as detailed file information.
- `cd` is used to move between directories.
- `cat` can be used to read the contents of a file.

## SSH to the Next Level

`ssh bandit4@bandit.labs.overthewire.org -p 2220`

## Security Relevance

Hidden files can contain configuration files, credentials, or other information on Linux systems. Knowing how to locate hidden files is useful during system administration and security investigations.

## Evidence

A screenshot showing the solution is included with this write-up. The password has been hidden.
