create_clock -period 1000.000 -name CLK2 -waveform {0.000 500.000} -add [get_ports -filter { NAME =~  "*clock*" && DIRECTION == "IN" }]

