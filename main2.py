# import requests, json  #imports the json library

# result = requests.get("https://randomuser.me/api/")
# user = result.json()  #a dictionary containing the user's data
# print(
#   json.dumps(user, indent=2)
# )  #outputs the json to the console with an indent to make it more readable.

import requests, json

result = requests.get("https://randomuser.me/api/")
user = result.json()
# print(json.dumps(user, indent=2))

name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

print(name) # output the variable
image = f"""{user["results"][0]["picture"]["medium"]}"""  # Get the user's profile picture and assign to a variable, changing 'medium' to 'large' will make the image less pixelated
picture = requests.get(image)  #downloads the image
f = open(
  "image.jpg", "wb"
)  # opens the image.jpg file for writing in binary (data of the image will be added to the repl)
f.write(picture.content)  #writes the image to the file
f.close()  #closes the file

print(image)
