from instascrape import Profile
# Create a profile object
import warnings

# Replace 'your_session_id' with the actual session ID
session_id = 'your_session_id'
profile = Profile('gruber._.maximilian')

# Scrape the profile data
profile.scrape()

# Print the profile information
print(f"Username: {profile.username}")
print(f"Full Name: {profile.full_name}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.following}")
print(f"Posts: {profile.posts}")
