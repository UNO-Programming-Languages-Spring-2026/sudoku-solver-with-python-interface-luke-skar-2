% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
row(1..9).
col(1..9).
num(1..9).
g(1..9).

1 {sudoku(X, Y, N) : num(N) } 1 :- row(X), col(Y).

:- initial(X, Y, N0), sudoku(X, Y, N), N != N0.

:- row(X), num(N), col(Y1), col(Y2), Y1 < Y2, sudoku(X, Y1, N), sudoku(X, Y2, N).

:- col(Y), num(N), row(X1), row(X2), X1 < X2, sudoku(X1, Y, N), sudoku(X2, Y, N).

rowblock(X,1) :- row(X), X <= 3.
rowblock(X,2) :- row(X), X >= 4, X <= 6.
rowblock(X,3) :- row(X), X >= 7.

colblock(Y,1) :- col(Y), Y <= 3.
colblock(Y,2) :- col(Y), Y >= 4, Y <= 6.
colblock(Y,3) :- col(Y), Y >= 7.

subgrid(X, Y, G) :- row(X), col(Y), rowblock(X, RB), colblock(Y, CB), G = (RB - 1) * 3 + CB. 

:- g(G), num(N), subgrid(X1, Y1, G), subgrid(X2, Y2, G), (X1, Y1) < (X2, Y2), sudoku(X1, Y1, N), sudoku(X2, Y2, N).


#show sudoku/3.
