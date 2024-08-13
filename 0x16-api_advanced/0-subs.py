#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid or an error occurs.
    """
    # Define the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set up the headers with a custom User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and the subreddit exists
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the number of subscribers
        subscribers = data["data"]["subscribers"]
        
        return subscribers
    else:
        # Return 0 if the subreddit doesn't exist or there's an error
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
