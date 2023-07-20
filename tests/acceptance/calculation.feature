Feature: Funkcjonalnosc - wykonywanie dzialan matematycznych

  Scenario: Wykonanie dzialania matematycznego
    Given Mam kalkulator
    And Mam pierwszą liczbę <a>
    And Mam drugą liczbę <b>
    When Po wykonaniu działania "calulator calculate_sum"
    Then Wynik działania wynosi <suma>

    Examples:
    | a   | b       | suma  |
    | 2   | 32      | 34    |
    | 45  | 110     | 155   |
    | 67  | 33      | 100   |