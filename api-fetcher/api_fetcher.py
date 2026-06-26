import requests


def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print("That GitHub username could not be found.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("A connection could not be made. Check your internet connection.")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")

    return None


def display_profile(profile):
    print("\nGitHub Profile")
    print("-" * 35)
    print(f"Username: {profile.get('login')}")
    print(f"Name: {profile.get('name') or 'Not provided'}")
    print(f"Location: {profile.get('location') or 'Not provided'}")
    print(f"Public repositories: {profile.get('public_repos')}")
    print(f"Followers: {profile.get('followers')}")
    print(f"Following: {profile.get('following')}")
    print(f"Profile: {profile.get('html_url')}")


def main():
    username = input(
        "Enter a GitHub username or press Enter to use Tomhero2kc: "
    ).strip()

    if not username:
        username = "Tomhero2kc"

    profile = get_github_profile(username)

    if profile:
        display_profile(profile)


if __name__ == "__main__":
    main()