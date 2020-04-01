import requests
import json

def getUserIdByEmail(email):
  response = requests.get("https://jsonplaceholder.typicode.com/users?email=%s" %(email))
  data = response.json()
  for user in data:
      user_id=user["id"]
  return user_id

def getPostsByUserId(user_id):
  res = []
  response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=%s" %(user_id))
  data = response.json()
  for post in data:
    res.append(post)
  return res

def getAlbumsByUserId(user_id):
  res = []
  response = requests.get("https://jsonplaceholder.typicode.com/albums?userId=%s" %(user_id))
  data = response.json()
  for album in data:
    res.append(album)
  return res

def getPhotosFromAlbum(albums,album_pos):
  res = []
  album_id=albums[album_pos]["id"]
  response = requests.get("https://jsonplaceholder.typicode.com/photos?albumId=%s" %(album_id))
  data = response.json()
  for photo in data:
    res.append(photo)
  return res


if __name__=="__main__":
  user_id = getUserIdByEmail("Nathan@yesenia.net")
  posts = getPostsByUserId(user_id)
  albums = getAlbumsByUserId(user_id)
  photos = getPhotosFromAlbum(albums,3)

  response = {"user_id":user_id, "posts":posts, "albums":albums, "photos": photos}
  json_response = json.dumps(response)

  print(json_response)
  
