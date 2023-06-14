import numpy

complete_genes = numpy.array([[ 2,   'b1702'],
                              [ 3.0, 'b1380'],
                              [ 3.1, 'b2133'],
                              [ 5.0, 'b0902'],
                              [ 5.1, 'b0903'],
                              [ 6,   'b0114'],
                              [ 7,   'b0871'],
                              [ 9,   'b2297'],
                              [10,   'b2296'],
                              [11,   'b1241'],
                              [12,   'b4154']])

numpy.save(open('complete_genes.npy', 'wb'), complete_genes)