import numpy

# remember: make it work first, then make it understandable and efficient. (That means using numba!)

def tensor_centre_gradient(tensor: numpy.ndarray, h: float = 1.0):
    output = numpy.zeros((tensor.ndim, *tensor.shape))
    padded = numpy.pad(tensor, 1, mode='edge')

    for dimension in range(tensor.ndim):
        forward = numpy.roll(padded, -1, axis=dimension)
        backward = numpy.roll(padded, 1, axis=dimension)

        trim = tuple(slice(1, -1) for _ in range(tensor.ndim))
        forward = forward[trim]
        backward = backward[trim]

        output[dimension] = (forward - backward) / (2 * h)

    return output

def tensor_centre_hessian(tensor: numpy.ndarray, h: float = 1.0):
    n = tensor.ndim
    output = numpy.zeros((n, n, *tensor.shape))
    padded = numpy.pad(tensor, 1, mode='edge')
    trim = tuple(slice(1, -1) for _ in range(n))

    for i in range(n):
        for j in range(n):
            if i == j:
                # diagonal: standard second derivative along one axis
                forward = numpy.roll(padded, -1, axis=i)[trim]
                backward = numpy.roll(padded, 1, axis=i)[trim]
                output[i, j] = (forward + backward - 2 * tensor) / (h ** 2)
            else:
                # off-diagonal: mixed partial, via 4 diagonal-neighbour shifts
                pp = numpy.roll(numpy.roll(padded, -1, axis=i), -1, axis=j)[trim]
                pm = numpy.roll(numpy.roll(padded, -1, axis=i), 1, axis=j)[trim]
                mp = numpy.roll(numpy.roll(padded, 1, axis=i), -1, axis=j)[trim]
                mm = numpy.roll(numpy.roll(padded, 1, axis=i), 1, axis=j)[trim]
                output[i, j] = (pp - pm - mp + mm) / (4 * h ** 2)

    return output

def tensor_centre_laplacian(tensor: numpy.ndarray, h: float = 1.0):
    output = numpy.zeros_like(tensor)
    padded = numpy.pad(tensor, 1, mode='edge')
    trim = tuple(slice(1, -1) for _ in range(tensor.ndim))

    for dimension in range(tensor.ndim):
        forward = numpy.roll(padded, -1, axis=dimension)[trim]
        backward = numpy.roll(padded, 1, axis=dimension)[trim]

        output += (forward + backward - 2 * tensor) / (h ** 2)

    return output