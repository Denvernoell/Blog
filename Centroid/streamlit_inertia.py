import streamlit as st
from inertia import single_shape, full_shape

from shapely.geometry import Point, Polygon
# from descartes import PolygonPatch
from IPython.display import display
# from icecream import ic
from math import pi
import matplotlib.pyplot as plt


st.title("Inertia")

# full = st.session_state
# st.session_state.shapes = []
# full = []


def next_spot():
    for i in range(1, 11):
        c_shape = f"S{i}"
        if c_shape not in st.session_state:
            # return c_shape
            # st.session_state[c_shape] = info
            return c_shape


# def add_rectangle():
if st.sidebar.button("New Rectangle"):
    # form = st.form('r')
    with st.form(key='r'):

        x1 = [float(p) for p in st.text_input("x1")]
        x2 = [float(p) for p in st.text_input("x2")]
        y1 = [float(p) for p in st.text_input("y1")]
        y2 = [float(p) for p in st.text_input("y2")]

        sign = st.radio('Positive or Negative', ['+', '-'])

        submitted = st.form_submit_button("Add")
        if submitted:
            info = {
                'shape': Polygon([x1, y1], [x2, y1], [x2, y2], [x1, y2]),
                'shape_type': 'Rectangle',
                'sign': sign,
            }
            next_spot(info)

            # st.session_state.shapes.append(info)

if st.sidebar.button("New Triangle"):
    # def add_triangle():
    with st.form(key='Tri'):

        p1 = st.text_input("p1 (x,y)")
        p2 = st.text_input("p2 (x,y)")
        p3 = st.text_input("p3 (x,y)")

        sign = st.radio('Positive or Negative', ['+', '-'])

        submitted = st.form_submit_button("Add")
        if submitted:
            p1 = [float(p) for p in p1.split(',')]
            p2 = [float(p) for p in p2.split(',')]
            p3 = [float(p) for p in p3.split(',')]

            info = {
                'shape': Polygon(p1, p2, p3),
                'shape_type': 'Triangle',
                'sign': sign,
            }
            # next_spot(info)
            # st.session_state.shapes.append(info)


def add_circle():
    with st.form(key='c'):

        center = st.text_input("Center (x,y)")
        radius = st.text_input("Radius")
        sign = st.radio('Positive or Negative', ['+', '-'])

        submitted = st.form_submit_button("Add")
        if submitted:
            center = [float(p) for p in center.split(",")]
            info = {
                'shape': Point(center).buffer(radius),
                'shape_type': 'Circle',
                'sign': sign,
            }
            st.session_state[next_spot()] = info

            # next_spot(info)
            # st.markdown(info)
            # st.session_state[next_spot()] = info
            # st.session_state.shapes.append(info)
if st.sidebar.button("New Circle"):
    add_circle()
    # st.session_state['S1'].append(add_circle())

st.markdown(st.session_state)

# if st.sidebar.button("New Rectangle"):
#     add_rectangle()

# if st.sidebar.button("New Triangle"):
#     add_triangle()

# if st.sidebar.button("New Circle"):
#     add_circle()

if st.sidebar.button("I_x"):
    st.write(st.session_state)

    # inertia_type = 'I_x'
    # D = full_shape(st.session_state, "I_x", 'centroid')
    # st.write(D.df)
    # st.write(D.fig)


if st.sidebar.button("I_y"):
    st.write(st.session_state)
    # inertia_type = 'I_y'
    # D = full_shape(st.session_state, "I_y", 'centroid')
    # st.write(D.df)
    # st.write(D.fig)

# D = full_shape(full, "I_y", 'centroid')
# # st.dataframe(D)
# # st.write(type(D))
# st.write(D.df)
# st.write(D.fig)


# points = [
#     [0, 0],
#     [8, 0],
#     [8, 8],
#     [5, 14],
#     [0, 14], ]
# hole = Point(5, 8).buffer(2)
# full = Polygon(points)
# S1 = full.envelope
# S2 = hole
# S3 = S1.difference(full)

# full = [
#     {
#         'shape': S1,
#         'shape_type': 'Rectangle',
#         'sign': '+',
#     },
#     {
#         'shape': S2,
#         'shape_type': 'Circle',
#         'sign': '-',
#     },
#     {
#         'shape': S3,
#         'shape_type': 'Triangle',
#         'sign': '-',
#     },
# ]

# D = full_shape(full, "I_y", 'centroid')
# # st.dataframe(D)
# # st.write(type(D))
# st.write(D.df)
# st.write(D.fig)
