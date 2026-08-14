# Linux Basics — Part 3 + Bash

## Topics Covered

- Processes
- Process management
- ps
- kill
- top
- Cron jobs
- Bash scripting
- Variables
- if/else
- Loops

## Process Management

A process is a running instance of a program.

### ps

Displays information about running processes.

`ps`

A more detailed view can be obtained with:

`ps aux`

### top

Displays running processes and system resource usage in real time.

`top`

### kill

Terminates a process using its process ID (PID).

`kill PID`

## Cron Jobs

Cron is a Linux utility used to schedule commands or scripts to run automatically at specific times.

Cron jobs are useful for tasks such as:

- Backups
- System maintenance
- Automated scripts
- Scheduled monitoring

The command used to edit a user's scheduled cron jobs is:

`crontab -e`

## Bash

Bash is a command-line shell and scripting language commonly used on Linux.

Bash scripts can automate repetitive tasks and combine multiple commands.

## Variables

Variables store values that can be used later in a script.

Example:

`name="Linux"`

`echo $name`

## if/else

Conditional statements allow a script to make decisions.

Example:

`if [ "$name" = "Linux" ]; then echo "Correct"; else echo "Incorrect"; fi`

## Loops

Loops repeat commands multiple times.

Example:

`for i in 1 2 3; do echo $i; done`

## What I Learned

I learned how Linux manages running processes and how commands such as ps, top, and kill can be used to monitor and manage them. I also learned the basics of cron scheduling and Bash scripting.

## Cybersecurity Relevance

Process management and Bash scripting are important in cybersecurity for system monitoring, automation, log analysis, incident response, and security administration.
