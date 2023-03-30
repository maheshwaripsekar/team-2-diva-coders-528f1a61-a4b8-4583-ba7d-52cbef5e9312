*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Valid Case #1                   3             3             2                     UP        3           4           3
Valid Case #2                   10            10            5                     UP       10           10          6
Valid Case #3                   5             10            2                     Down      5           9           3
Valid Case #4                   6              7            3                     Down      6           6           4
Valid Case #5                   7              8            4                     Right     8           8           5
Valid Case #6                   3              7            6                     Left      2           7           7
Valid Case #7                   1              1            1                     Right     2           1           2
Valid Case #8                   6              6            5                      Left     5           6           6
Valid Case #9                   2              3            4                      UP       2           4           5
Valid Case #10                  1              10           137                     UP      1           10          138
Valid Case #11                  10              1           4                       Right   10          1           5
Valid Case #12                  6               5           5                       Down    6           4           6
Valid Case #13                  7               3           6                       Down    7           2           7
Valid Case #14                  1               2           7                       UP      1           3           8
Valid Case #15                  7               4           3                       UP      8           4           4
Valid Case #16                  4               5           7                       Down    4           4           8
*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
