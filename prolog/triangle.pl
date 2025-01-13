print_stars(0).
print_stars(N) :-
    N > 0,
    print_row(N),
    nl,
    print_stars(N - 1).

print_row(0).
print_row(Count) :-
    Count > 0,
    write('* '),
    Count1 is Count - 1,
    print_row(Count1).
/*?- print_stars(5).

*/