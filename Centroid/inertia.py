from shapely.geometry import Point, Polygon
from descartes import PolygonPatch
from IPython.display import display
from icecream import ic
from math import pi
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array

# pd.set_option('display.precision',2)
pd.set_option('display.float_format','{:,.2f}'.format)


class single_shape:
	def __init__(self,shape,shp_num,full_shape,inertia_type,axis_type):
		self.shape = shape['shape']
		self.shape_type = shape['shape_type']
		self.sign = shape['sign']
		self.inertia_type = inertia_type
		self.full_shape = full_shape
		self.axis_type = axis_type
		self.get_bounds()
		self.get_inertia()

		if self.inertia_type == 'I_y':
			self.df = pd.DataFrame({
				'Name':[shp_num],
				'Sign':[self.sign],
				'x Centroid': [self.shape.centroid.x],
				'Area':[self.shape.area],
				'Parallel axis':[self.p_axis],
				'I_y':[self.inertia],
			})
		if self.inertia_type == 'I_x':
			self.df = pd.DataFrame({
				'Name':[shp_num],
				'Sign':[self.sign],
				'y Centroid': [self.shape.centroid.y],
				'Area':[self.shape.area],
				'Parallel axis':[self.p_axis],
				'I_x':[self.inertia],
			})




	
	def get_bounds(self):
		s = self.shape
		self.x_len = (s.bounds[2] - s.bounds[0])
		self.y_len = (s.bounds[3] - s.bounds[1])


		if self.inertia_type == 'I_y':
			self.b = self.y_len
			self.h = self.x_len
			if self.axis_type == 'axis':
				self.p_axis =  (self.shape.area * (self.shape.centroid.x)**2)
			elif self.axis_type == 'centroid':
				self.p_axis =  (self.shape.area * (self.shape.centroid.x - self.full_shape.centroid.x)**2)
			# 



		elif self.inertia_type == 'I_x':
			self.b = self.x_len
			self.h = self.y_len
			if self.axis_type == 'axis':
				self.p_axis =  (self.shape.area * (self.shape.centroid.y)**2)
			elif self.axis_type == 'centroid':
				self.p_axis =  (self.shape.area * (self.shape.centroid.y - self.full_shape.centroid.y)**2)


			# 
		

	def get_inertia(self):
		if self.shape_type == 'Rectangle':
			self.inertia = (1/12 * self.b * self.h**3) + self.p_axis
		elif self.shape_type == 'Triangle':
			self.inertia = (1/36 * self.b * self.h**3) + self.p_axis
		elif self.shape_type == 'Circle':
			self.inertia = (1/4 * pi * (self.b/2)**4) + self.p_axis

		
		



class full_shape:
	def __init__(self,shapes,inertia_type,axis_type):
		# self.df = pd.DataFrame({'inertia':[],'shape_type':[],'sign':[]})

		for i,shape in enumerate(shapes):
			if i == 0:
				self.shape = shape['shape']
			elif shape['sign'] == '+':
				self.shape = self.shape.union(shape['shape'])
			else:
				self.shape = self.shape.difference(shape['shape'])

		for i,shape in enumerate(shapes):
			c_shape = single_shape(shape,i+1,self.shape,inertia_type,axis_type)
			single_inertia = c_shape.inertia
			# print(f"{i}  {single_inertia:,.2f}")
			if i == 0:
				self.inertia = single_inertia
			elif shape['sign'] == '+':
				self.inertia += single_inertia
			else:
				self.inertia -= single_inertia

			# Dataframe
			if i ==0:
				self.df = c_shape.df
			else:
				self.df = self.df.append(c_shape.df)

		# Df
		if inertia_type == 'I_y':
			self.df = self.df.append(pd.DataFrame({
				'Name':['Total'],
				'Sign':[''],
				'x Centroid': [self.shape.centroid.x],
				'Area':[self.shape.area],
				'Parallel axis':[''],
				'I_y':[self.inertia],
			}))
		if inertia_type == 'I_x':
			self.df = self.df.append(pd.DataFrame({
				'Name':['Total'],
				'Sign':[''],
				'y Centroid': [self.shape.centroid.y],
				'Area':[self.shape.area],
				'Parallel axis':[''],
				'I_x':[self.inertia],
			}))
		self.df.set_index('Name',inplace=True)

		# Plot
		fig,ax = plt.subplots(figsize=(3,3))
		x1,y1,x2,y2 = self.shape.bounds
		xy1 = min(x1,y1)
		xy2 = max(x2,y2)
		ax.set_xlim(xy1,xy2)
		ax.set_ylim(xy1,xy2)
		

		for i,shape in enumerate(shapes):
			S = shape['shape']
			if shape['sign'] == '+':
				ax.add_artist(PolygonPatch(S,facecolor='green',alpha=1))
				ax.text(S.centroid.x,S.centroid.y,f"{i+1}",fontsize=10,bbox=dict(facecolor='green', alpha=1))
			else:
				ax.add_artist(PolygonPatch(S,facecolor='red',alpha=0.3))
				ax.text(S.centroid.x,S.centroid.y,f"{i+1}",fontsize=10,bbox=dict(facecolor='red', alpha=.3))
