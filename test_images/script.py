# import requests
# from urllib.parse import urljoin

# # Replace with your actual Unsplash API access key
# # ACCESS_KEY = "EVgXJnphEor2zwvsT6gDWagAC9ugvUNvokHBzGlUNrk"
# ACCESS_KEY = "42726933-ae5027059d857388fbdd2f34e"
# # API endpoint for searching images
# # BASE_URL = "https://api.unsplash.com/"
# BASE_URL = f"https://pixabay.com/api/?key={ACCESS_KEY}&q={'empty roads'}"

# # SEARCH_ENDPOINT = "search/photos"

# # Search terms for pot holes and plain roads
# # SEARCH_TERMS = "stray animals"

# # Specify desired number of images per search (max 30)
# NUM_IMAGES_PER_SEARCH = 30

# # Function to download an image and save it locally
# def download_image(image_url, filename):
#     response = requests.get(image_url)
#     if response.status_code == 200:
#         with open(filename, "wb") as f:
#             f.write(response.content)
#         print(f"Downloaded image: {filename}")
#     else:
#         print(f"Error downloading image: {image_url}")

# # Function to search for images using the API
# def search_images(page):
#     url = BASE_URL
#     params = {
#         # "client_id": ACCESS_KEY,
#         # "query": search_term,
#         "per_page": NUM_IMAGES_PER_SEARCH,
#         "page": page,
#     }
#     response = requests.get(url, params=params)
#     response.raise_for_status()  # Raise an exception for non-200 status codes
#     data = response.json()

#     # Download each image in the results
#     for image in data["results"]:
#         download_image(image["urls"]["regular"], f"{search_term}_{image['id']}.jpg")


# NUM_IMAGES_TO_DOWNLOAD = 360

# # Track downloaded images
# downloaded_count = 0
# page=1

# # Loop until target number is reached
# while downloaded_count < NUM_IMAGES_TO_DOWNLOAD:

#     # Download images for current search term
#     search_images(page)

#     # Update downloaded count
#     downloaded_count += NUM_IMAGES_PER_SEARCH
#     page+=1
#     # Print progress and avoid exceeding API rate limits
#     print(f"Downloaded {downloaded_count} images so far.")
#     # time.sleep(1)
# # Iterate through search terms and download images

# # Note: Ensure you stay within the API rate limits and terms of service.

import os

# Get the current working directory
cwd = os.getcwd()

# Initialize a counter to store the number of images
image_count = 0
# word="empty_road"

# Iterate over all files in the directory
for filename in os.listdir(cwd):
  # Check if the filename ends with a common image extension (jpg, jpeg, png)
  if filename.lower().endswith((".jpg", ".png",".jpeg")):
    image_count += 1
    # print(filename.lower())

# Print the total number of images found
print(f"Number of images in the current directory: {image_count}")
# # 1019--> buildings
# # 1500--> pedestrian
# # 1019--> shadows
# # 676--> streetlights
# # 980 --> stray animals
# # 1499 --> empty
# # 1027 --> road signs


# import requests
# import time

# # Your Pixabay API key
# API_KEY = "42726933-ae5027059d857388fbdd2f34e"

# # Base URL for Pixabay API requests
# BASE_URL = "https://pixabay.com/api"

# # Search term
# SEARCH_TERM = "pedestrian"

# # Desired number of images per page
# PER_PAGE = 200

# # Function to download an image
# def download_image(url, filename):
#     try:
#         response = requests.get(url, stream=True)
#         response.raise_for_status()

#         with open(filename, "wb") as f:
#             for chunk in response.iter_content(1024):
#                 f.write(chunk)

#         print(f"Downloaded image: {filename}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error downloading image: {e}")

# # Start with page 1
# page = 1
# # imagecnt=0
# download_cnt=0
# max_images=1000
# # Loop until enough images are downloaded or no more results are found
# while download_cnt<max_images:
#     # Construct search URL with pagination parameters
#     search_url = f"{BASE_URL}?key={API_KEY}&q={SEARCH_TERM}&image_type=photo&page={page}&per_page={PER_PAGE}"

#     # Make the search request
#     try:
#         response = requests.get(search_url)
#         response.raise_for_status()

#         data = response.json()

#         # Check if results are found
#         if data["totalHits"] > 0:
#             # Extract and download images from the current page
#             for hit in data["hits"]:
#                 image_url = hit["webformatURL"]
#                 filename = f"pedestrian_{hit['id']}.jpg"

#                 download_image(image_url, filename)
#                 download_cnt+=1
#                 # time.sleep(1)  # Introduce a delay between requests

#             # Check if the number of downloaded images is less than per_page
#             if len(data["hits"]) < PER_PAGE:
#                 # No more results on subsequent pages, break the loop
#                 print(f"Downloaded {len(data['hits'])} images. No more results found.")
            
#                 break

#             # Increment page number for next iteration
#             page += 1
#         else:
#             print(f"No results found for search term: {SEARCH_TERM}")
#             break  # No results found, break the loop
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching search results: {e}")
#         break  # Encountered error, break the loop

# print(f"total images: {download_cnt}")
# print("Download complete!")
