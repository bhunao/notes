# Import HappyX
import
  happyx

# Serve at http://127.0.0.1:5000
serve("127.0.0.1", 5000):
  # on GET HTTP method at http://127.0.0.1:5000/
  get "/":
    # Return plain text
    "Hello, world!"
  # on any HTTP method at http://127.0.0.1:5000/public/path/to/file.ext
  staticDir "public"

