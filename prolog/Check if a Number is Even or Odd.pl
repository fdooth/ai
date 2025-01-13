even_or_odd(Number, Result) :-
    (Number mod 2 =:= 0 -> Result = even ; Result = odd).
/*?- even_or_odd(4, Result)*/