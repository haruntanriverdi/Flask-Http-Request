# Flask Http Request
Flask Blueprint HTTP request using Yandex Geocoder API. This is the Flask Blueprint application to find the distance from the Moscow Ring Road to the specified address. 
coordinates. 

## Features
- Yandex Geocoder API are used to find address 

  Plaease refer: 
  https://yandex.com/dev/maps/geocoder/doc/desc/examples/geocoder_examples.html?from=mapsapi
  
- The distance between the coordinates found and the MKAD coordinates is calculated with the haversine formula.

```python
            R = radius(address_lot_lan[1])

            # Calculate distance with haversine formula for every mkad coordinates
            for coord in mkad_km:
                lon1 = radians(coord[1])
                lat1 = radians(coord[2])

                lon2 = radians(address_lot_lan[0])
                lat2 = radians(address_lot_lan[1])

                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distance = R * c
                distance_dict[coord[0]] = distance
```

- This formula calculates earth radius for specified address coordinates to increase distance accuracy:

```python
    # Radius calculation
    def radius(
            B):  # https://stackoverflow.com/questions/56420909/calculating-the-radius-of-earth-by-latitude-in-python-replicating-a-formula
        B = radians(B)  # converting into radians
        a = 6378.137  # Radius at sea level at equator
        b = 6356.752  # Radius at poles
        c = (a ** 2 * cos(B)) ** 2
        d = (b ** 2 * sin(B)) ** 2
        e = (a * cos(B)) ** 2
        f = (b * sin(B)) ** 2
        R = sqrt((c + d) / (e + f))
        return R
```

- To find nearest distance and point to specified address, minimum distance are selected in list and response as json format.


## Usage

- Install requirements

```
$ pip install -r requirements.txt
```
- You can run the application with the following command:

```
$ flask run
```
- Go to http://127.0.0.1:5000 using your web browser.

- http://127.0.0.1:5000/api?address=YOURADDRESS -> This returns full address which you specify
                    address, distance(km), point and status code
