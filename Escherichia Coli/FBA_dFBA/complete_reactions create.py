import numpy

complete_reactions = numpy.array([[ 2,   'PPS'   ],
                                  [ 3.0, 'LDH_D' ],
                                  [ 3.1, 'LDH_D2'],
                                  [ 5,   'PFL'   ],
                                  [ 6,   'PDH'   ],
                                  [ 7,   'POX'   ],
                                  [ 9,   'PTAr'  ],
                                  [10,   'ACKr'  ],
                                  [11,   'ALCD2x'],
                                  [12.0, 'FRD2'  ],
                                  [12.1, 'FRD3'  ]], 'object')

numpy.save(open('complete_reactions.npy', 'wb'), complete_reactions)