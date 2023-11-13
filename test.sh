#!/bin/bash

printf "\nVerifica URL http://www.wikipedia.org/\n"
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/sites/u=https://www.wikipedia.org/

sleep 3

printf "\nVerifica URL https://www.thetimes.co.uk/ con espressione regolare\n"
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/sites/u=https://www.thetimes.co.uk/search/%3Fsource=nav-desktop%26q=italy/r=%5BIi%5Dtaly%7C%28%5E%5C%5B%2F%263%7B2%7D%24%29

sleep 3

printf "\nVerifica URL https://www.focus.it/\n"
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/sites/u=https://www.focus.it/

sleep 3

printf "\nVerifica URL http://www.google.com/niente\n"
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/sites/u%3Dhttp://www.google.com/niente/

sleep 3

printf "\nVerifica URL https://www.w3schools.com/ con espressione regolare\n"
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/sites/u%3Dhttps://www.w3schools.com/tags/ref_urlencode.ASP/r%3D[0-9]

