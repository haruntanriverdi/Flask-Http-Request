from flask import Blueprint, Flask, render_template, request, jsonify, Response, make_response
import time, base64, hmac, hashlib, requests, json
import xml.etree.ElementTree as ET
from math import sin, cos, sqrt, atan2, radians
import logging

Main = Blueprint('Main', __name__, template_folder='templates')
Error = Blueprint('errors', __name__)

LOG = logging.getLogger(__name__)


@Main.route('/')
def index():
    return render_template('index.html')


@Error.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404


@Main.route('/api', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'address' in request.args:

        address = str(request.args['address'])
    else:
        status_code = Response(status=400)
        return jsonify(status_code=status_code.status_code, description="Please specify address")

    mkad_km = [
        [1, 37.842762, 55.774558],
        [2, 37.842789, 55.76522],
        [3, 37.842627, 55.755723],
        [4, 37.841828, 55.747399],
        [5, 37.841217, 55.739103],
        [6, 37.840175, 55.730482],
        [7, 37.83916, 55.721939],
        [8, 37.837121, 55.712203],
        [9, 37.83262, 55.703048],
        [10, 37.829512, 55.694287],
        [11, 37.831353, 55.68529],
        [12, 37.834605, 55.675945],
        [13, 37.837597, 55.667752],
        [14, 37.839348, 55.658667],
        [15, 37.833842, 55.650053],
        [16, 37.824787, 55.643713],
        [17, 37.814564, 55.637347],
        [18, 37.802473, 55.62913],
        [19, 37.794235, 55.623758],
        [20, 37.781928, 55.617713],
        [21, 37.771139, 55.611755],
        [22, 37.758725, 55.604956],
        [23, 37.747945, 55.599677],
        [24, 37.734785, 55.594143],
        [25, 37.723062, 55.589234],
        [26, 37.709425, 55.583983],
        [27, 37.696256, 55.578834],
        [28, 37.683167, 55.574019],
        [29, 37.668911, 55.571999],
        [30, 37.647765, 55.573093],
        [31, 37.633419, 55.573928],
        [32, 37.616719, 55.574732],
        [33, 37.60107, 55.575816],
        [34, 37.586536, 55.5778],
        [35, 37.571938, 55.581271],
        [36, 37.555732, 55.585143],
        [37, 37.545132, 55.587509],
        [38, 37.526366, 55.5922],
        [39, 37.516108, 55.594728],
        [40, 37.502274, 55.60249],
        [41, 37.49391, 55.609685],
        [42, 37.484846, 55.617424],
        [43, 37.474668, 55.625801],
        [44, 37.469925, 55.630207],
        [45, 37.456864, 55.641041],
        [46, 37.448195, 55.648794],
        [47, 37.441125, 55.654675],
        [48, 37.434424, 55.660424],
        [49, 37.42598, 55.670701],
        [50, 37.418712, 55.67994],
        [51, 37.414868, 55.686873],
        [52, 37.407528, 55.695697],
        [53, 37.397952, 55.702805],
        [54, 37.388969, 55.709657],
        [55, 37.383283, 55.718273],
        [56, 37.378369, 55.728581],
        [57, 37.374991, 55.735201],
        [58, 37.370248, 55.744789],
        [59, 37.369188, 55.75435],
        [60, 37.369053, 55.762936],
        [61, 37.369619, 55.771444],
        [62, 37.369853, 55.779722],
        [63, 37.372943, 55.789542],
        [64, 37.379824, 55.79723],
        [65, 37.386876, 55.805796],
        [66, 37.390397, 55.814629],
        [67, 37.393236, 55.823606],
        [68, 37.395275, 55.83251],
        [69, 37.394709, 55.840376],
        [70, 37.393056, 55.850141],
        [71, 37.397314, 55.858801],
        [72, 37.405588, 55.867051],
        [73, 37.416601, 55.872703],
        [74, 37.429429, 55.877041],
        [75, 37.443596, 55.881091],
        [76, 37.459065, 55.882828],
        [77, 37.473096, 55.884625],
        [78, 37.48861, 55.888897],
        [79, 37.5016, 55.894232],
        [80, 37.513206, 55.899578],
        [81, 37.527597, 55.90526],
        [82, 37.543443, 55.907687],
        [83, 37.559577, 55.909388],
        [84, 37.575531, 55.910907],
        [85, 37.590344, 55.909257],
        [86, 37.604637, 55.905472],
        [87, 37.619603, 55.901637],
        [88, 37.635961, 55.898533],
        [89, 37.647648, 55.896973],
        [90, 37.667878, 55.895449],
        [91, 37.681721, 55.894868],
        [92, 37.698807, 55.893884],
        [93, 37.712363, 55.889094],
        [94, 37.723636, 55.883555],
        [95, 37.735791, 55.877501],
        [96, 37.741261, 55.874698],
        [97, 37.764519, 55.862464],
        [98, 37.765992, 55.861979],
        [99, 37.788216, 55.850257],
        [100, 37.788522, 55.850383],
        [101, 37.800586, 55.844167],
        [102, 37.822819, 55.832707],
        [103, 37.829754, 55.828789],
        [104, 37.837148, 55.821072],
        [105, 37.838926, 55.811599],
        [106, 37.840004, 55.802781],
        [107, 37.840965, 55.793991],
        [108, 37.841576, 55.785017]
    ]
    address_lot_lan = []
    distance_dict = {}

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

    base = "https://geocode-maps.yandex.ru/1.x/"
    method = "?apikey=acd75d9c-3e83-4bd1-a118-27af4e1866ec&geocode={}&lang=en_RU".format(address)
    uri = base + method

    result = requests.get(url=uri)
    string_xml = result.content

    root = ET.fromstring(string_xml)
    for found in root.iter('{http://maps.yandex.ru/geocoder/1.x}found'):
        yandex_status = found.text
    for i in root.iter('{http://maps.yandex.ru/geocoder/1.x}text'):
        full_address = i.text
    if yandex_status == "1":
        status_code = Response(status=200)
        for child in root.iter("{http://www.opengis.net/gml}pos"):
            # print("lon:{}".format(child.text.split()[0]),"lat:{}".format(format(child.text.split()[1])))
            address_lot_lan.append(float(child.text.split()[0])), address_lot_lan.append(float(child.text.split()[1]))
        if any((address_lot_lan[0] and address_lot_lan[1]) in s for s in mkad_km):
            LOG.error('Specified address is located inside the MKAD')

            return jsonify(description="Specified address is located inside the MKAD",
                           status_code=status_code.status_code)
        else:
            R = radius(address_lot_lan[1])

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

            # print(test_dict)

            a, b = min(distance_dict.items(), key=lambda x: x[1])

            # print("Nearest point: {}".format(a), "\nDistance(km): {}".format(b))  # https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary

            return jsonify(point=a, distance=b, full_address=full_address, status_code=status_code.status_code,
                           coordinates=address_lot_lan)

    else:
        LOG.error('Invalid address input')
        status_code = Response(status=400)
        return jsonify(description="Invalid address input", status_code=status_code.status_code)
