# DB-Cross-Ref

<img src="banner.png" alt="Banner with logo">

## About

DB-Cross-Ref is a Python script that checks if the emails found in `file A` also exist in `file B`.

| File | Usage                            |
| ---- | -------------------------------- |
| A    | File containing emails to check  |
| B    | File to check the emails against |

Note that this relies on both files to have a maximum of one email per new line.
<br>
References to `Spotify-Account1.txt` and `000webhost.com.txt` already in the script are legitimate and left in as an example.

The sort of counts that is returned:
- Matched emails
- Matched duplicate emails
- Mismatched emails
- Mismatched duplicate emails

## Disclaimer

This is for educational and research purposes only. I am not responsible for misuse or damage caused by the involvement of this program. 

## Prerequisites

- Python 3

## Setup

Edit the `dumpa` and `dumpb` variable values with the name of the files you wish to utilise.
<br>
For example:
<br>
```
dumpa = 'file_a.txt'
dumpb = 'file_b.txt'
```
