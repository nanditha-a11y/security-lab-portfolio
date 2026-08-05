# Linux Basics — Part 2

## Topics Covered

- File permissions
- chmod
- chown
- Users and groups
- Pipes
- Input and output redirection

## File Permissions

Linux assigns permissions to files and directories for:

- User (owner)
- Group
- Others

The three basic permissions are:

- r — read
- w — write
- x — execute

Example:

`-rwxr-xr--`

This represents permissions for the owner, group, and others.

## chmod

`chmod` changes file permissions.

Example:

`chmod 777 file.txt`

The three numbers represent permissions for:

1. Owner
2. Group
3. Others

## chown

`chown` changes the owner of a file or directory.

Example:

`chown user file.txt`

## Users and Groups

Linux is a multi-user operating system.

Useful commands include:

`whoami`

Shows the current user.

`id`

Displays information about the current user and groups.

`cat /etc/passwd`

Displays information about user accounts.

`su`

Switches to another user.

`sudo`

Runs a command with elevated privileges.

## Pipes

The pipe `|` sends the output of one command as input to another command.

Example:

`ls | grep txt`

This can be used to filter the output of `ls`.

## Redirection

`>` redirects output to a file and replaces its contents.

Example:

`echo "Hello" > file.txt`

`>>` adds output to the end of a file.

Example:

`echo "World" >> file.txt`

`<` takes input from a file.

## What I Learned

I learned how Linux controls access to files using permissions and how users and groups affect access. I also learned how pipes and redirection allow commands to work together.

## Cybersecurity Relevance

Permissions, users, groups, and privilege management are important for protecting systems from unauthorized access and limiting what users and processes can do.
