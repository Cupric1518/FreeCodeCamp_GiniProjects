import numpy as np

def calculate(list):
    m = np.ones((3,3),dtype='int32')
    m[0,:] = list[:3].copy()
    m[1,:] = list[3:6].copy()
    m[2,:] = list[6:].copy()
    mean(m),'\n',var(m),'\n',stdev(m),'\n',max(m),'\n',min(m),'\n',sum(m)

def cols(m):
	axis1 = ([m[0,:], m[1,:], m[2,:]])
	return axis1

def rows(m):
    axis2 = ([m[:,0], m[:,1], m[:,2]])
    return axis2

def mean(m):
    meanrows = ([0,0,0])
    meancols = ([0,0,0])
    for i in range(3):
        meanrows[i] = ([rows(m)[i].sum()/rows(m)[i].size])
        meancols[i] = ([cols(m)[i].sum()/cols(m)[i].size])
    flat = m.sum()/9
    return print("'mean':",meanrows,',',meancols,',',flat,',')

def var(m):
    varcols = ([0,0,0])
    varrows = ([0,0,0])
    for i in range(3):
        varrows[i] = (rows(m)[i].var())
        varcols[i] = (cols(m)[i].var())
    flat = m.var()
    return print("'variance':",varrows,',',varcols,',',flat,',')

def stdev(m):
    stdrows = ([0,0,0])
    stdcols = ([0,0,0])
    for i in range(3):
        stdrows[i] = (rows(m)[i].std())
        stdcols[i] = (cols(m)[i].std())
    flat = m.std()
    return print("'standard deviation': [",stdrows,',',stdcols,',',flat,'],')

def max(m):
    mrows = ([0,0,0])
    mcols = ([0,0,0])
    for i in range(3):
        mrows[i] = (rows(m)[i].max())
        mcols[i] = (cols(m)[i].max())
    flat = m.max()
    return print("'max': [",mrows,',',mcols,',',flat,'],')

def min(m):
    mrows = ([0,0,0])
    mcols = ([0,0,0])
    for i in range(3):
        mrows[i] = (rows(m)[i].min())
        mcols[i] = (cols(m)[i].min())
    flat = m.min()
    return print("'min': [",mrows,',',mcols,',',flat,'],')

def sum(m):
    sumrows = ([0,0,0])
    sumcols = ([0,0,0])
    for i in range(3):
        sumrows[i] = (rows(m)[i].sum())
        sumcols[i] = (cols(m)[i].sum())
    flat = m.sum()
    return print("'sum': [",sumrows,',',sumcols,',',flat,'],')
