print_natural(0).
print_natural(N) :-
    N > 0,
    print_natural(N - 1),
    writeln(N).
/*?- print_natural(5).

*/