import re
import pytz
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from geojson import Feature, FeatureCollection, Point

IMAGE_REGEX = re.compile("aurora_[N|S]_(.*).jpg")


def _parse_image_date(s):
    s = re.findall(IMAGE_REGEX, s)[0]
    d = datetime.strptime(s, '%Y-%m-%d_%H%M').replace(tzinfo=pytz.UTC)
    return d.isoformat()


def _parse_forecast_date(s):
    d = datetime.strptime(s, '%Y-%m-%d_%H:%M').replace(tzinfo=pytz.UTC)
    return d.isoformat()


def get_images(pole):
    """
    Get URLs to all of the OVATION model images for the last 24 hours for the provided pole.

    Returns list of dictionaries
    """
    url = f"https://services.swpc.noaa.gov/images/animations/ovation/{pole}/"
    r = requests.get(url)
    s = BeautifulSoup(r.content, "html.parser")
    a_list = s.find_all("a")
    href_list = []
    for a in a_list:
        if 'latest.jpg' in a['href']:
            continue
        if '.jpg' not in a['href']:
            continue
        href_list.append(
            dict(
                url=f"{url}{a['href']}",
                timestamp=_parse_image_date( a['href']),
                pole=pole
            )
        )
    return href_list


def get_latest_image(pole):
    """
    Get URL to the latest OVATION model image for the provided poll.
    
    Returns a URL string.
    """
    return f"https://services.swpc.noaa.gov/images/animations/ovation/{pole}/latest.jpg"


def get_grid():
    """
    Get auroral data in a gridded format for the entire Earth.

    Returns GeoJSON.
    """
    r = requests.get("https://services.swpc.noaa.gov/json/ovation_aurora_latest.json")
    j = r.json()
    feature_list = []
    for d in j['coordinates']:
        f = Feature(
            geometry=Point((d[0], d[1])),
            properties=dict(aurora=d[2])
        )
        feature_list.append(f)
    fc = FeatureCollection(feature_list)
    fc['properties'] = dict(
        observation_time=j['Observation Time'],
        forecast_time=j['Forecast Time']
    )
    return fc


def get_forecast():
    """
    Get Ovation Aurora Short Term Forecast data.

    Returns a list of dictionaries
    """
    r = requests.get("https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt")
    t = r.text.splitlines()
    str_list = t[16:]
    row_list = []
    for s in str_list:
        val_list = [v.strip() for v in s.split("    ")]
        d = dict(
            observation_time=_parse_forecast_date(val_list[0]),
            forecast_time=_parse_forecast_date(val_list[1]),
            hpi_north=int(val_list[2]),
            hpi_south=int(val_list[3]),
        )
        row_list.append(d)
    return row_list
