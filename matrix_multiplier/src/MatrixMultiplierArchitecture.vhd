library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;       
use ieee.numeric_std.all;               
use ieee.math_real.all;                 
library work;
use work.all;
use work.Common.all;

	--This is the overall architecture of the multiplier including input/output registers,

entity MatrixMultiplierArchitecture is
	generic (
			matrixAColNumber : positive := 2;
			matrixBColNumber : positive := 2;
			matrixARowNumber : positive := 2;
			matrixBRowNumber : positive := 2 
		);
	port (
		clock	: in std_ulogic;
		reset   : in std_ulogic;
		matrixA : in BitMatrix(0 to matrixARowNumber-1,0 to matrixAColNumber-1)(3 downto 0);
		matrixB : in BitMatrix(0 to matrixBRowNumber-1,0 to matrixBColNumber-1)(3 downto 0);
		matrixP : out BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(8 downto 0 )
		--matrixP : out BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(integer((ceil(log2(real(((real(64) * real(matrixAColNumber)) + real(1) )))))) downto 0 )
	);
end MatrixMultiplierArchitecture;

architecture rtl of MatrixMultiplierArchitecture is
	-- defined output sizing as a constant to ease readability.
	constant outBits : positive := 8;
	--constant outBits : positive := integer((ceil(log2(real(((real(64) * real(matrixAColNumber)) + real(1) ))))));
	
	component MatrixRegister
		generic (
				matrixRowNumber : positive;
				matrixColNumber : positive;
				cellBits		: positive
		);
		port (
			clock : in std_ulogic;
			reset : in std_ulogic;
			d	  : in BitMatrix(0 to matrixRowNumber-1,0 to matrixColNumber-1)(cellBits downto 0);
			q     : out BitMatrix(0 to matrixRowNumber-1,0 to matrixColNumber-1)(cellBits downto 0)
		);	
	end component MatrixRegister;

	component MatrixMultiplier
		generic (
			matrixAColNumber : positive;
			matrixBColNumber : positive;
			matrixARowNumber : positive;
			matrixBRowNumber : positive
		);
		port (
			matrixA : in BitMatrix(0 to matrixARowNumber-1,0 to matrixAColNumber-1)(3 downto 0);
			matrixB : in BitMatrix(0 to matrixBRowNumber-1,0 to matrixBColNumber-1)(3 downto 0);
			matrixP : out BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(outBits downto 0 )
		);
	end component MatrixMultiplier;

	signal regAOut : BitMatrix(0 to matrixARowNumber-1,0 to matrixAColNumber-1)(3 downto 0);
	signal regBOut : BitMatrix(0 to matrixBRowNumber-1,0 to matrixBColNumber-1)(3 downto 0);
	signal multOut : BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(outBits downto 0 );
	
begin
matrixAReg : MatrixRegister 	generic map (
									matrixColNumber => matrixAColNumber, 
									matrixRowNumber => matrixARowNumber, 
									cellBits => 3
								) 
						      	port map (
						      		d => matrixA,
						      		clock => clock,
						      		reset => reset,
						      		q => regAOut
						      	);
						      	
matrixBReg : MatrixRegister 	generic map (
									matrixColNumber => matrixBColNumber,
									matrixRowNumber => matrixBRowNumber,
									cellBits => 3
								) 
							  	port map (
							  		d => matrixB,
							  		clock => clock, 
							  		reset => reset,
							  		q => regBOut
							  	);
							  	
multiplier	: MatrixMultiplier generic map(
									matrixAColNumber => matrixAColNumber,
									matrixARowNumber => matrixARowNumber,
									matrixBColNumber => matrixBColNumber,
									matrixBRowNumber=>matrixBRowNumber
								) 
							    port map(
							    	matrixA => regAOut,
							    	matrixB =>regBOut,
							    	matrixP=>multOut
							    );
							    
matrixPReg : MatrixRegister 	generic map (
									matrixColNumber => matrixBColNumber, 
									matrixRowNumber => matrixARowNumber, 
									cellBits => outBits
								) 
							  	port map(
							  		d =>multOut,
							  		q=>matrixP,
							  		clock => clock,
							  		reset => reset
							  	);
end rtl;

