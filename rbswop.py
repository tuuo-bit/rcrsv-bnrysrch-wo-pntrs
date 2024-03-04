# Recurs_ve b_nary search w_thout po_nters (only time _'ll be using i&j)
# to return _ndex of element from (None _n case not from) a sorted array.

def b_narySearch( arr, ele, _ndex=0):
    if len( arr) == 1 and arr[ 0] != ele:
        return
    elif ele in arr:
        m_d = len( arr) // 2
        if arr[ m_d] == ele:
            _ndex += m_d
            return _ndex
        elif arr[ m_d] > ele:
            return b_narySearch( arr[:m_d], ele, _ndex)
        elif arr[ m_d] < ele:
            _ndex += m_d
            return b_narySearch( arr[m_d:], ele, _ndex)
    else:
        return
