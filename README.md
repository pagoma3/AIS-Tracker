# AIS-Tracker
This web app attempts displays a live map of oil tankers in the Laconian Gulf (Greece), with the goal of tracking Russian shadow fleet Ship-to-Ship oil transfers that avoid Western sanctions.

The data consists of AIS Messages from the open-source websocket aisstream.io ; the map is built on top of the Leaflet Javascript library. 

TODO: aisstream.io does not allow cross-origin resource sharing, so the HTML scripts cannot obtain information directly
