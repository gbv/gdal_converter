from flask import Flask, request, render_template
from osgeo import ogr
app = Flask(__name__)


@app.route("/kml/")
def to_kml():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    return geometry.ExportToKml


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
