library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;        
use ieee.numeric_std.all;               

	--This package contains the type definition for the core matrix type used by all modules in the project.

	--since VHDL-2008, one of the main changes to composite types 
	--(array and record types) is that now you can declare unconstrained array
	--and record elements (The sizes of unconstrained fields of a record can be 
	--determined when a constant, signal… of the record type is used).
 
	--Unconstrained std_ulogic_vector/std_logic_vector is available
	--(the user has to set the options to work with VHDL 2008).
	
	--it was choose to use the UNRESOLVED TYPE for the array, so it was used std_ulogic.

package Common is
	type BitMatrix is array(natural range<>,natural range<>) of std_ulogic_vector;
end Common;

package body Common is
end Common;
