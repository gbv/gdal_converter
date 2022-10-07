from turtle import st
from flask import Flask, request, render_template
from osgeo import ogr, gdal

from tempfile import mkdtemp
from zipfile import ZipFile
from os import listdir
from glob import glob
from os.path import join, splitext
from shutil import rmtree
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
    return geometry.ExportToGML(options = ['NAMESPACE_DECL=YES'])


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

@app.route('/geojson', methods=['POST'])
def convert():
    
    zipped_shape = None
    for k, v in request.files.to_dict().items():
        if k.lower().endswith('.zip'):
            zipped_shape = ZipFile(v)
            break
    if zipped_shape:
        try:
            extract_here = mkdtemp()
            print(extract_here, flush=True)
            zipped_shape.extractall(extract_here)
            shape_files = glob(join(extract_here, '**', '*.shp'))
            print(shape_files, flush=True)
            features = []
            json_path = join(extract_here, 'result.geojson')
            options = gdal.VectorTranslateOptions(format="GeoJSON")

            for shape_file in shape_files:
                gdal.VectorTranslate(json_path, shape_file, options=options)
            
                with open(json_path, 'r') as jason:
                    collection = json.load(jason)
                features += collection['features']
                
            return {'type': 'FeatureCollection', 'features': features}
        finally:
            rmtree(extract_here)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
