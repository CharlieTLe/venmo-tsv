#Usage
`python venmo_parser.py -token ACCESS_TOKEN -after 2016-01-07 -receiver USERNAME`

The following command requests using the Venmo API to receive a JSON output of
transactions since the `after` date to the `receiver`.

```
Date Created    First Name      Last Name       Amount  Note
2016-06-18T04:30:36     Charlie Le      88.0    Airbnb reimbursement
2016-06-18T04:27:15     Charlie Le      88.0    Accidentally used card to pay for Airbnb stay
2016-05-28T03:43:40     Rick Astley			35.0    Bash
2016-05-28T03:20:05     Air Goh 				35.0    Shit
2016-05-27T01:55:13     Bob Joe					30.0    for le fin
.
.
.
```
