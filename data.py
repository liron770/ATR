# =========================
# GET PARAMETERS
# =========================


SET_SEARCH_LOCATIONS_PARAMS = {
    "server_id": 0,
    "lat": 32.0,
    "lon": 34.0
}

NO_GPS_MODE_JSON = {
    "gps_mode": "1",
    "server_id": 0
}

# =========================
# CHANNEL CONTROL
# =========================

START_CHANNEL = {
    "action": "atr2"
}

STOP_CHANNEL = {
    "action": "atr2"
}

RESTART_CHANNEL = {
    "action": "geo"
}


RESTART_PORTRACK = {
    "serverId": 1
}

# =========================
# PARAMETERS
# =========================

SET_PARAMETERS = {
    "NIC": "192.168.1.10",
    "channelId": "1",
    "create_klv": "true",
    "keep_vmti": "false",
    "klv_on": "1",
    "klv_out": "udp://239.1.1.1:9007",
    "lowlatency": "true",
    "mode": "both",
    "nms": "0.5",
    "no_gps_mode": "false",
    "port": "8090",
    "profile": "vis960sfull",
    "threshold": "0.3",
    "time_existing_klv": "3",
    "tsPath": "../videos/22.ts",
    "udp_in": "udp://239.1.1.1:9003",
    "udp_out": "udp://239.1.1.1:9006"
}

GET_PARAMETERS = {
    "channelId": "1"
}


# =========================
# DETECTORS / PROFILES
# =========================

ADD_DETECTOR = {
    "detectorName": "vis960sfull",
    "algtrId": "1"
}

REMOVE_DETECTOR = {
    "detectorName": "vis960sfull",
    "algtrId": "1"
}

REMOVE_PROFILE = {
    "name": "vis960sfull"
}


# =========================
# LABELS / SAHI
# =========================

SET_LABELS = {
    "channelId": "1",
    "config": {
        "vis960sfull": ["person", "car", "bus"]
    }
}

SET_SAHI_CONFIG = {
    "channelId": "1",
    "config": {
        "model": "vis960sfull",
        "threshold": 0.3,
        "slice_size": 640
    }
}


# =========================
# GPS / GEOSPATIAL
# =========================

PIXEL2GEO = {
    "server_id": 0,
    "body": {
        "transf": [
            -4099002.1053290642,
            -1717193.3676469387,
            -40247.204896303949,
            -40206.957691407639,
            2474285.0967267,
            -887959.89243447175,
            -98945.0565793439,
            -98846.11152276455,
            -7.1738552626405374,
            85.365154527813758,
            -0.17388608623416502,
            -0.17371220014793085,
            64697721.917891443,
            87660503.8712204,
            4550343.3154194653,
            4545812.9721040456,
        ],
        "pixels": {
            "ptc": {"x": 0.18875502008032127, "y": 0.50614734420538587}
        }
    }
}

GEO2PIXEL = {
    "server_id": 0,
    "body": {
        "transf": [
            -4099002.1053290642,
            -1717193.3676469387,
            -40247.204896303949,
            -40206.957691407639,
            2474285.0967267,
            -887959.89243447175,
            -98945.0565793439,
            -98846.11152276455,
            -7.1738552626405374,
            85.365154527813758,
            -0.17388608623416502,
            -0.17371220014793085,
            64697721.917891443,
            87660503.8712204,
            4550343.3154194653,
            4545812.9721040456,
        ],
        "coords": {
            "ptc": {
                "x": 0.18875502008032127,
                "y": 0.50614734420538587,
                "z": 0
            }
        }
    }
}