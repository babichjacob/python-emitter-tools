"Test emitter tools"


from emitter import emittable
from emitter_tools import categorize


def test_categorize():
    "Test that categorize can be used to separate different types of events from the same emitter"

    input_events = [
        ("b", 12),
        ("a", 7),
        ("c", 83),
        ("a", 49),
        ("b", 9),
        ("a", 70),
        ("a", 1),
        ("c", 35),
    ]

    expected_a = [
        ("a", 7),
        ("a", 49),
        ("a", 70),
        ("a", 1),
    ]
    expected_b = [
        ("b", 12),
        ("b", 9),
    ]
    expected_c = [
        ("c", 83),
        ("c", 35),
    ]

    actual_a = []
    actual_b = []
    actual_c = []

    abc_emitter = emittable()

    categorized_emitters = categorize(
        abc_emitter, lambda event: event[0], ["a", "b", "c"]
    )

    a_emitter = categorized_emitters["a"]
    b_emitter = categorized_emitters["b"]
    c_emitter = categorized_emitters["c"]

    unlisten_a = a_emitter.listen(actual_a.append)
    unlisten_b = b_emitter.listen(actual_b.append)
    unlisten_c = c_emitter.listen(actual_c.append)

    for event in input_events:
        abc_emitter.emit(event)

    assert actual_a == expected_a
    assert actual_b == expected_b
    assert actual_c == expected_c

    unlisten_a()
    unlisten_b()
    unlisten_c()
