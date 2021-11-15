program main;

var t, a, b: integer;

begin
	readln(t);
    repeat
    	read(a, b);
        writeln(a + b);
    	dec(t);
    until t;
end.