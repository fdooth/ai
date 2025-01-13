pattern2(0).
pattern2(N) :-
    N > 0,
    print_row(N),
    nl,
    N1 is N - 1,
    pattern2(N1).

print_row(0).
print_row(Count) :-
    Count > 0,
    write('*'),
    Count1 is Count - 1,
    print_row(Count1).
/*?- pattern2(5).

*/