library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;       
use ieee.numeric_std.all;               
use ieee.math_real.all;                 
library work;
use work.Common.all;

	--This module implements the logic core of the matrix multiplier

entity MatrixMultiplier is
	generic (
			matrixAColNumber : positive;
			matrixBColNumber : positive;
			matrixARowNumber : positive;
			matrixBRowNumber : positive
		);
	port (
		matrixA : in BitMatrix(0 to matrixARowNumber-1,0 to matrixAColNumber-1)(3 downto 0);
		matrixB : in BitMatrix(0 to matrixBRowNumber-1,0 to matrixBColNumber-1)(3 downto 0);
		matrixP : out BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(8 downto 0) -- Cell sizing for matrix P elements according to 
																							 -- the formula to avoid finite arithmetics errors
	);
end MatrixMultiplier;

--matrixP : out BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(integer((ceil(log2(real(((real(64)*real(matrixAColNumber)) + real(1) )))))) downto 0 )


architecture beh of MatrixMultiplier is
	function  MatrixMultiplication  ( a : BitMatrix; b:BitMatrix) return BitMatrix is
	
	--the use of variables is due to the fact that there is a for cycle, so it must be updated values immediately, 
	--not after the function/process (delta delay rule for signals and variables, that updates 
	--signals after the end of the function/process).
	variable i,j,k : integer:=0;
	variable product : BitMatrix(0 to matrixARowNumber-1,0 to matrixBColNumber-1)(8 downto 0 ):=(others => (others => (others => '0')));
	begin
		for i in 0 to matrixARowNumber-1 loop
			for j in 0 to matrixBColNumber-1 loop
				for k in 0 to matrixAColNumber-1 loop
		   			product(i,j) := std_ulogic_vector(signed(product(i,j)) + (signed(a(i,k)) * signed(b(k,j))));
				end loop;
			end loop;
		end loop;
		return product;
	end MatrixMultiplication;
begin
	matrixP <= MatrixMultiplication(matrixA,matrixB);
end beh;


