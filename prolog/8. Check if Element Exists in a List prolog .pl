element_exists(Element, [Element|_]).
element_exists(Element, [_|Tail]) :-
    element_exists(Element, Tail).
/*?- element_exists(3, [1, 2, 3, 4]).

*/