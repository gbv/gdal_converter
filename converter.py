from flask import Flask, request, render_template
from osgeo import ogr
import json
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


def extract_geometry(request):
    logging.debug("extracting geometry")
    geojson = request.get_json()
    logging.debug("got: " + str(geojson))
    if geojson:
        logging.debug("OGRING geometry")
        return ogr.CreateGeometryFromJson(json.dumps(geojson))
    else:
        raise ValueError("empty json")


@app.route("/gml/")
def to_gml():
    geometry = extract_geometry(request)
    if geometry is None:
        logging.debug("No geomtry: " + str(geometry))
        return
    return geometry.ExportToGML()


@app.route("/kml/")
def to_kml():
    geometry = extract_geometry(request)
    if geometry is None:
        return
    return geometry.ExportToKML()


@app.route("/wkt/")
def to_wkt():
    geometry = extract_geometry(request)
    if geometry is None:
        return
    return geometry.ExportToWkt()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
