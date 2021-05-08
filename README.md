# rearrange_logs

You are given a few log files which contains logs from three API calls.

log format: time date function_name parameters

Example lines:

12:03:24 08/12/2020 Get id:1234 name:apple

12:05:24 08/12/2020 Set id:1236 price:12

12:05:24 08/12/2020 Add id:1239 name:orange price:12 location:wa

...
 
Your task is to rearrange all logs by creating new three new logs, namely get_log, set_log, and add_log where they store logs for Get, Set, Add calls respectively. After that, you will also need to create a log named stats_log where it shows the total calls for each function per day.
Example lines:

Get

08/12/2020 13

08/13/2020 34

...

Set

08/12/2020 23

08/13/2020 54

...

Add

08/12/2020 21

08/13/2020 55

...
 
input: a list of log filenames (e.g. ['log1', 'log2', ...])

output: three new log files: get_log, set_log, add_log, stats_log
