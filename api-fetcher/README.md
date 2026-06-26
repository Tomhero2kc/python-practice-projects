# GitHub Profile Fetcher

I built this small project to practise getting information from an API.

The program asks for a GitHub username, sends a request to the GitHub API and displays some public profile details.

## What It Shows

- Username
- Name
- Location
- Number of public repositories
- Followers
- Following

## How to Run It

Install the Requests library:

```bash
pip install requests
```

Run the program from the main repository folder:

```bash
python api-fetcher/api_fetcher.py
```

Press Enter without typing a username to use `Tomhero2kc`.

## What I Learned

While building this project, I learned how to:

- Send requests to an API
- Read JSON data returned by the API
- Access information stored in Python dictionaries
- Handle internet connection problems
- Display a message when a GitHub username cannot be found
