
from urllib.request import urlopen
from urllib.error import HTTPError

url = "https://www.flipkart.com/search?q=tv"

try:
    response = urlopen(url)
    # Process the response here
except HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

































# if __name__=="__main__":
#     app.run(host="0.0.0.0")
