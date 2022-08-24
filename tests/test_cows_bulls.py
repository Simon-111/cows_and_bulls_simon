
from ..src.cows_bulls_funcs import *

# tests for validate_setup_input function


def test_setup_over_range():
    assert validate_setup_input('11') is False


def test_setup_negative_input():
    assert validate_setup_input('-1') is False


def test_setup_alpha_input():
    assert validate_setup_input('asdf') is False


def test_setup_float_input():
    assert validate_setup_input('4.0') is False


def test_setup_empty_in():
    assert validate_setup_input('') is False


def test_setup_int_in_range():
    assert validate_setup_input('5') is True


def test_setup_spaces_for_input():
    assert validate_setup_input(' ') is False


# tests for gen_code function


def test_gen_code():
    for num in range(2, 10):
        code = gen_code(num)
        assert len(code) == num
        assert code.isdigit
        assert len(code) == len(set(code))


# tests for validate_guess_input function


def test_alpha_for_input():
    assert validate_guess_input('wasd', 4) is False


def test_string_num_with_decimal_input():
    assert validate_guess_input('21.5', 4) is False


def test_repeated_digits():
    assert validate_guess_input('1231', 4) is False


def test_empty_string():
    assert validate_guess_input('', 0) is False


def test_spaces():
    assert validate_guess_input('  ', 2) is False


def test_guess_to_short():
    assert validate_guess_input('12345', 6) is False


def test_guess_to_long():
    assert validate_guess_input('123456789', 8) is False


def test_valid_input_four_long():
    assert validate_guess_input('5678', 4) is True


def test_valid_input_six_long():
    assert validate_guess_input('123456', 6) is True


# testing for count_cows function


def test_zero_cows():
    assert count_cows('1234', '5678') == 0


def test_zero_cows_one_bull():
    assert count_cows('1234', '1567') == 0


def test_four_cows():
    assert count_cows('0987', '7890') == 4


def test_one_cow_no_bulls():
    assert count_cows('3456', '0983') == 1


def test_two_cows_two_bulls():
    assert count_cows('0123', '0132') == 2


# testing for count_bulls function


def test_no_bulls():
    assert count_bulls('1234', '5678') == 0


def test_one_bull_one_cow():
    assert count_bulls('0987', '0754') == 1


def test_two_bulls_two_cows():
    assert count_bulls('1276', '6271') == 2


def test_four_bulls():
    assert count_bulls('5978', '5978') == 4
