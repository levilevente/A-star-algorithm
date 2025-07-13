import plotly.graph_objects as plotly_graph_objects
import math as mat
import heapq


class Point:
    def __init__(self, x, y, z, b):
        self.x = x
        self.y = y
        self.z = z
        self.b = b

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}, {self.b})'


class Coordinates:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distance(c1, c2):
        return mat.sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2 + (c2.z - c1.z) ** 2)


class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = float('inf')
        self.z = 0


def readFileMap(filename, sizex, sizey):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"File {filename} not found")
        exit(1)
    matrix = [[0] * sizex for _ in range(sizey)]
    for line in f.readlines():
        fields = line.split(' ')
        matrix[int(fields[0])][int(fields[1])] = Point(int(fields[0]), int(fields[1]), float(fields[2]), int(fields[3]))
    f.close()

    return matrix


def readFileStartEnd(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"File {filename} not found")
        exit(1)
    start = f.readline()
    start_x_y = start.split(" ")
    start_x = int(start_x_y[0])
    start_y = int(start_x_y[1])
    stop = f.readline()
    stop_x_y = stop.split(" ")
    stop_x = int(stop_x_y[0])
    stop_y = int(stop_x_y[1])
    return start_x, start_y, stop_x, stop_y


def calcPathWriteToFile(matrix, final_path1, final_path2):
    x_path1 = []
    y_path1 = []
    z_path1 = []

    x_path2 = []
    y_path2 = []
    z_path2 = []

    dist1 = 0
    ok = False
    fout = open("Eredmenyek_a.txt", "w")
    for i in final_path1:
        x_path1.append(matrix[i[0]][i[1]].x)
        y_path1.append(matrix[i[0]][i[1]].y)
        z_path1.append(matrix[i[0]][i[1]].z)
        fout.write(
            str(matrix[i[0]][i[1]].x) + " " + str(matrix[i[0]][i[1]].y) + " " + str(matrix[i[0]][i[1]].z) + "\n")

        if not ok:
            ok = True
            j = i

        else:
            dist1 += h_euclides(Point(matrix[j[0]][j[1]].x, matrix[j[0]][j[1]].y, matrix[j[0]][j[1]].z, 0), Point(matrix[i[0]][i[1]].x, matrix[i[0]][i[1]].y, matrix[i[0]][i[1]].z, 0))
            j = i
    fout.write("Az ut koltsege a) " + str(dist1))
    fout.writelines("\n")

    dist2 = 0
    ok = False

    fout = open("Eredmenyek_b.txt", "w")
    for i in final_path2:
        x_path2.append(matrix[i[0]][i[1]].x)
        y_path2.append(matrix[i[0]][i[1]].y)
        z_path2.append(matrix[i[0]][i[1]].z)
        fout.write(
            str(matrix[i[0]][i[1]].x) + " " + str(matrix[i[0]][i[1]].y) + " " + str(matrix[i[0]][i[1]].z) + "\n")

        if not ok:
            ok = True
            j = i
        else:
            dist2 += 1
            j = i
    fout.write("Az ut koltsege b) " + str(dist2))
    fout.writelines("\n")

    fout.close()
    print(f"a) {dist1}\nb) {dist2}\n")


def draw3d(matrix, final_path1, final_path2, title):  # drawing the path and the map and write the result in a file

    x_path1 = []
    y_path1 = []
    z_path1 = []

    x_path2 = []
    y_path2 = []
    z_path2 = []

    x = []
    y = []
    z = []

    x_obstacle = []
    y_obstacle = []
    z_obstacle = []
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            b = matrix[i][j].b
            if not b:
                x.append(matrix[i][j].x)
                y.append(matrix[i][j].y)
                z.append(matrix[i][j].z)
            else:
                x_obstacle.append(matrix[i][j].x)
                y_obstacle.append(matrix[i][j].y)
                z_obstacle.append(matrix[i][j].z)

    for i in final_path1:
        x_path1.append(matrix[i[0]][i[1]].x)
        y_path1.append(matrix[i[0]][i[1]].y)
        z_path1.append(matrix[i[0]][i[1]].z)

    for i in final_path2:
        x_path2.append(matrix[i[0]][i[1]].x)
        y_path2.append(matrix[i[0]][i[1]].y)
        z_path2.append(matrix[i[0]][i[1]].z)

    scatter_path1 = plotly_graph_objects.Scatter3d(
        x=x_path1,
        y=y_path1,
        z=z_path1,
        mode='markers',
        marker=dict(
            size=5,
            color='blue',
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    scatter_path2 = plotly_graph_objects.Scatter3d(
        x=x_path2,
        y=y_path2,
        z=z_path2,
        mode='markers',
        marker=dict(
            size=5,
            color='orange',
            colorscale='Viridis',
            opacity=0.8
        ),
    )
    scatter_non_obstacle = plotly_graph_objects.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=5,
            color=z,
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    scatter_obstacle = plotly_graph_objects.Scatter3d(
        x=x_obstacle,
        y=y_obstacle,
        z=z_obstacle,
        mode='markers',
        marker=dict(
            size=5,
            color='red',
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    layout = plotly_graph_objects.Layout(
        scene=dict(
            xaxis=dict(title='X Label'),
            yaxis=dict(title='Y Label'),
            zaxis=dict(title='Z Label')
        )
    )

    fig = plotly_graph_objects.Figure(data=[scatter_non_obstacle, scatter_obstacle, scatter_path1, scatter_path2], layout=layout)
    fig.update_layout(title_text=title)
    fig.show()


def draw2d(matrix, final_path1, final_path2, title):
    x = []
    y = []
    z = []
    x_obstacle = []
    y_obstacle = []
    z_obstacle = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            b = matrix[i][j].b
            if not b:
                x.append(matrix[i][j].x)
                y.append(matrix[i][j].y)
                z.append(matrix[i][j].z)
            else:
                x_obstacle.append(matrix[i][j].x)
                y_obstacle.append(matrix[i][j].y)
                z_obstacle.append(matrix[i][j].z)

    x_path1 = []
    y_path1 = []
    z_path1 = []

    x_path2 = []
    y_path2 = []
    z_path2 = []

    for i in final_path1:
        x_path1.append(matrix[i[0]][i[1]].x)
        y_path1.append(matrix[i[0]][i[1]].y)
        z_path1.append(matrix[i[0]][i[1]].z)

    for i in final_path2:
        x_path2.append(matrix[i[0]][i[1]].x)
        y_path2.append(matrix[i[0]][i[1]].y)
        z_path2.append(matrix[i[0]][i[1]].z)

    scatter_path1 = plotly_graph_objects.Scatter(
        x=x_path1,
        y=y_path1,
        mode='markers',
        marker=dict(
            size=8,
            color='blue',
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    scatter_path2 = plotly_graph_objects.Scatter(
        x=x_path2,
        y=y_path2,
        mode='markers',
        marker=dict(
            size=8,
            color='orange',
            colorscale='Viridis',
            opacity=0.8
        ),
    )
    scatter_non_obstacle = plotly_graph_objects.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(
            size=8,
            color=z,
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    scatter_obstacle = plotly_graph_objects.Scatter(
        x=x_obstacle,
        y=y_obstacle,
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            colorscale='Viridis',
            opacity=0.8
        ),
    )

    layout = plotly_graph_objects.Layout(
        xaxis=dict(title='X Label'),
        yaxis=dict(title='Y Label'),
    )

    fig = plotly_graph_objects.Figure(data=[scatter_non_obstacle, scatter_obstacle, scatter_path1, scatter_path2], layout=layout)
    fig.update_layout(title_text=title)
    fig.show()


def is_valid(row, col, ROW, COL):  # the coordinate is still in the range
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


def is_free(matrix, row, col):  # the coordinate was not an obstacle
    return matrix[row][col].b == 0


def is_destionation(row, col, end):  # check if the gived coordinate is the end(finish) coordinate
    return row == end.x and col == end.y


def h_csebisev(a, b):  # the distance between two Points for b) where the distance between two neighbours is 1.0
    return max(abs(a.x - b.x), abs(a.y - b.y))


def h_euclides(start, end):  # the euclides distance between two points
    return Coordinates.distance(start, end)


def trace_path(point_details, end):  # using the parent field of the point_detail, we can easly read the final path
    path = []
    row = end.x
    col = end.y
    while not (point_details[row][col].parent_i == row and point_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = point_details[row][col].parent_i
        temp_col = point_details[row][col].parent_j
        row = temp_row
        col = temp_col

    path.append((row, col))
    path.reverse()  # because we read the path from end->start we need to reverse the list
    final_path = []
    for i in path:
        final_path.append(i)
    return final_path


def a_star(matrix, start, end, h):
    closed_list = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    point_details = [[Cell() for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    actual_x = start.x
    actual_j = start.y
    point_details[actual_x][actual_j].f = 0
    point_details[actual_x][actual_j].g = 0
    point_details[actual_x][actual_j].h = 0
    point_details[actual_x][actual_j].parent_i = actual_x
    point_details[actual_x][actual_j].parent_j = actual_j
    point_details[actual_x][actual_j].z = matrix[actual_x][actual_j].z

    open_list = []
    heapq.heappush(open_list, (0.0, actual_x, actual_j))

    while len(open_list) > 0:
        p = heapq.heappop(open_list)
        actual_x = p[1]
        actual_j = p[2]

        closed_list[actual_x][actual_j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # the 8 directions where we can go
        for dir in directions:
            neighbour_x = actual_x + dir[0]
            neighbour_y = actual_j + dir[1]

            # if the neighbour is not an obstacle, and it is not outside the map, and
            # it is not yet discovered
            if is_valid(neighbour_x, neighbour_y, len(matrix), len(matrix[1])) and is_free(matrix, neighbour_x, neighbour_y) and not closed_list[neighbour_x][neighbour_y]:
                # if we arrived at the destination it means we have a path, so we stop
                if is_destionation(neighbour_x, neighbour_y, end):
                    point_details[neighbour_x][neighbour_y].parent_i = actual_x
                    point_details[neighbour_x][neighbour_y].parent_j = actual_j
                    point_details[neighbour_x][neighbour_y].z = matrix[actual_x][actual_j].z
                    return trace_path(point_details, end)
                else:
                    # otherwise we continue the search using the heuristical values
                    g_new = point_details[actual_x][actual_j].g + h(Point(neighbour_x, neighbour_y, matrix[neighbour_x][neighbour_y].z, 0), Point(actual_x, actual_j, matrix[actual_x][actual_j].z, 0))
                    h_new = h(Point(neighbour_x, neighbour_y, matrix[neighbour_x][neighbour_y].z, 0), end)
                    f_new = g_new + h_new
                    # if the new point was not yet discovered OR the new mini path was shorter than the previous it means we need to keep the new point in the path
                    if point_details[neighbour_x][neighbour_y].f == float('inf') or point_details[neighbour_x][neighbour_y].f > f_new:
                        heapq.heappush(open_list, (f_new, neighbour_x, neighbour_y))
                        point_details[neighbour_x][neighbour_y].parent_i = actual_x
                        point_details[neighbour_x][neighbour_y].parent_j = actual_j
                        point_details[neighbour_x][neighbour_y].f = f_new
                        point_details[neighbour_x][neighbour_y].g = g_new
                        point_details[neighbour_x][neighbour_y].h = h_new
                        point_details[neighbour_x][neighbour_y].z = matrix[neighbour_x][neighbour_y].z

    print("Failed to find the route 66")
    return None


def main():
    print("Give me the surface file name: ")
    surface_file = input()
    print("Give me the end points file name: ")
    end_points_file = input()
    print("Give me the size of the matrix (nxn): ")
    n = int(input("n = "))
    matrix = readFileMap(surface_file, n, n)

    start_x, start_y, stop_x, stop_y = readFileStartEnd(end_points_file)
    start = matrix[start_x][start_y]
    stop = matrix[stop_x][stop_y]

    final_path1 = a_star(matrix, start, stop, h_euclides)
    final_path2 = a_star(matrix, start, stop, h_csebisev)
    calcPathWriteToFile(matrix, final_path1, final_path2)
    draw3d(matrix, final_path1, final_path2, "3D")
    draw2d(matrix, final_path1, final_path2, "2D")


main()
