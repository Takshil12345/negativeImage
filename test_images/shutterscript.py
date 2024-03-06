import requests

# Set up your Shutterstock API credentials
client_id = 'EBIbG7QP3NRrc7zXQj0IznLMp7Kdwy4j'
client_secret = 'so8vr30pEUDLNxTn'

# Set up the base URL for the Shutterstock API
base_url = 'https://api.shutterstock.com/v2/'

# Set up parameters for the image search
params = {
    'query': 'houses on empty roads',
    'per_page': 100,  # Adjust per_page based on your needs
}

# Make the request to search for images
response = requests.get(base_url + 'images/search', params=params, auth=(client_id, client_secret))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Iterate over the results and download the images
    for image in data['data']:
        image_url = image['assets']['preview']['url']
        # Download the image (you may want to handle exceptions here)
        image_data = requests.get(image_url).content
        with open(f'{image["id"]}.jpg', 'wb') as f:
            f.write(image_data)
else:
    print('Error:', response.status_code)
