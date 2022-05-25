create_clock -period 8.000 -name PL_clock -waveform {0.000 4.000} -add [get_ports -filter { NAME =~  "*clock*" && DIRECTION == "IN" }]
