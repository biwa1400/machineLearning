'''
tile(inX,(dataSetSize,1))-dataSet
sqDiffMat.sum(axis=1)
distance.argsort()
'''
from numpy import *

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels
	
def classify0 (inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat = diffMat**2
	sqDistance = sqDiffMat.sum(axis=1)
	distance = sqDistance**0.5
	sortedDistance = distance.argsort()
	return sortedDistance
	
if __name__ == '__main__':
	group,labels = createDataSet()
	value = classify0([0,0],group,labels,3)
	print(value)