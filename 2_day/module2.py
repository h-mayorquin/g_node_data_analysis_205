from numpy import *
from pylab import *
import scipy.signal

def cart2pol(x, y):
    """
    Convert from Cartesian to polar coordinates.

    Example
    -------
    >>> theta, radius = pol2cart(x, y)
    """
    radius = hypot(x, y)
    theta = arctan2(y, x)
    return theta, radius

def compass(u, v, arrowprops=None):
    """
    Compass draws a graph that displays the vectors with
    components `u` and `v` as arrows from the origin.

    Examples
    --------
    >>> import numpy as np
    >>> u = [+0, +0.5, -0.50, -0.90]
    >>> v = [+1, +0.5, -0.45, +0.85]
    >>> compass(u, v)
    """

    angles, radii = cart2pol(u, v)

    fig, ax = subplots(subplot_kw=dict(polar=True))

    kw = dict(arrowstyle="->", color='k')
    if arrowprops:
        kw.update(arrowprops)
    [ax.annotate("", xy=(angle, radius), xytext=(0, 0),
                 arrowprops=kw) for
     angle, radius in zip(angles, radii)]

    ax.set_ylim(0, np.max(radii))
    return ax

def EX_psth(data, TimeUnitsMS, BinSizeMS):
    """
    data: n x 1 array of 0/1 spike data
    TimeUnitsMS: resoluton of spike matrix relative to milliseconds (<=1)
    WindowWidthMS: length of the window (in ms)
    
    """
    # max time
    data = array(data,dtype='float')
    Tmax = data.shape[0]*TimeUnitsMS
    
    # number of trials
    n=data.shape[1]

    # bin size in orignal time res
    bin_size = floor(BinSizeMS/TimeUnitsMS);

    # define histogram borders (left edges)
    edges=arange(0,floor(Tmax/bin_size)*bin_size,bin_size)
    # make histogram
    M=data[0:floor(Tmax/bin_size)*bin_size,:].sum(axis=1)/n

    M2=reshape(M,(bin_size,M.shape[0]/bin_size),order='F').sum(axis=0)

    # nomalize hitogram to rate

    M2 = M2/BinSizeMS*1000
    b = bar(edges,M2,width=bin_size)
    
    ylabel('Rate  (1/s)')
    xlabel('Time (ms)')
    ylim(0, ceil(M2.max()/10)*10)
    xlim(0,Tmax)
    return M2,edges,gca()

def EX_boxcar(data, TimeUnitsMS, WindowWidthMS):
    """
    This function performs a boxcar convoluton, or equivalently, a moving
    window average. For matlab compatibility convolution is performed along 
    the 1st dimenson (python standard would be along last dimension).
    
    data: full 0/1 spike matrix with dimensions rows x cols: 
          time x trial OR time x channel
    TimeUnitsMS: resoluton of spike matrix relative to milliseconds
    WindowWidthMS: length of the window (in ms)
    """
    
    w = floor(WindowWidthMS/TimeUnitsMS)
    data = atleast_2d(data)
    boxcar = ones(w)

    # 2 - filter time series (alternatively use : ADF_convolution.m)
    data = scipy.signal.lfilter(boxcar,1, data.T, 0)
    data = data[w:,:]

    # 3 - normalize to firing rate in units of 1/s = Hz
    data = data/w*1000
    time = arange(0,len(data))+floor(w/2)
    time = time*TimeUnitsMS
    return data.T,time

def EX_dotdisplay(data, TimeUnitsMS):
    """
    data: full 0/1 spike matrix with dimensions rows x cols: 
          time x trial OR time x channel
    TimeUnitsMS: resoluton of spike matrix relative to milliseconds
    """
    t = arange(data.shape[0])*TimeUnitsMS
    Tmax = data.shape[0]*TimeUnitsMS
    n = data.shape[1]
    x,y = where(data==1)
    vlines(x,y-.25,y+.25)
    ylim(0.5,n+0.5)
    xlim(0,Tmax)
    ylabel('Trials')
    xlabel('Time (ms)')
    return gca()
