# OverTheWire Bandit — Level 4 → Level 5

## Level Goal

The password for the next level is stored in the only human-readable file in the `inhere` directory.

## Commands Used

`cd inhere`

`ls`

`file ./-*`

`cat ./-filename`

## Steps

1. Logged into the Bandit Level 4 account.
2. Entered the `inhere` directory using `cd inhere`.
3. Used `ls` to view the files in the directory.
4. Used the `file` command to determine the type of each file.
5. Identified the only file containing human-readable text.
6. Used `cat` to display the contents of that file.
7. The output was the password for `bandit5`.

## What I Learned

- The `file` command can identify the type and contents of a file.
- File extensions are not always reliable indicators of file type in Linux.
- `ASCII text` indicates that a file contains readable text.
- `./` can be used to explicitly refer to files in the current directory.
- The `file` command is useful when many files need to be examined.

## SSH to the Next Level

`ssh bandit5@bandit.labs.overthewire.org -p 2220`

## Security Relevance

Being able to identify and inspect unknown files is useful during cybersecurity investigations. Security analysts may encounter files with misleading names or extensions and need to determine their actual contents and type.

## Evidence

A screenshot showing the `file` command and the identified human-readable file is included with this write-up. The password has been hidden.
