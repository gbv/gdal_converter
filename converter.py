from flask import Flask, request, render_template
from osgeo import ogr
import json
app = Flask(__name__)


@app.route("/gml/")
def to_gml():
    geojson = json.dumps(request.get_json())
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry is None:
        return
    return geometry.ExportToGML()


@app.route("/kml/")
def to_kml():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry is None:
        return
    return geometry.ExportToKML()


@app.route("/wkt/")
def to_wkt():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry is None:
        return

    return geometry.ExportToWKT()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
