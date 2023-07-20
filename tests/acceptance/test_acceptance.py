from pytest_bdd import scenario, given, parsers, when, then

from src import calulator

@scenario(r"C:\Users\ASUS\PycharmProjects\Kalkulator\tests\acceptance\calculation.feature", "Wykonanie dzialania matematycznego")
def test_summing_numbers(capsys):
    pass

@given("Mam kalkulator", target_fixture="calculation")
def calculation():
    return calulator

@given(parsers.parse("Mam pierwszą liczbę <a>"))
def have_first_number(calculation, a):
    return a

@given(parsers.parse("Mam drugą liczbę <b>"))
def have_first_number(calculation, b):
    return b

@when(parsers.parse("Wynik działania wynosi \"{command}\""))
def runcommand(calculation, command):
    calculation.run(command)

@then(parsers.parse("Wynik działania wynosi <suma>"))
def outputcontains(suma, capsys):
    expected_list =
    out, _ = capsys.readouterr()
    assert out == expected_list


