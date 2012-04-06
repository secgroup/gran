reset
set autoscale
set tics out nomirror
set grid
set xlabel "number of roles"
set ylabel "time (s)"
se noborder
set terminal postscript color enhanced
set output '| ps2pdf - benchmark.pdf
plot "gran.dat" with lines
