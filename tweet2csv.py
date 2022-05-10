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
                                        description = "Format: python3 [-u | -s | -f | -F] [-i] <<path/to/input>> [-o] [output_format]",
                                        epilogue = "By itself, the script will take user-defined input and The following are optional arguments to add")

input_parser.add_argument("-l", "--list", type = str, required = False, help = "use a list of search terms provided via a .txt file. The search terms should be separated by new line.")
input_parser.add_argument("-o", "--output", type = str, required = False, help ="define an output format other than stdout. Can be .csv or .json")
input_parser.add_argument("-u", "--username", type = str, required = False, help ="Query data for a Twitter profile given a username.")
input_parser.add_argument("-f", "--followers", type = str, required = False, help ="Obtain followers for an account and their profile details.")
input_parser.add_argument("-F", "--following", type = str, required = False, help ="Obtain who an account is following for an account and their profile details.")
args = input_parser.parse_args()

# ARG Logic

# API calls

# Output Logic


# Take list of usernames as argument
with open(sys.argv[1].split("\n"), 'r') as f:
    contents = f.read()


