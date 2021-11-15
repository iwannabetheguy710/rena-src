var t, a, b: longint;

begin
	readln(t);
    repeat
    	read(a, b);
        writeln(a + b);
        dec(t);
    until t = 0;
end.