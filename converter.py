from flask import Flask, request, render_template
from osgeo import ogr
app = Flask(__name__)


@app.route("/gml/")
def to_gml():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry:
        return geometry.ExportToGML()


@app.route("/kml/")
def to_kml():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry:
        return geometry.ExportToKML()


@app.route("/wkt/")
def to_gml():
    geojson = request.get_json()
    geometry = ogr.CreateGeometryFromJson(geojson)
    if geometry:
        return geometry.ExportToWKT()



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
