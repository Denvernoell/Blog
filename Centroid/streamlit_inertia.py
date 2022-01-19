import streamlit as st
from inertia import single_shape,full_shape

from shapely.geometry import Point, Polygon
# from descartes import PolygonPatch
from IPython.display import display
# from icecream import ic
from math import pi
import matplotlib.pyplot as plt


st.title("Inertia")


points = [[0,0],
[8,0],
[8,8],
[5,14],
[0,14],]
hole = Point(5,8).buffer(2)
full = Polygon(points)
S1 = full.envelope
S2 = hole
S3 = S1.difference(full)

full = [
	{
		'shape':S1,
		'shape_type':'Rectangle',
		'sign':'+',
		},
	{
		'shape':S2,
		'shape_type':'Circle',
		'sign':'-',
		},
	{
		'shape':S3,
		'shape_type':'Triangle',
		'sign':'-',
		},
]
D = full_shape(full,"I_y",'centroid').df
st.write(type(D))
# st.write(D)





