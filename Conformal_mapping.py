import numpy as np
from scipy.constants import epsilon_0
epsilon=11.75

def create_numerator_and_denumerator_points(points):
    '''
    This function helps find numerator and denumerator points
    '''
    numerator_point_ids = [p for p in np.arange(2,len(points)-2,2)]
    denumerator_point_ids = [p for p in range(len(points)) if p not in numerator_point_ids]
    
    numerator_points = np.asarray(points)[numerator_point_ids]
    denumerator_points = np.asarray(points)[denumerator_point_ids]
    
    return numerator_points, denumerator_points

def function_for_points(points):
    '''
    This function create lists of points
    '''
    result = []
    for i in range(0, len(points)-2, 2):
        result.append(np.roll(points, -i))
    return result


def gauss_chebyshev(numerator_points, denumerator_points, limits, n=100):
    '''
    This function counts Gauss-Chebyshev integral
    '''

    x = np.cos((2*np.arange(n)+1)*np.pi/(2*n))*(limits[1]-limits[0])*0.5+np.mean(limits)
    #y = np.ones(x.shape, np.complex)
    y = np.ones(x.shape)

    for p in numerator_points:
        y *= np.sqrt(np.abs(x-p))
        #if x[0]<p:
            #y *= 1j
    for p in denumerator_points:
        y /= np.sqrt(np.abs(x-p))
        #if x[0]<p:
            #y *= -1j

    return np.sum(y)*np.pi/n


class ConformalMapping:

    def __init__(self, points):
        self.points=points

    def cl(self):
        '''
        Main part
        '''
        shape_of_matrix=(len(self.points)-2)/2
        print('Shape of matrix=', shape_of_matrix)

        numerator_points, denumerator_points = create_numerator_and_denumerator_points(self.points)

        list_of_points=function_for_points(self.points)

        Phi=np.zeros((int(shape_of_matrix), int(shape_of_matrix)))
        Q=np.zeros((int(shape_of_matrix), int(shape_of_matrix)))

        if shape_of_matrix > 1:

            '''
            This part makes Phi matrix
            '''
            for i in range(int(shape_of_matrix)):
                list_=function_for_points(self.points)[i]
                numerator_points, denumerator_points =create_numerator_and_denumerator_points(list_)



                for j in range(int(shape_of_matrix)):
                    limits=[denumerator_points[0], denumerator_points[j+1]]

                    points_part1=denumerator_points[1 : j+1]
                    points_part2=denumerator_points[j+2 : len(denumerator_points)]

                    denumerator_points_=np.concatenate((points_part1, points_part2), axis=0)

                    Phi[j][i]=gauss_chebyshev(numerator_points, denumerator_points_, limits)

                    print(Phi[j][i])

            '''
            This part makes Q matrix
            '''

            for i in range(int(shape_of_matrix)):
                list_=function_for_points(self.points)[i]
                numerator_points, denumerator_points =create_numerator_and_denumerator_points(list_)



                for j in range(int(shape_of_matrix)):
                    limits=[denumerator_points[0], denumerator_points[j+2]]

                    points_part1=denumerator_points[1 : j+2]
                    points_part2=denumerator_points[j+3 : len(denumerator_points)]

                    denumerator_points_=np.concatenate((points_part1, points_part2), axis=0)

                    Q[j][i]=gauss_chebyshev(numerator_points, denumerator_points_, limits)

                    print(Q[j][i])

            Phi_inv=np.linalg.inv(Phi)

            C=epsilon_0*epsilon*Q*Phi_inv

        else:


            limits1=[denumerator_points[0], denumerator_points[1]]

            limits2=[denumerator_points[1], denumerator_points[2]]

            print (denumerator_points, limits1, limits2)
            Phi=gauss_chebyshev([], denumerator_points, limits1)
            Q=gauss_chebyshev([], denumerator_points, limits2)


            C=epsilon_0*epsilon*Q/Phi

        print('Phi= ', Phi)
        print('Q= ', Q)
        print('C= ', C)

        return Phi, Q, C
