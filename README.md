# DB-Cross-Ref

Database breach cross-reference tool

## About

DB-Cross-Ref is a Python script that checks if the emails found in `file A` also exist in `file B`.
<br>
| File | Usage                            |
| ---- | -------------------------------- |
| A    | File containing emails to check  |
| B    | File to check the emails against |
<br>
Note that this relies on both files to have a maximum of one email per new line.
<br>
References to `Spotify-Account1.txt` and `000webhost.com.txt` already in the script are legitimate and left in as an example of how it should be used. The second file would be much larger than the first.

## Disclaimer

This is for educational and research purposes only. I am not responsible for misuse or damage caused by the program. 

## Prerequisites

- Python 3

## Setup

Edit the 'dumpa' and 'dumpb' variable values.
<br>
```
dumpa = file A
dumpb = file B
```
<br>
For the differences, refer to the table in the `about` section of this file.

## Known issues

- If there is a duplicate email then it will count as an `invalid account`.