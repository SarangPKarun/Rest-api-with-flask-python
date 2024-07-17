"""
blocklist.py

This file contains the blocklist of the JWT tokens. It will be imported by the app 
and the logout resources so that the token can be added to the blocklist when the user logs out.

"""

BLOCKLIST = set()

