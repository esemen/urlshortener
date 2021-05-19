# Installation
```
$ docker-compose up
```

# Usage
You can use the link below to open the main interface
```
http://localhost:8000
```

### Api Documentation
You can use the link below for API documentation.
```
/apidoc/ 
```

# Settings
### settings.py
Domain to be used in URL shortening:
```
SITE_ADDRESS = "wrlc.shrt"
```
Number of characters URL shortened
```
MAX_CHAR_URLSHORTENER = 7
```

URL entry with a simple form on the home page and entered the last 
shortened URL addresses listed.

When the shortened link is clicked, a redirection is provided with Http Status Code 302.

### Statistics
After the short URL is created, it creates the relevant record in the statistics table at the first visit (GET method). It then updates this record with each visit.
