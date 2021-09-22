
import numpy as np
import sys
import os
import subprocess as sp
from astropy.io import fits
import os.path  
import scipy
import scipy.special
from scipy.special import gammaincinv
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import mimetypes
import warnings
import platform


from scipy import interpolate
from astropy.io.votable import parse
from mgefit.sectors_photometry import sectors_photometry

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,NullFormatter,
                               AutoMinorLocator,LogLocator,LinearLocator,AutoLocator)






