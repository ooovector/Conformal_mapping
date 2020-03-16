import numpy as np
from scipy.constants import epsilon_0
epsilon=11.75

class Conformal_mapping:

    def __init__(self, _points):

        self._points=_points

    def Give_me_result(self):
        Points=self._points
        Shape_of_matrix=(len(Points)-2)/2
        print('Shape of matrix=', Shape_of_matrix)

        '''
        This function helps find numerator and denumerator points
        '''

        def Create_numerator_and_denumerator_points(points):
            shape_of_matrix=(len(points)-2)/2
            #len(points)
            #print('Shape of matrix=', shape_of_matrix)
            create_numerator_points=np.zeros(int(shape_of_matrix)-1)
            create_denumerator_points=np.zeros(len(points)-(int(shape_of_matrix)-1))
            j=0
            if shape_of_matrix > 1:
                for i in range(len(create_numerator_points)):
                    create_numerator_points[i]=points[j+2]
                    j=j+2
            else:
                create_numerator_points=None

            if shape_of_matrix > 1:

                create_denumerator_points[0]=points[0]
                create_denumerator_points[1]=points[1]

                create_denumerator_points[len(create_denumerator_points)-1]=points[len(points)-1]
                create_denumerator_points[len(create_denumerator_points)-2]=points[len(points)-2]
                create_denumerator_points[len(create_denumerator_points)-3]=points[len(points)-3]

                k=3
                for i in range(2, len(create_denumerator_points)-3):
                    create_denumerator_points[i]=points[k]
                    k=k+2
            else:
                 for i in range(len(create_denumerator_points)):
                        create_denumerator_points[i]=points[i]

            numerator_points=create_numerator_points
            denumerator_points=create_denumerator_points

            #print('Numerator points', numerator_points)
            #print('Deumerator points', denumerator_points)

            return numerator_points, denumerator_points

        Numerator_points=Create_numerator_and_denumerator_points(Points)[0]
        Denumerator_points=Create_numerator_and_denumerator_points(Points)[1]

        '''
        This function create lists of points
        '''

        def Function_for_points(points):
            shape_of_matrix=(len(points)-2)/2

            list_of_points=[points]
            new_points=points

            if shape_of_matrix > 1:
                for i in range(1,int(shape_of_matrix)):
                    n=2

                    points_part1=new_points[0:n]
                    points_part2=new_points[n:len(new_points)]

                    changed_points=np.concatenate((points_part2, points_part1), axis=0)
                    list_of_points.append(changed_points)
                    new_points=changed_points
            else:
                list_of_points=[points]


            return list_of_points

        List_of_points=Function_for_points(Points)

        '''
        This function counts Gauss-Chebyshev integral
        '''

        def GaussChebyshev(numerator_points, denumerator_points, limits, n=100):
            x = np.cos((2*np.arange(n)+1)*np.pi/(2*n))*(limits[1]-limits[0])*0.5+np.mean(limits)
            y = np.ones(x.shape, np.complex)
            for p in numerator_points:
                y *= np.sqrt(np.abs(x-p))
                if x[0]<p:
                    y *= 1j
            for p in denumerator_points:
                y /= np.sqrt(np.abs(x-p))
                if x[0]<p:
                    y *= -1j
            return np.sum(y)*np.pi/n

        '''
        Main part
        '''

        Matrix_Phi=np.zeros((int(Shape_of_matrix), int(Shape_of_matrix)))
        Matrix_Q=np.zeros((int(Shape_of_matrix), int(Shape_of_matrix)))

        for i in range(int(Shape_of_matrix)):
            for i in range(int(Shape_of_matrix)):
                List=Function_for_points(Points)[i]
                Numerator_points=Create_numerator_and_denumerator_points(List)[0]
                Denumerator_points=Create_numerator_and_denumerator_points(List)[1]
                #Limits=





        def Create_matrix_Q():
            print('Q')
            return None

        def Create_matrix_Phi(points):

            print('Phi')
            return list


        Q=Create_matrix_Phi(Points)


        return List_of_points
