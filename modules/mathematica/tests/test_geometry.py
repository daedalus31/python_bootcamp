from geometry.figures import square_area, triangle_area


def test_square_area():
    square_edge_length = 9
    assert square_area(square_edge_length) == 81


def test_triangle_area():
    assert triangle_area(10, 5) == 25
