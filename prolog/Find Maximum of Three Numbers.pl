max_of_three(A, B, C, Max) :-
    Max1 is max(A, B),
    Max is max(Max1, C).
/*?- max_of_three(10, 25, 15, Max).

*/