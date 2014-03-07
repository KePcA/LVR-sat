
import java.util.Scanner;
import java.util.Stack;



/*
 * Interpreter za programski jezik BF
 * Preko argumenta args[0] sprejme program in ga izvede
 * Trak je konèen s številom celic 10000 in se zaène pri indexu 0 (nazaj ne more iti)
 * V kolikor program zaide v index manjši od 0 se sproži napaka le, èe program želi v tisto celico pisati ali iz nje brati
 * Interpreter ignorira vse ostale znake, ki niso del programskega jezika BF
 * razrec Cells.java predstavlja trak, ki ga potrebuje program za izvajanje
 */


public class BrainFuckInterpreter {
	
	
	static Scanner scan;
	
	
	public static void main(String args[]) {
		
		
		
		
		String program = "";
		
		try {
			program = args[0];
		}
		catch(Exception e) {
			System.out.print("Ni podanega argumenta!");
			System.exit(0);
		}
		
		
		
		
		char[] programArray = program.toCharArray();
		
		//Naš trak celic, ki ima na zaèetku povsod nièle
		Cells cells = new Cells();
		
		//Inicializiramo sklad, kamor shranimo pozicije za vrnitev na zaèetek zanke
		Stack<Integer> positions = new Stack<Integer>();
		
		
		
		//Trenutni index programa - šteje, kje se nahajamo pri programu
		int index = 0;
		
		//Zastavica - true pomeni, da ukaz ignoriramo - to se zgodi v primeru neizpolnjenega pogoja zanke, ki jo preskoèimo
		boolean ignore = false;
		
		//Štejemo pojavitve [, da vemo, kateri je ustrezni ], ki postavi zastavico ignore na false
		int ignoreCount = 0;
		
		
		
		
		
		//GLAVNA ZANKA
		while(index<programArray.length) {
			
			//Pridobimo ukaz iz programa
			char command = programArray[index];
			
			//ÈE SMO S SPREMENLJIVNO SPET NA 0, POTEM VEÈ NE IGNORIRAMO
			if(ignoreCount == 0) {
				ignore = false;
			}
			
			
			//Zaèetek zanke
			if(programArray[index] == '[') {
				
				//Zastavica na true, ignoriramo, prištejemo pojavitev [
				if(ignore) {
					ignoreCount++;
				}
				
				//Zastavica na false
				else {
					
					
					//POGLEDAMO VSEBINO CELICE, ÈE JE 0 POSTAVIMO ignore=true in prištejemo pojavitev [
					if(cells.currentCellContent() == 0) {
						ignore = true;
						ignoreCount++;
					}
					
					//Vsebina celice ni niè, shranimo pozicijo na sklad, saj se bomo tam morali vrniti ob koncu zanke
					else {
						positions.push(index);
					}
					
				}
				
				
			}
			
			//Naleteli smo na konec zanke
			else if (programArray[index] == ']') {
				
				//Èe je zastavica na true, zmanjšamo števec, saj smo našli en ]
				if(ignore) {
					ignoreCount--;
				}
				
				//Zastavica je na false - vrnemo se na zaèetek zanke
				else {
					index = positions.pop();
					index--;
				}
			}
			
			//Naleteli smo na enostaven ukaz, ga izvedemo, èe je zastavica na false
			else {
				
				if(!ignore) {
					executeCommand(command, cells);
				}
				
			}
			index++;
			
			
			
		}
		
	}
	
	
	
	//Metoda, ki sproži ustrezno akcijo glede na to, kak ukaz prejme - akcije so definirane v razredu Cells
	public static void executeCommand(char command, Cells cells) {
		
		if(command == '<') { cells.previous(); }
		else if (command == '>') { cells.next(); }
		else if (command == '+') { cells.increase(); }
		else if (command == '-') { cells.decrease(); }
		else if (command == '.') { cells.print(); }
		else if (command == ',') { scan = new Scanner(System.in); cells.read(scan); }
		else {
			//IGNORIRAMO OSTALE ZNAKE
		}
		
	}
	
	
	
	
	
	
	

}
