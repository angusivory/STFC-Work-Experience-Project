import unittest

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    # test case len list < 10
    def test_given_a_list_with_less_than_ten_items_when_adding_fish_to_aquarium_then_returns_dict_containing_list(self):
        fish = ["shark", "tuna"]
        expected = {"tank_a": fish}
        actual = add_fish_to_aquarium(fish)
        self.assertEqual(actual, expected)

    # test case len list > 10
    def test_given_a_list_with_more_than_ten_items_when_adding_fish_to_aquarium_then_returns_dict_containing_list(self):
        fish = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish)
        self.assertEqual(str(exception_context.exception), "A maximum of 10 fish can be added to the aquarium")