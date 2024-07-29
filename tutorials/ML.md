# Tensorflow vs pyTorch
Both are open-source Python libraries that use graphs to perform numerical computations on data in deep learning applications.

## tensor
In mathematics, a tensor is an algebraic object that describes a multilinear relationship between sets of algebraic objects related to a vector space. 

## What Is TensorFlow?
TensorFlow was developed by Google and released as open-source in 2015. It grew out of Google’s homegrown machine learning software, which was refactored and optimized for use in production.
The name “TensorFlow” describes how you organize and perform operations on data. The basic data structure for both TensorFlow and PyTorch is a tensor. When you use TensorFlow, you perform operations on the data in these tensors by building a stateful dataflow graph, kind of like a flowchart that remembers past events.

* example of multiplying tensors
```
>>> import tensorflow as tf

>>> x = [[2., 4., 6.]]         # tensor 
>>> y = [[1.], [3.], [5.]]     # tensor
>>> m = tf.math.multiply(x, y) # it does element-wise multiplication

>>> m
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[ 2.,  4.,  6.],
       [ 6., 12., 18.],
       [10., 20., 30.]], dtype=float32)>
```

## 