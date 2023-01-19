# import requests

# # Use a for loop to send the request 10 times
# for i in range(10):
#   # Send the request to the Random User API
#   result = requests.get("https://randomuser.me/api/")

#   # Get the data from the response
#   data = result.json()

#   # Get the first and last name of the user
#   first_name = data['results'][0]['name']['first']
#   last_name = data['results'][0]['name']['last']

#   # Print the first and last name
#   print(f"{first_name} {last_name}")

import requests
import os

# Set the URL for the random user API
url = 'https://randomuser.me/api/'

# Use a for loop to make 10 requests to the API
for i in range(10):
  # Make the request
  result = requests.get(url)

  # Parse the response data as JSON
  data = result.json()

  # Get the user's first and last names
  first_name = data['results'][0]['name']['first']
  last_name = data['results'][0]['name']['last']

  # Print the first and last names
  print(f"{first_name} {last_name}")

  # Download the user's image
  image_url = data['results'][0]['picture']['large']
  image_data = requests.get(image_url).content

  # Save the image to a local file named {firstName} {lastName}.jpg
  file_name = f"{first_name} {last_name}.jpg"
  with open(file_name, 'wb') as f:
    f.write(image_data)
