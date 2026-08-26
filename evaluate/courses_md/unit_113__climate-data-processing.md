---
title: "Climate data processing in Python"
unit_id: 113
course_id: 4
level: "Developer"
slug: climate-data-processing
is_course: 0
---

# Climate data processing in Python

## Extracted resources (local files)

### Climate data processing using xarray, cython and dask
*Source file:* `Instructions_for_climate_data_processing.pdf`  ·  *type:* file

Climate data processing using xarray, cython and dask 
 
Prepared by 
Qinqin Kong and Matthew Huber 
Department of Earth, Atmospheric, and Planetary Sciences 
kong97@purdue.edu  
Objective 
The main objective of this tutorial is to introduce how to make climate data processing 
efficiently using the python packages xarray, cython, and dask. 
 
Introduction 
Massive climate model output size has posed great challenges to data processing. First, the 
dataset can be too large load into memory. Second, interpreted programming languages like 
Python are usually slow especially when processing large amount of data. The first challenge can 
be solved by using Dask which can split your large computations in to smaller ones and do 
calculation chunk by chunk. The second challenge can be resolved by using both Cython and 
Dask. Cython is able to speed up Python code by compiling it into machine code, and Dask will 
further improve your code performance by enabling parallel computing.  
 
Course material: 
Jupyter notebook:  
Climate_data_processing_using_xarray_dask_cython_mygeohub.ipynb 
Using_Cython_to_speed_up_your_python_code_mygeohub.ipynb 
 
You can access the jupyter notebooks at:  
1) the “FAIR Climate and Water Science” course webpage in Mygeohub;  
2) https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master  
 
Pre-recorded video: 
The pre-recorded video for this tutorial is accessible in the YouTube Channel of the Climate 
Dynamics Prediction Lab:  
https://www.youtube.com/watch?v=0GYdLmBU28s&t=707s  
https://www.youtube.com/watch?v=Wa3bAaXsS-4&t=981s

## Fetched resources (external URLs)

### Jupyter Notebook Exercise: using cython (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP9/Using_Cython_to_speed_up_your_python_code_mygeohub.ipynb

# Cython
In this tutorial, we will introduce how to use cython to speed up our python code

```python
import xarray as xr
import intake
import numpy as np
from scipy import optimize
from numba import njit, vectorize
import cython
```

____________
## 1. Read in CMIP6 data in Cloud
____________

```python
col = intake.open_esm_datastore("https://storage.googleapis.com/cmip6/pangeo-cmip6.json")
query = dict(experiment_id=['historical','ssp585'],
             source_id='KACE-1-0-G',
             table_id='3hr',
             variable_id=['tas','huss','ps'],
             member_id = 'r1i1p1f1')
col_subset = col.search(require_all_on=['source_id'], **query)
col_subset.df
```

```python
dset_dict = col_subset.to_dataset_dict(zarr_kwargs={'consolidated': True})
```

```python
list(dset_dict.keys())
```

```python
# we only select the first and last year of this century and compare them
hist=dset_dict['CMIP.NIMS-KMA.KACE-1-0-G.historical.3hr.gr'].sel(time='2000')
ssp=dset_dict['ScenarioMIP.NIMS-KMA.KACE-1-0-G.ssp585.3hr.gr'].sel(time='2100')
```

____________
## 2. Wet bulb temperature calculation using pure python functions
____________
First, we define a set of pure python functions to calculate wet bulb temperature.
References:
- Bolton: *The computation of equivalent potential temperature. Monthly weather review (1980) vol. 108 (7) pp. 1046-1053*
- Davies-Jones: *An efficient and accurate method for computing the wet-bulb temperature along pseudoadiabats. Monthly Weather Review (2008) vol. 136 (7) pp. 2764-2785*

```python
# define some constants
kd = 0.2854
lamda = 3.504
C = 273.15
y0 = 3036.0
y1 = 1.78
y2 = 0.448

# return saturation vapor pressure (Pa)
def esat(Tk):
    # Tk: air temperature (K)
    return 611.2*np.exp(17.67*(Tk-C)*((Tk-29.65)**(-1)))

# return saturation mixing ratio (kg/kg)
def mixrsat(Tk, ps):
    # Tk: air temperature (K)
    return 0.622*esat(Tk)*((ps - esat(Tk))**(-1))

#return vapor pressure (Pa)
def vaporpres(huss, ps):
    #huss: specific humidity (kg/kg)
    #ps: surface pressure (Pa)
    r=huss*((1-huss)**(-1))
    return ps*r*((0.622+r)**(-1))

# return temperature at lifting condensative level
def lcltemp(Tk,e):
    # Tk: air temperature (K)
    # e: vapor pressure (Pa)
    return 2840.0*(( 3.5*np.log(Tk) - np.log(e/100.0) - 4.805)**(-1)) + 55.0
    
# return potential temperature at LCL (K)
def thetadl(Tk, ps, e,Tl,mixr):
    return Tk*((100000*((ps-e)**(-1)))**kd)*((Tk*(Tl**(-1)))**(mixr*0.00028))

# return equivalent potential temperature (K)
def thetae(theta_dl, Tl, mixr):
    return theta_dl*np.exp(((3.036*(Tl**(-1)))-0.00178)*mixr*(1.0 + 0.000448*mixr))

# 1st guess of wet bulb temperature
def wb1stguess(X, D, Teq, ps, pi):
    if X > D:
        rs_teq=mixrsat(Teq,ps)
        dlnes_dTeq = 4302.645*((Teq-29.65)**(-2))
        wb_temp = Teq - ((2675.0*rs_teq)*((1.0 + 2675.0*rs_teq*dlnes_dTeq)**(-1)))
    else:
        k1 = pi*(-38.5*pi+137.81)-53.737
        k2 = pi*(-4.392*pi+56.831)-0.384
        if X>=1.0 and X<=D:
            wb_temp = k1-k2*X+C
        elif X>=0.4 and X<1:
            wb_temp = k1-1.21-(k2-1.21)*X+C
        else:
            wb_temp = k1-2.66-(k2-1.21)*X+0.58*(X**(-1))+C
    return wb_temp
def f(wb, ps, rs_wb):
    G=(y0*(wb**(-1))-y1)*(rs_wb*(1+y2*rs_wb))
    return ((C*(wb**(-1)))**lamda)*(1.0 - esat(wb)*(ps**(-1)))*np.exp(-lamda*G)
def dfdT(wb,ps,rs_wb):
    des_dwb=esat(wb)*4302.645*((wb-29.65)**(-2))
    pminuse = ps - esat(wb)
    rsdT=0.622*ps*(pminuse**(-2))*des_dwb
    dGdT = -y0*(rs_wb+y2*rs_wb*rs_wb)*(wb**(-2))+(y0*(wb**(-1))-y1)*(1.0+2.0*y2*rs_wb)*rsdT
    return -lamda*(wb**(-1)+kd*((pminuse)**(-1))*des_dwb+dGdT)*f(wb,ps,rs_wb)
def fwb(x, C0,C1):
    rs=mixrsat(x,C0)
    ff=f(x,C0,rs)
    df=dfdT(x,C0,rs)
    return (ff - C1)*(df**(-1))

# return wet bulb temperature
def wetbulb_py (Tk, huss, ps, xtol=0.001, rtol=8.881784197001252e-16, mitr=100):
    Tk=np.atleast_3d(Tk)
    huss=np.atleast_3d(huss)
    ps=np.atleast_3d(ps)
    x_max = Tk.shape[0]
    y_max = Tk.shape[1]
    z_max = Tk.shape[2]
    result = np.zeros((x_max, y_max, z_max), dtype=np.float64)
    for i in range(x_max):
        for j in range(y_max):
            for k in range(z_max):
                ps_tmp=ps[i,j,k]
                huss_tmp=huss[i,j,k]
                Tk_tmp=Tk[i,j,k]
                pi = (ps_tmp/100000)**(kd)
                mixr=huss_tmp*((1-huss_tmp)**(-1))*1000
                e=vaporpres(huss_tmp,ps_tmp)
                D = (0.1859*ps_tmp/100000 + 0.6512)**(-1)
                Tl = lcltemp(Tk_tmp,e)
                theta_dl=thetadl(Tk_tmp, ps_tmp, e,Tl,mixr)
                epott = thetae(theta_dl,Tl,mixr)
                Teq = epott*pi
                X = (C*(Teq**(-1)))**lamda
                wb_temp=wb1stguess(X, D, Teq,ps_tmp,pi)
                xa=wb_temp-10
                xb=wb_temp+10
                C0=ps_tmp
                C1=X
                result[i,j,k]=optimize.brentq(fwb, xa, xb, (C0,C1), xtol, rtol, mitr) # use scipy.optimize.brentq
    return result.squeeze()
```

Let's calculate wet bulb temperature for only one time step, and look at how long it takes

```python
tas=hist.tas.squeeze().drop(['height','member_id'])[0,:,:].load()
huss=hist.huss.squeeze().drop(['height','member_id'])[0,:,:].load()
ps=hist.ps.squeeze().drop(['height','member_id'])[0,:,:].load()
```

```python
%time wb=wetbulb_py(tas.values, huss.values, ps.values)
```

____________
## 3. Speed up our python code using cython
____________


Numba's ```@njit``` decorator can compile python code into machine code and make our for loop much faster. However, it won't work in this case. 

Cython is what we need! In order to really show how Cython is useful, let's start from the basics!

**How to build Cython code?**

**Two stages:**
- use Cython compiler to compile cython source file (```.pyx```) into C code (```.c```)
- use C compiler to compile ```.c``` file into ```.so``` file

**Several ways:**
- setup tools (more flexible, powerful)
- jupyter notebook: Cython compilation interactively (more interactive)

```python
def f(x):
    return x**2-x

def integrate_f_py(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
```

```python
%load_ext Cython
```

```python
%%cython -a
def f_cy(x):
    return x**2-x

def integrate_f_cy(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f_cy(a+i*dx)
    return s * dx
```

```python
%timeit integrate_f_py(1, 100, 1000)
```

```python
%timeit integrate_f_cy(1, 100, 1000)
```

Speed up by **30%** without doing anything: removal of interpreter overhead.

However the real improvement come from static typing!

**We can type variables**

```python
%%cython -a
def f_static(double x):
    return x**2-x

def integrate_f_static_var(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f_static(a+i*dx)
    return s * dx
```

```python
%timeit integrate_f_static_var(1, 100, 1000)
```

5 times speed up!

**We can also type function!** Python function is expensive, especially when calling in cython.

```python
%%cython -a
cdef double f_static(double x):
    return x**2-x

def integrate_f_static_var_func(double a, double b, int N):
    cdef int i
    cdef double s
    s = 0
    dx = (b-a)*N**(-1)
    for i in range(N):
        s += f_static(a+i*dx)
    return s * dx
```

```python
%timeit integrate_f_static_var_func(1, 100, 1000)
```

200 times speed up!

**Three typs of functions in cython.**
- ```cdef``` function can only be called within cython: fast supporting functions
- ```def``` functions can be called in python session: function that you want to import in python
- ```cpdef``` function can be called both within cython (as C functions) and python (python wrapper)

**No need to type everything!**
- cython enables automatic type inference during assignmnet
- Unnecessary typing may even slow things down (unnecessary type checks or conversions)
- Must type in performance critical part of the code (such as ```for``` loop: ```for``` loop needs to be white! ) 

**compare with Numba ```@njit```**

```python
@njit
def f_njit(x):
    return x**2-x
@njit
def integrate_f_njit(a,b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f_njit(a+i*dx)
    return s * dx
```

```python
%timeit integrate_f_njit(1, 100, 1000)
```

**Cython makes caling external C libraries straightfoward**

Cython already defines many standard C libarary functions for us! Such as the most commonly used standard C math library

```python
from libc.math cimport sin
cdef double f(double x):
    return sin(x * x)
```

https://github.com/cython/cython/blob/master/Cython/Includes/libc/math.pxd

**Cython for numpy user!**

```python
# a simple python function: add two arrays
a=np.random.randn(100,100)
b=np.random.randn(100,100)
def add_numpy(array_1,array_2):
    return array_1+array_2
```

```python
# numpy is already hightly optimized for such simple vectorized computation
%timeit add_numpy(a,b)
```

naively compile it

```python
%%cython -a
def add_cy(array_1,array_2):
    return array_1+array_2
```

```python
# no performance improvement, that's not how cython deal with array calculation
%timeit add_cy(a,b)
```

```python
# in order to show how cython speed up array calculation, let's start with this simple pure python code
# which does the same thing but use for loop
def add_py(array_1, array_2):
    x_max = array_1.shape[0]
    y_max = array_1.shape[1]
    result = np.zeros((x_max, y_max), dtype=array_1.dtype)
    for x in range(x_max):
        for y in range(y_max):
            result[x, y] = array_1[x, y]+array_2[x, y]
    return result
```

```python
# as we expect, it's slow
%timeit add_py(a,b)
```

```python
%%cython -a
import numpy as np
def add_cy1(array_1, array_2):
    x_max = array_1.shape[0]
    y_max = array_1.shape[1]
    result = np.zeros((x_max, y_max), dtype=array_1.dtype)
    for x in range(x_max):
        for y in range(y_max):
            result[x, y] = array_1[x, y]+array_2[x, y]
    return result
```

```python
%timeit add_cy1(a,b)
```

Only 30% speed up, we know real improvement come from static typing, but how to type array?

**Typed memoryview**
- **Memoryview:** memoryviews are C structures that can hold a pointer to the data of a NumPy array and all the necessary buffer metadata to provide efficient and safe access: dimensions, strides, item size, item type information, etc… They can be indexed by C integers, thus allowing fast access to the NumPy array data.

```python
cdef int [:] foo         # 1D memoryview
cdef int [:, :] foo      # 2D memoryview
cdef int [:, :, :] foo   # 3D memoryview
...                      # You get the idea.
```

```python
%%cython -a
import numpy as np
cimport numpy as np
def add_cy2(double[:, :] array_1, double[:, :] array_2):
    # Py_ssize_t is the proper C type for Python array indices.
    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]
    result = np.zeros((x_max, y_max))
    cdef double[:, :] result_view = result
    cdef Py_ssize_t x, y
    for x in range(x_max):
        for y in range(y_max):
            result_view[x, y] = array_1[x, y]+array_2[x, y]
    return result
```

```python
%timeit add_cy2(a,b)
```

Still slower than Numpy. What else we can do? 

**contiguous memory view** can enable fast index!
```python
cdef double[:, ::1] foo
```

```python
%%cython -a
import numpy as np
cimport cython
@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def add_cy3(double[:, ::1] array_1, double[:, ::1] array_2): #C contiguous memoryview
    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]
    result = np.zeros((x_max, y_max))
    cdef double[:, ::1] result_view = result
    cdef Py_ssize_t x, y
    for x in range(x_max):
        for y in range(y_max):
            result_view[x, y] = array_1[x, y]+array_2[x, y]
    return result
```

```python
%timeit add_cy3(a,b)
```

After all these efforts, we still cannot defeat Numpy. So, we definitely don't want to use Cython for such simple vectorized calculation. 

So, when should we use cython? Before answer this question, let's look at another functionality that Cython offer us:

**Using Parallelism: ```prange```**

```python
%%cython -a --compile-args=-fopenmp --link-args=-fopenmp
from cython.parallel import prange
import numpy as np
cimport cython
@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def add_cy4(double[:, ::1] array_1, double[:, ::1] array_2):
    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]
    result = np.zeros((x_max, y_max))
    cdef double[:, ::1] result_view = result
    cdef Py_ssize_t x, y
    for x in prange(x_max,nogil=True):
        for y in range(y_max):
            result_view[x, y] = array_1[x, y]+array_2[x, y]
    return result
```

```python
%timeit add_cy4(a,b)
```

```python
%timeit add_numpy(a,b)
```

```python
# make arrays bigger to show the benefits of parallelism
a=np.random.randn(1000,10000)
b=np.random.randn(1000,10000)
```

**When should we use Cython?**

- definitely not for ```a+b```; most useful for speeding up operations that can't be easily vectorized
- Use Cython for bottlenecks, rather than re-writing everything in Cython
- Numba ```@njit``` is an alternative, but sometimes not feasible, an example: https://docs.scipy.org/doc/scipy/reference/optimize.cython_optimize.html

```python
%%cython -a --compile-args=-Ofast --compile-args=-fopenmp --link-args=-fopenmp
import numpy as np
cimport numpy as np
cimport cython
from libc cimport math
from cython.parallel import prange
from scipy.optimize.cython_optimize cimport brentq
    
cdef double kd,lamda, C, y0, y1, y2
kd = 0.2854
lamda = 3.504
C = 273.15
y0 = 3036.0
y1 = 1.78
y2 = 0.448


ctypedef struct wb_params:
    double C0
    double C1

cdef double esat(double Tk) nogil:
    return 611.2*math.exp(17.67*(Tk-C)*((Tk-29.65)**(-1)))

cdef double mixrsat(double Tk,double ps) nogil:
    return 0.622*esat(Tk)*((ps - esat(Tk))**(-1))

cdef double vaporpres(double huss, double ps) nogil:
    cdef double r
    r=huss*((1-huss)**(-1))
    return ps*r*((0.622+r)**(-1))

cdef double lcltemp(double Tk,double e) nogil:
    return 2840.0*(( 3.5*math.log(Tk) - math.log(e/100.0) - 4.805)**(-1)) + 55.0

cdef double thetadl(double Tk, double ps, double e,double Tl,double mixr) nogil:
    return Tk*((100000*((ps-e)**(-1)))**kd)*((Tk*(Tl**(-1)))**(mixr*0.00028))

cdef double thetae(double theta_dl, double Tl, double mixr) nogil:
    return theta_dl*math.exp(((3.036*(Tl**(-1)))-0.00178)*mixr*(1.0 + 0.000448*mixr))

cdef double wb1stguess(double X, double D, double Teq, double ps, double pi) nogil:
    cdef double rs_teq, dlnes_dTeq, wb_temp, k1, k2
    if X > D:
        rs_teq=mixrsat(Teq,ps)
        dlnes_dTeq = 4302.645*((Teq-29.65)**(-2))
        wb_temp = Teq - ((2675.0*rs_teq)*((1.0 + 2675.0*rs_teq*dlnes_dTeq)**(-1)))
    else:
        k1 = pi*(-38.5*pi+137.81)-53.737
        k2 = pi*(-4.392*pi+56.831)-0.384
        if X>=1.0 and X<=D:
            wb_temp = k1-k2*X+C
        elif X>=0.4 and X<1:
            wb_temp = k1-1.21-(k2-1.21)*X+C
        else:
            wb_temp = k1-2.66-(k2-1.21)*X+0.58*(X**(-1))+C
    return wb_temp

cdef double f(double wb, double ps, double rs_wb) nogil:
    cdef double G
    G=(y0*(wb**(-1))-y1)*(rs_wb*(1+y2*rs_wb))
    return ((C*(wb**(-1)))**lamda)*(1.0 - esat(wb)*(ps**(-1)))*math.exp(-lamda*G)

cdef double dfdT(double wb,double ps,double rs_wb) nogil:
    cdef double des_dwb, pminus, rsdT, dGdT
    des_dwb=esat(wb)*4302.645*((wb-29.65)**(-2))
    pminuse = ps - esat(wb) #pminus in Pa
    rsdT=0.622*ps*(pminuse**(-2))*des_dwb
    dGdT = -y0*(rs_wb+y2*rs_wb*rs_wb)*(wb**(-2))+(y0*(wb**(-1))-y1)*(1.0+2.0*y2*rs_wb)*rsdT
    return -lamda*(wb**(-1)+kd*((pminuse)**(-1))*des_dwb+dGdT)*f(wb,ps,rs_wb)

cdef double fwb(double x, void *args) nogil:
    cdef wb_params *myargs = <wb_params *> args
    cdef double rs,ff,df
    rs=mixrsat(x,myargs.C0)
    ff=f(x,myargs.C0,rs)
    df=dfdT(x,myargs.C0,rs)
    return (ff - myargs.C1)*(df**(-1))

cdef double wb_brentq_wrapper(wb_params args, double xa, double xb, double xtol, double rtol, int mitr) nogil:
    return brentq(fwb, xa, xb, <wb_params *> &args, xtol, rtol, mitr, NULL)

@cython.wraparound(False)
@cython.boundscheck(False)
def wetbulb_cython (const double[:,:,:] Tk, const double[:,:,:] huss, const double[:,:,:] ps, double xtol=0.001, double rtol=0.0, int mitr=100000):
    cdef const double[:, :, ::1] Tk_view=Tk.copy()
    cdef const double[:, :, ::1] huss_view=huss.copy()
    cdef const double[:, :, ::1] ps_view=ps.copy()
    cdef Py_ssize_t i, j, k, x_max, y_max, z_max
    x_max = Tk_view.shape[0]
    y_max = Tk_view.shape[1]
    z_max = Tk_view.shape[2]
    result = np.zeros((x_max, y_max, z_max), dtype=np.float64)
    cdef double[:, :, ::1] result_view = result
    cdef double xa,xb,ps_tmp,huss_tmp,Tk_tmp,pi, mixr,e, D,Tl,theta_dl,epott,Teq,X,wb_temp
    cdef wb_params args
    for i in prange(x_max,nogil=True):
        for j in range(y_max):
            for k in range(z_max):
                ps_tmp=ps_view[i,j,k]
                huss_tmp=huss_view[i,j,k]
                Tk_tmp=Tk_view[i,j,k]
                pi = (ps_tmp/100000)**(kd)
                mixr=huss_tmp*((1-huss_tmp)**(-1))*1000 #mixing ratio (g/kg)
                e=vaporpres(huss_tmp,ps_tmp)
                D = (0.1859*ps_tmp/100000 + 0.6512)**(-1)
                Tl = lcltemp(Tk_tmp,e)
                theta_dl=thetadl(Tk_tmp, ps_tmp, e,Tl,mixr)
                epott = thetae(theta_dl,Tl,mixr)
                Teq = epott*pi
                X = (C*(Teq**(-1)))**lamda
                wb_temp=wb1stguess(X, D, Teq,ps_tmp,pi)
                xa=wb_temp-10
                xb=wb_temp+10
                args.C0=ps_tmp
                args.C1=X
                result_view[i,j,k]=wb_brentq_wrapper(args, xa, xb, xtol, rtol, mitr)
    return result
```

```python
# our cython function require 3D output of double type. But we can be more flexible by for example fused type in Cython
# Introduction to fused type: https://cython.readthedocs.io/en/latest/src/userguide/fusedtypes.html
tas3d=np.atleast_3d(tas).astype('float64')
huss3d=np.atleast_3d(huss).astype('float64')
ps3d=np.atleast_3d(ps).astype('float64')
```

```python
%timeit wb=wetbulb_cython (tas3d, huss3d, ps3d).squeeze()
```

nearly 200 times speed up!

### Jupyter Notebook Exercise: using xarray (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP8/Climate_data_processing_using_xarray_dask_cython_mygeohub.ipynb

# Python Data Processing

Our aim is to calculate wet bulb temperature using CMIP6 data, and then look at its change. We are going to introduce how Cython and Dask will help speed up our code, and how Dask can also help us handle data that are too large to fit in memory.

```python
import xarray as xr
import intake
import numpy as np
from scipy import optimize
from numba import njit, vectorize
import fsspec
xr.set_options(display_style='html') # make the display_style of xarray more user friendly
```

____________
## 1. Read in CMIP6 data in Cloud
____________

```python
col = intake.open_esm_datastore("https://storage.googleapis.com/cmip6/pangeo-cmip6.json")
query = dict(experiment_id=['historical','ssp585'],
             source_id='KACE-1-0-G',
             table_id='3hr',
             variable_id=['tas','huss','ps'],
             member_id = 'r1i1p1f1')
col_subset = col.search(require_all_on=['source_id'], **query)
col_subset.df
```

```python
dset_dict = col_subset.to_dataset_dict(zarr_kwargs={'consolidated': True})
```

```python
list(dset_dict.keys())
```

```python
# we only select the first and last year of this century and compare them
hist=dset_dict['CMIP.NIMS-KMA.KACE-1-0-G.historical.3hr.gr'].sel(time='2000')
ssp=dset_dict['ScenarioMIP.NIMS-KMA.KACE-1-0-G.ssp585.3hr.gr'].sel(time='2100')
```

____________
## 2. Wet bulb temperature calculation using pure python functions
____________
First, we define a set of pure python functions to calculate wet bulb temperature.
References:
- Bolton: *The computation of equivalent potential temperature. Monthly weather review (1980) vol. 108 (7) pp. 1046-1053*
- Davies-Jones: *An efficient and accurate method for computing the wet-bulb temperature along pseudoadiabats. Monthly Weather Review (2008) vol. 136 (7) pp. 2764-2785*

```python
# define some constants
kd = 0.2854
lamda = 3.504
C = 273.15
y0 = 3036.0
y1 = 1.78
y2 = 0.448

# return saturation vapor pressure (Pa)
def esat(Tk):
    # Tk: air temperature (K)
    return 611.2*np.exp(17.67*(Tk-C)*((Tk-29.65)**(-1)))

# return saturation mixing ratio (kg/kg)
def mixrsat(Tk, ps):
    # Tk: air temperature (K)
    return 0.622*esat(Tk)*((ps - esat(Tk))**(-1))

#return vapor pressure (Pa)
def vaporpres(huss, ps):
    #huss: specific humidity (kg/kg)
    #ps: surface pressure (Pa)
    r=huss*((1-huss)**(-1))
    return ps*r*((0.622+r)**(-1))

# return temperature at lifting condensative level
def lcltemp(Tk,e):
    # Tk: air temperature (K)
    # e: vapor pressure (Pa)
    return 2840.0*(( 3.5*np.log(Tk) - np.log(e/100.0) - 4.805)**(-1)) + 55.0
    
# return potential temperature at LCL (K)
def thetadl(Tk, ps, e,Tl,mixr):
    return Tk*((100000*((ps-e)**(-1)))**kd)*((Tk*(Tl**(-1)))**(mixr*0.00028))

# return equivalent potential temperature (K)
def thetae(theta_dl, Tl, mixr):
    return theta_dl*np.exp(((3.036*(Tl**(-1)))-0.00178)*mixr*(1.0 + 0.000448*mixr))

# 1st guess of wet bulb temperature
def wb1stguess(X, D, Teq, ps, pi):
    if X > D:
        rs_teq=mixrsat(Teq,ps)
        dlnes_dTeq = 4302.645*((Teq-29.65)**(-2))
        wb_temp = Teq - ((2675.0*rs_teq)*((1.0 + 2675.0*rs_teq*dlnes_dTeq)**(-1)))
    else:
        k1 = pi*(-38.5*pi+137.81)-53.737
        k2 = pi*(-4.392*pi+56.831)-0.384
        if X>=1.0 and X<=D:
            wb_temp = k1-k2*X+C
        elif X>=0.4 and X<1:
            wb_temp = k1-1.21-(k2-1.21)*X+C
        else:
            wb_temp = k1-2.66-(k2-1.21)*X+0.58*(X**(-1))+C
    return wb_temp
def f(wb, ps, rs_wb):
    G=(y0*(wb**(-1))-y1)*(rs_wb*(1+y2*rs_wb))
    return ((C*(wb**(-1)))**lamda)*(1.0 - esat(wb)*(ps**(-1)))*np.exp(-lamda*G)
def dfdT(wb,ps,rs_wb):
    des_dwb=esat(wb)*4302.645*((wb-29.65)**(-2))
    pminuse = ps - esat(wb)
    rsdT=0.622*ps*(pminuse**(-2))*des_dwb
    dGdT = -y0*(rs_wb+y2*rs_wb*rs_wb)*(wb**(-2))+(y0*(wb**(-1))-y1)*(1.0+2.0*y2*rs_wb)*rsdT
    return -lamda*(wb**(-1)+kd*((pminuse)**(-1))*des_dwb+dGdT)*f(wb,ps,rs_wb)
def fwb(x, C0,C1):
    rs=mixrsat(x,C0)
    ff=f(x,C0,rs)
    df=dfdT(x,C0,rs)
    return (ff - C1)*(df**(-1))

# return wet bulb temperature
def wetbulb_py (Tk, huss, ps, xtol=0.001, rtol=8.881784197001252e-16, mitr=100):
    Tk=np.atleast_3d(Tk)
    huss=np.atleast_3d(huss)
    ps=np.atleast_3d(ps)
    x_max = Tk.shape[0]
    y_max = Tk.shape[1]
    z_max = Tk.shape[2]
    result = np.zeros((x_max, y_max, z_max), dtype=np.float64)
    for i in range(x_max):
        for j in range(y_max):
            for k in range(z_max):
                ps_tmp=ps[i,j,k]
                huss_tmp=huss[i,j,k]
                Tk_tmp=Tk[i,j,k]
                pi = (ps_tmp/100000)**(kd)
                mixr=huss_tmp*((1-huss_tmp)**(-1))*1000
                e=vaporpres(huss_tmp,ps_tmp)
                D = (0.1859*ps_tmp/100000 + 0.6512)**(-1)
                Tl = lcltemp(Tk_tmp,e)
                theta_dl=thetadl(Tk_tmp, ps_tmp, e,Tl,mixr)
                epott = thetae(theta_dl,Tl,mixr)
                Teq = epott*pi
                X = (C*(Teq**(-1)))**lamda
                wb_temp=wb1stguess(X, D, Teq,ps_tmp,pi)
                xa=wb_temp-10
                xb=wb_temp+10
                C0=ps_tmp
                C1=X
                result[i,j,k]=optimize.brentq(fwb, xa, xb, (C0,C1), xtol, rtol, mitr) # use scipy.optimize.brentq
    return result.squeeze()
```

Let's calculate wet bulb temperature for only one time step, and look at how long it takes

```python
tas=hist.tas.squeeze().drop(['height','member_id'])[0,:,:].load()
huss=hist.huss.squeeze().drop(['height','member_id'])[0,:,:].load()
ps=hist.ps.squeeze().drop(['height','member_id'])[0,:,:].load()
```

```python
%time wb=wetbulb_py(tas.values, huss.values, ps.values)
```

____________
## 3. Speed up our pure python code
____________
Pure python code is slow, we are going to use Dask and Cython to speed it up!

## 3.1 Dask
Dask can speed up our code by enable parallel computing. It can also solve the problem of dataset being too large to fit in memory by doing calculations chunk by chunk.

```python
import dask
```

```python
airtemp = xr.tutorial.open_dataset("air_temperature").air
airtemp
```

```python
# we can chunk it to get a dask array
airtemp=airtemp.chunk({'time':500})
# we get a dask array with the interface of xarray
airtemp
```

```python
# we can take off the interface of xarray by calling .data
airtemp.data
```

```python
# we can always rechunk it
airtemp=airtemp.chunk({'time':200})
airtemp
```

```python
# change the unit from Kelvin to degree Celsius 
airtemp_degC=airtemp-273.15
airtemp_degC
```

```python
# Untile we explicitly call load() or compute(), Dask actually didn't do any real calculation
# We are doing the calculations below parallelly. However not much benefit from parallel computing since it's not a big problem
%time airtemp_degC=airtemp_degC.load()
```

#### Dask has two families of task schedulers:
* **Single machine scheduler:** Default scheduler, can only be used on a single machine. If you import Dask, set up a computation, and then call compute, then you will use the single-machine scheduler by default. ***We use single-machine scheduler above by default!***


* **Distributed scheduler:** can run on a single machine or distributed across a cluster, **should be preferred even on a single machine** (offer more diagnostic features). To use the dask.distributed scheduler you must set up a Client

```python
from dask.distributed import Client
client = Client(processes=False)
#client = Client(n_workers=4)
client
```

- **Threads**: One process, multiple threads; good for numeric code that releases the GIL (like NumPy, Pandas, Scikit-Learn, Numba, …)

- **Processes**: several processes (maybe also multiple threads in one process); good for pure Python objects like strings or JSON-like dictionary data that holds onto the GIL; expensive inter-process communication

**Apply customized function to dask arrays chunk by chunk: ```xr.apply_ufunc()```**

```python
# return saturation vapor pressure
def esat(Tk):
    return 611.2*np.exp(17.67*(Tk-273.15)*((Tk-29.65)**(-1)))
```

```python
es=xr.apply_ufunc(esat,airtemp,dask="parallelized",output_dtypes=[float])
es
```

```python
%time es=es.load()
```

**Dask also enable computations across multiple nodes:**
```python
from dask_jobqueue import SLURMCluster # you may choose PBSCluster depending on the job scheduling system
from dask.distributed import Client
cluster = SLURMCluster( # setup for one node
    queue="huberm",
    cores=24,
    processes=1,
    local_directory='/tmp',
    project="huberm",
    memory="80 GB",
    walltime="00:30:00",
    interface='ib0' # choose the faster network
)

client=Client(cluster)
cluster.scale(5) # ask for 5 nodes
cluster.adapt(minimum=2, maximum=10) # dask also enable adapative deployments according to the work load
```

**Tips on using Dask**:

- Familiarize yourself with [Dask best practices](https://docs.dask.org/en/latest/array-best-practices.html).

- Don’t use Dask! Or more specifically, only use a distributed cluster if you really need it, i.e. if your calculations are running out of memory or are taking an unacceptably long time to complete.

- Start small; work on a small subset of your problem to debug before scaling up to a very large dataset.

- If you use a distributed cluster, use adapative mode rather than a fixed size cluster; this will help share resources more effectively.

- Use the Dask dashboard heavily to monitor the activity of your cluster.
- Tips about chunk
  - small enough so that many chunks can fit in memory at once
  - large enough to avoid overhead (rare to see chunk size below 100MB)
  - the way we chunk matters; if we often slice along 'time' dimension, it's better to chunk along it.
- avoid too many tasks
  - every task comes with overhead (200us ~ 1ms);  millions of tasks lead to overhead of 10 minutes ~ hours
  - easy to create too many tasks: ```array_a+1``` can create many new tasks
  - avoid too small chunks
  - Fusing operations together and use ```xr.apply_ufunc()```

## 3.2 Cython
Cython speed up our python code by compiling it into machine code. If you want to know more about the detail, please see our video about using cython to speed up python code

Numba's ```@njit``` decorator did similar thing. However, it won't work in this case.

```python
import cython
%load_ext Cython
```

our cython version function

```python
%%cython -a --compile-args=-Ofast --compile-args=-fopenmp --link-args=-fopenmp
import numpy as np
cimport numpy as np
cimport cython
from libc cimport math
from cython.parallel import prange
from scipy.optimize.cython_optimize cimport brentq
    
cdef double kd,lamda, C, y0, y1, y2
kd = 0.2854
lamda = 3.504
C = 273.15
y0 = 3036.0
y1 = 1.78
y2 = 0.448


ctypedef struct wb_params:
    double C0
    double C1

cdef double esat(double Tk) nogil:
    return 611.2*math.exp(17.67*(Tk-C)*((Tk-29.65)**(-1)))

cdef double mixrsat(double Tk,double ps) nogil:
    return 0.622*esat(Tk)*((ps - esat(Tk))**(-1))

cdef double vaporpres(double huss, double ps) nogil:
    cdef double r
    r=huss*((1-huss)**(-1))
    return ps*r*((0.622+r)**(-1))

cdef double lcltemp(double Tk,double e) nogil:
    return 2840.0*(( 3.5*math.log(Tk) - math.log(e/100.0) - 4.805)**(-1)) + 55.0

cdef double thetadl(double Tk, double ps, double e,double Tl,double mixr) nogil:
    return Tk*((100000*((ps-e)**(-1)))**kd)*((Tk*(Tl**(-1)))**(mixr*0.00028))

cdef double thetae(double theta_dl, double Tl, double mixr) nogil:
    return theta_dl*math.exp(((3.036*(Tl**(-1)))-0.00178)*mixr*(1.0 + 0.000448*mixr))

cdef double wb1stguess(double X, double D, double Teq, double ps, double pi) nogil:
    cdef double rs_teq, dlnes_dTeq, wb_temp, k1, k2
    if X > D:
        rs_teq=mixrsat(Teq,ps)
        dlnes_dTeq = 4302.645*((Teq-29.65)**(-2))
        wb_temp = Teq - ((2675.0*rs_teq)*((1.0 + 2675.0*rs_teq*dlnes_dTeq)**(-1)))
    else:
        k1 = pi*(-38.5*pi+137.81)-53.737
        k2 = pi*(-4.392*pi+56.831)-0.384
        if X>=1.0 and X<=D:
            wb_temp = k1-k2*X+C
        elif X>=0.4 and X<1:
            wb_temp = k1-1.21-(k2-1.21)*X+C
        else:
            wb_temp = k1-2.66-(k2-1.21)*X+0.58*(X**(-1))+C
    return wb_temp

cdef double f(double wb, double ps, double rs_wb) nogil:
    cdef double G
    G=(y0*(wb**(-1))-y1)*(rs_wb*(1+y2*rs_wb))
    return ((C*(wb**(-1)))**lamda)*(1.0 - esat(wb)*(ps**(-1)))*math.exp(-lamda*G)

cdef double dfdT(double wb,double ps,double rs_wb) nogil:
    cdef double des_dwb, pminus, rsdT, dGdT
    des_dwb=esat(wb)*4302.645*((wb-29.65)**(-2))
    pminuse = ps - esat(wb) #pminus in Pa
    rsdT=0.622*ps*(pminuse**(-2))*des_dwb
    dGdT = -y0*(rs_wb+y2*rs_wb*rs_wb)*(wb**(-2))+(y0*(wb**(-1))-y1)*(1.0+2.0*y2*rs_wb)*rsdT
    return -lamda*(wb**(-1)+kd*((pminuse)**(-1))*des_dwb+dGdT)*f(wb,ps,rs_wb)

cdef double fwb(double x, void *args) nogil:
    cdef wb_params *myargs = <wb_params *> args
    cdef double rs,ff,df
    rs=mixrsat(x,myargs.C0)
    ff=f(x,myargs.C0,rs)
    df=dfdT(x,myargs.C0,rs)
    return (ff - myargs.C1)*(df**(-1))

cdef double wb_brentq_wrapper(wb_params args, double xa, double xb, double xtol, double rtol, int mitr) nogil:
    return brentq(fwb, xa, xb, <wb_params *> &args, xtol, rtol, mitr, NULL)

@cython.wraparound(False)
@cython.boundscheck(False)
def wetbulb_cython (const double[:,:,:] Tk, const double[:,:,:] huss, const double[:,:,:] ps, double xtol=0.001, double rtol=0.0, int mitr=100000):
    cdef const double[:, :, ::1] Tk_view=Tk.copy()
    cdef const double[:, :, ::1] huss_view=huss.copy()
    cdef const double[:, :, ::1] ps_view=ps.copy()
    cdef Py_ssize_t i, j, k, x_max, y_max, z_max
    x_max = Tk_view.shape[0]
    y_max = Tk_view.shape[1]
    z_max = Tk_view.shape[2]
    result = np.zeros((x_max, y_max, z_max), dtype=np.float64)
    cdef double[:, :, ::1] result_view = result
    cdef double xa,xb,ps_tmp,huss_tmp,Tk_tmp,pi, mixr,e, D,Tl,theta_dl,epott,Teq,X,wb_temp
    cdef wb_params args
    for i in prange(x_max,nogil=True):
        for j in range(y_max):
            for k in range(z_max):
                ps_tmp=ps_view[i,j,k]
                huss_tmp=huss_view[i,j,k]
                Tk_tmp=Tk_view[i,j,k]
                pi = (ps_tmp/100000)**(kd)
                mixr=huss_tmp*((1-huss_tmp)**(-1))*1000 #mixing ratio (g/kg)
                e=vaporpres(huss_tmp,ps_tmp)
                D = (0.1859*ps_tmp/100000 + 0.6512)**(-1)
                Tl = lcltemp(Tk_tmp,e)
                theta_dl=thetadl(Tk_tmp, ps_tmp, e,Tl,mixr)
                epott = thetae(theta_dl,Tl,mixr)
                Teq = epott*pi
                X = (C*(Teq**(-1)))**lamda
                wb_temp=wb1stguess(X, D, Teq,ps_tmp,pi)
                xa=wb_temp-10
                xb=wb_temp+10
                args.C0=ps_tmp
                args.C1=X
                result_view[i,j,k]=wb_brentq_wrapper(args, xa, xb, xtol, rtol, mitr)
    return result
```

```python
# our cython function require 3D output of double type. But we can be more flexible by for example fused type in Cython
# Introduction to fused type: https://cython.readthedocs.io/en/latest/src/userguide/fusedtypes.html
tas3d=np.atleast_3d(tas).astype('float64')
huss3d=np.atleast_3d(huss).astype('float64')
ps3d=np.atleast_3d(ps).astype('float64')
```

calculate again using cython version function

```python
%time wb=wetbulb_cython(tas3d, huss3d, ps3d).squeeze()
```

____________
## 4. Combine both Cython and Dask to compute wet bulb temperature
____________

```python
# access each variable for year 2000
tas_hist=hist.tas.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
huss_hist=hist.huss.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
ps_hist=hist.ps.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
# access each variable for year 2100
tas_ssp=ssp.tas.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
huss_ssp=ssp.huss.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
ps_ssp=ssp.ps.squeeze().drop(['member_id','height']).astype('float64').chunk({'time':200})
```

```python
wb_hist=xr.apply_ufunc(wetbulb_cython, tas_hist, huss_hist, ps_hist,dask="parallelized",output_dtypes=[float])
wb_hist
```

```python
# you can directly write the result into disk chunk by chunk
%time wb_hist=wb_hist.load()
```

```python
wb_ssp=xr.apply_ufunc(wetbulb_cython, tas_ssp, huss_ssp, ps_ssp,dask="parallelized",output_dtypes=[float])
wb_ssp
```

```python
%time wb_ssp=wb_ssp.load()
```

```python
wb_ssp.to_netcdf('./wb_ssp.nc')
wb_hist.to_netcdf('./wb_hist.nc')
```

____________
## 5. calculate changes in annual mean and 95th percentile of wet bulb temperature
____________

```python
# calculate changes in annual mean wet bulb temperature
mean_diff=wb_ssp.mean('time')-wb_hist.mean('time')
# calculate changes in annual 95th percentile of wet bulb temperature
q95_diff=(wb_ssp.chunk({'time':-1}).quantile([0.95], 'time')-wb_hist.chunk({'time':-1}).quantile([0.95], 'time')).squeeze().drop(['quantile'])
# rename the xarray DataArray, otherwise it would have the same name and cannot be merged
mean_diff.name='mean_diff'
q95_diff.name='q95_diff'
```

```python
output=xr.merge([mean_diff,q95_diff])
output
```

```python
output.to_netcdf('./output.nc')
```
