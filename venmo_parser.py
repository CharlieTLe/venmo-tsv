import json
import argparse
import requests

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-token', required=True, help='token')
parser.add_argument('-after', required=True, help='transactions to look after, format=yyyy-mm-dd')
parser.add_argument('-limit', default=100, help='how many transactions to fetch')
parser.add_argument('-receiver', required=True, help='filter for who should be on the receiving end of the transaction')


args = parser.parse_args()
payments_url = "https://api.venmo.com/v1/payments?access_token={}&after={}&limit={}".format(args.token, args.after, args.limit)
r = requests.get(payments_url)
if r.status_code == 200:
	print "Date Created\tFirst Name\tLast Name\tAmount\tNote"
	for payment in r.json()['data']:
		actor = payment['actor']
		if payment['target']['user']['username'] == args.receiver:
			fmt = "{}\t{}\t{}\t{}\t{}\t"
			print fmt.format(payment['date_created'],
							actor['first_name'],
							actor['last_name'],
							payment['amount'],
							payment['note'].replace('\n', ' ').encode('utf8'))
else:
	print "Error fetching payload ({})".format(r.status_code)
