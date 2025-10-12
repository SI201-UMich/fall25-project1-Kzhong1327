import pytest

from project1 import calculate_species_averages
from project1 import calculate_flipper_percentage


def test_calculate_species_averages():
    data = [
        {'species': 'Adelie', 'body_mass_g': 3700, 'bill_length_mm': 40.1},
        {'species': 'Adelie', 'body_mass_g': 3900, 'bill_length_mm': 39.9}
    ]
    result = calculate_species_averages(data)
    assert round(result['Adelie']['avg_body_mass_g'], 2) == 3800.0
    assert round(result['Adelie']['avg_bill_length_mm'], 2) == 40.0

    data = [
        {'species': 'Gentoo', 'body_mass_g': 5000, 'bill_length_mm': 47.5},
        {'species': 'Gentoo', 'body_mass_g': 5100, 'bill_length_mm': 47.3}
    ]
    result = calculate_species_averages(data)
    assert 'Gentoo' in result
    assert abs(result['Gentoo']['avg_body_mass_g'] - 5050) < 0.1

    data = [{'species': 'Adelie', 'body_mass_g': None, 'bill_length_mm': 38.7}]
    result = calculate_species_averages(data)
    assert result == {} 

    data = []
    result = calculate_species_averages(data)
    assert result == {}





def test_calculate_flipper_percentage():
    print('--- Testing calculate_flipper_percentage() ---')

    data = [
        {'species': 'Adelie', 'sex': 'Male', 'flipper_length_mm': 210.0},
        {'species': 'Adelie', 'sex': 'Male', 'flipper_length_mm': 190.0},
        {'species': 'Adelie', 'sex': 'Female', 'flipper_length_mm': 205.0},
        {'species': 'Adelie', 'sex': 'Female', 'flipper_length_mm': 195.0}
    ]
    result = calculate_flipper_percentage(data, threshold=200)
    assert round(result[('Adelie', 'Male')]['percentage_above'], 2) == 50.0
    assert round(result[('Adelie', 'Female')]['percentage_above'], 2) == 50.0
    print('General Case 1 passed.')

    data = [
        {'species': 'Gentoo', 'sex': 'Male', 'flipper_length_mm': 220.0},
        {'species': 'Gentoo', 'sex': 'Male', 'flipper_length_mm': 230.0},
        {'species': 'Gentoo', 'sex': 'Male', 'flipper_length_mm': 210.0},
        {'species': 'Gentoo', 'sex': 'Male', 'flipper_length_mm': 190.0}
    ]
    result = calculate_flipper_percentage(data, threshold=200)
    assert round(result[('Gentoo', 'Male')]['percentage_above'], 2) == 75.0
    print('General Case 2 passed.')


    data = [
        {'species': 'Adelie', 'sex': 'Male', 'flipper_length_mm': None},
        {'species': 'Adelie', 'sex': 'Male', 'flipper_length_mm': 205.0}
    ]
    result = calculate_flipper_percentage(data, threshold=200)
    assert ('Adelie', 'Male') in result
    assert result[('Adelie', 'Male')]['percentage_above'] == 100.0
    print('Edge Case 1 passed.')


    data = []
    result = calculate_flipper_percentage(data, threshold=200)
    assert result == {}
    print('Edge Case 2 passed.')

    print('All tests for calculate_flipper_percentage() passed.\n')


if __name__ == '__main__':
    test_calculate_flipper_percentage()
