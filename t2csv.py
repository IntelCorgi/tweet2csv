import os
import sys
import csv
import json
import tweepy
import argparse
from tweepy import API


# Handle authentication for Tweepy
auth = tweepy.OAuthHandler(os.environ.get("api_key"), os.environ.get("api_secret"))
api = tweepy.API(auth, wait_on_rate_limit = True)

# input arguments
input_parser = argparse.ArgumentParser(arg_formating=argparse.RawDescriptionHelpFormatter,
                                        description = "Format: python3 [-u | -s | -f | -F] [-i] <<path/to/input>> [-o] <<output file name>>",
                                        epilogue = "By itself, the script will take user-defined input and dump Twitter data to a CSV.")

input_parser.add_argument("-l", "--list", type = str, required = False, help = "use a list of search terms provided via a .txt file. The search terms should be separated by new line.")
input_parser.add_argument("-u", "--username", type = str, required = False, help ="Query data for a Twitter profile given a username.")
input_parser.add_argument("-f", "--followers", type = str, required = False, help ="Obtain followers for an account and their profile details.")
input_parser.add_argument("-F", "--following", type = str, required = False, help ="Obtain who an account is following for an account and their profile details.")
input_parser.add_argument("-o", "--output_csv", type = str, required = True, help ="Specify the name of your output file.")
args = input_parser.parse_args()

# empty dictionary to pass input to depending on input options
input_usernames = []
input_search_term = []

# Input [-i] arg Logic
# Take list of usernames as argument
if args.list:
    with open(sys.argv[1].split("\n"), 'r') as f:
        contents = f.read()

if args.username:

if args.followers:

if args.following: 

if args.output_csv:

        




# API calls
def get_profile_data(query):
    tweets = []



# Output Logic
if args.output_csv:
    with open(args.output_csv, "w") as f:
        writer = csv.writer(f)
        # csv_headers_tweet = [<<headers from data - tweets>>]
        # csv_headers_profile = [<<headers from data - Profile>>]



