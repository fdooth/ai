reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).
/*?- reverse_list([1, 2, 3, 4], Reversed).

*/