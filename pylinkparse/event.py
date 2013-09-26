# Authors: Denis Engemann <d.engemann@fz-juelich.de>
#
# License: BSD (3-clause)

import numpy as np


def find_custom_events(raw, pattern, prefix=True, sep=' '):
    """Find arbitrary messages
    Parameters
    ----------
    raw : instance of pylinkparse.raw.Raw
        the raw file to find events in.
    pattern : str
        A substring to be matched
    prefix : bool
        Whether the message includes a prefix, e.g., MSG or
        directly begins with the time sample.
    sep : str
        The separator.

    Returns
    -------
    idx : instance of numpy.ndarray
        The indices found.
    """
    events = []

    idx = 1 if prefix else 0
    with open(raw.info['fname']) as fid:
        for line in fid:
            if pattern in line:
                events.append(line.split(sep)[idx])
    events = np.array(events, dtype='f8')
    events -= raw._t_zero
    events /= 1e3
    print events
    return np.nonzero(np.in1d(raw._samples['time'], events))[0]