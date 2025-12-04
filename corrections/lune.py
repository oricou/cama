def mat_lune(t):
    ''' should return a matrix such that
        pos = (mat_lune(t) @ np.array([150934, 0, 1]))[:2]
    '''
    sol_terre, periode_terre = 150550., 365.
    terre_lune, periode_lune = 384., 29.
    rotation = lambda a: np.array([[np.cos(a), -np.sin(a),0], [np.sin(a), np.cos(a),0],[0,0,1]])
    translation = lambda x,y: np.array([[1,0,x], [0,1,y], [0,0,1]])
    a_terre = 2*np.pi / (periode_terre / t)
    a_lune = 2*np.pi / (periode_lune / t)
    return  rotation(a_terre) @ translation(sol_terre,0) @ rotation(a_lune) @ translation(-sol_terre, 0)

