library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;      
library work;
use work.Common.all;

	--This module hold a matrix like a D-FLIP FLOP using BitMatrix defined type.

entity MatrixRegister is
	generic (
		matrixRowNumber : positive;
		matrixColNumber : positive;
		cellBits		: positive
	);
	port (
		clock	: in std_ulogic;
		reset	: in std_ulogic;
		d		: in BitMatrix(0 to matrixRowNumber-1,0 to matrixColNumber-1)(cellBits downto 0);
		q		: out BitMatrix(0 to matrixRowNumber-1,0 to matrixColNumber-1)(cellBits downto 0)
	);
end MatrixRegister;

architecture beh of MatrixRegister is
begin	
	comb_p: process(clock) --using synchronous reset (active low reset)
		begin
			if(rising_edge(clock)) then
				if(reset = '0') then
					q<=(others => (others => (others => '0')));
				else
					q <= d;
				end if;
			end if;
	end process comb_p;
end beh;

