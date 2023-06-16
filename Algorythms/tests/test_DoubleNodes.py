from Algorythms.python_solutions.DoubleNodes import Stack, Queue, Deck, DoubleNode, prev

def test_doublenode():
    dn_0 = DoubleNode(3)
    dn_2 = DoubleNode(4)
    dn_1 = DoubleNode(5, dn_0, dn_2)
    assert prev(dn_1) == dn_0, (prev(dn_1), dn_0)
    assert next(dn_1) == dn_2, (next(dn_1), dn_2)
    assert str(dn_0) == '3', str(dn_0)
    dn_0 = DoubleNode(prev_node = dn_1, next_node = dn_2)
    assert str(dn_0) == 'None', str(dn_0)
   
def test_stack():
    st = Stack()
    st.push(None)
    assert st.size == 1, st.size
    st.push(4)
    st.push([None, 'None', 4, []])
    st.push('None')
    assert st.back() == 'None', st.back()
    assert st.front() is None, st.front()
    assert st.pop() == 'None', st.back()
    assert type(st.back()) == list, type(st.back())
    assert st.front() is None, st.front()
    assert len(st.back()) == 4, len(st.back())
    while len(st) != 1:
        st.pop()
    assert st.front() == st.back(), (st.front(), st.back())
    assert st.front() is None, st.front()
    st.pop()
    assert len(st) == 0, len(st)

def test_queue():
    q = Queue()
    # check only pop, push, back and front
    # because other methods are defined 
    # and checked in Stack
    q.push(None)
    assert q.size == 1, q.size
    assert q.front() is None, q.front()
    q.push(4)
    q.push([None, 'None', 4, []])
    q.push('None')
    assert q.front() is None, q.front()
    assert q.back() == 'None', q.back()
    assert q.pop() is None, q.pop()
    assert q.front() == 4, q.back()
    while len(q) != 1:
        q.pop()
    assert q.front() == q.back(), (q.front(), q.back())
    assert q.front() == 'None', q.front()

def test_deck():
    d = Deck()
    d.push_front(None)
    assert d.size == 1, q.size
    assert d.front() is None, q.front()
    d.push_back(4)
    d.push_front([None, 'None', 4, []])
    d.push_back('None')
    assert type(d.front()) == list, d.front()
    assert d.back() == 'None', d.back()
    d.pop_front()
    assert d.front() is None, d.front()
    d.pop_back()
    assert d.back() == 4, d.back()


    
