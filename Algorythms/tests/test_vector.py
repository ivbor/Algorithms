from Algorythms.python_solutions import vector


def test_can_create_vector_and_len_exists():
    vec = vector.Vector(size=0, capacity=1)
    assert len(vec) == 0, len(vec)

    vec = vector.Vector(capacity=4)
    assert len(vec) == 0, len(vec)

    vec = vector.Vector([1, 2, 3, 4])
    assert len(vec) == 4, len(vec)
    assert vec.size == len(vec), vec.size
    assert vec.capacity == 8, vec.capacity


def test_set_and_get_item():
    vec = vector.Vector()
    vec[0] = 0
    assert vec.size == 1, vec.size
    assert vec[0] == 0, vec[0]
    assert vec.capacity == 2, vec.capacity

    vec = vector.Vector()
    vec[0] = 10
    vec[1] = 20
    assert vec[0] == 10, vec[0]
    assert vec[1] == 20, vec[1]
    vec[-1] = 30
    assert vec[1] == 30, vec[1]


def test_insertion():
    vec = vector.Vector()
    vec.insert(2, 0)
    assert vec[0] == 2, vec[0]
    assert len(vec) == 1, len(vec)
    for i in range(4):
        vec.insert(i, i)
    assert len(vec) == 5, len(vec)
    vec.insert(2, 5)
    assert len(vec) == 6, len(vec)
    assert vec[-1] == 2, vec[-1]
    assert vec[-2] == 2, vec[-2]


def test_erase():
    vec = vector.Vector()
    assert len(vec) == 0, len(vec)
    vec.insert(2, 0)
    assert len(vec) == 1, len(vec)
    vec.erase(0)
    assert len(vec) == 0, len(vec)
    vec.insert(2, 0)
    vec.append(3)
    assert vec[0] == 2, vec[0]
    assert vec[1] == 3, vec[0]
    assert len(vec) == 2, len(vec)
    vec.erase(0)
    assert len(vec) == 1, len(vec)
    assert vec[0] == 3, vec[0]
    vec.insert(2, 0)
    assert vec[1] == 3, vec[1]
    assert len(vec) == 2, len(vec)
    vec.erase(1)
    assert len(vec) == 1, len(vec)
    for i in range(10):
        vec.append(i)
    for i in range(len(vec)-1):
        vec.erase(0)
    assert vec[0] == 9, len(vec)
