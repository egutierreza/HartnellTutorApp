----------------------------------------------------------------------------------
-- Engineer: Bridget Benson
-- Create Date: 09/21/2015 09:02:18 AM
-- Description: Template file for test benches
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity simulation is
end simulation;

architecture Behavioral of simulation is

    component bcdComparator is
        Port ( 
           num1, num2: in std_logic_vector(3 downto 0);
           anComp: out std_logic_vector(3 downto 0);
           catComp: out std_logic_vector(7 downto 0);
           offButton: in std_logic
          );
    end component bcdComparator;

    signal num1 : std_logic_vector(3 downto 0) := "0000";
    signal num2 : std_logic_vector(3 downto 0) := "0000";    
    signal anComp : std_logic_vector(3 downto 0);
    signal catComp : std_logic_vector(7 downto 0) := "00000000";
    signal offButton : std_logic := '1';
	
    begin
    
        uut: bcdComparator PORT MAP (
            num1 => num1,
            num2 => num2,
            anComp => anComp,
            catComp => catComp,
            offButton => offButton
        );
				
        stim_proc: process
        begin
            num1 <= "0110";
            num2 <= "1001";
            
            wait for 10ns;
        end process;
end Behavioral;