
import java.util.Scanner;
import java.util.Stack;



/*
 * Interpreter za programski jezik BF
 * Preko argumenta args[0] sprejme program in ga izvede
 * Trak je kon�en s �tevilom celic 10000 in se za�ne pri indexu 0 (nazaj ne more iti)
 * V kolikor program zaide v index manj�i od 0 se spro�i napaka le, �e program �eli v tisto celico pisati ali iz nje brati
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
		
		//Na� trak celic, ki ima na za�etku povsod ni�le
		Cells cells = new Cells();
		
		//Inicializiramo sklad, kamor shranimo pozicije za vrnitev na za�etek zanke
		Stack<Integer> positions = new Stack<Integer>();
		
		
		
		//Trenutni index programa - �teje, kje se nahajamo pri programu
		int index = 0;
		
		//Zastavica - true pomeni, da ukaz ignoriramo - to se zgodi v primeru neizpolnjenega pogoja zanke, ki jo presko�imo
		boolean ignore = false;
		
		//�tejemo pojavitve [, da vemo, kateri je ustrezni ], ki postavi zastavico ignore na false
		int ignoreCount = 0;
		
		
		
		
		
		//GLAVNA ZANKA
		while(index<programArray.length) {
			
			//Pridobimo ukaz iz programa
			char command = programArray[index];
			
			//�E SMO S SPREMENLJIVNO SPET NA 0, POTEM VE� NE IGNORIRAMO
			if(ignoreCount == 0) {
				ignore = false;
			}
			
			
			//Za�etek zanke
			if(programArray[index] == '[') {
				
				//Zastavica na true, ignoriramo, pri�tejemo pojavitev [
				if(ignore) {
					ignoreCount++;
				}
				
				//Zastavica na false
				else {
					
					
					//POGLEDAMO VSEBINO CELICE, �E JE 0 POSTAVIMO ignore=true in pri�tejemo pojavitev [
					if(cells.currentCellContent() == 0) {
						ignore = true;
						ignoreCount++;
					}
					
					//Vsebina celice ni ni�, shranimo pozicijo na sklad, saj se bomo tam morali vrniti ob koncu zanke
					else {
						positions.push(index);
					}
					
				}
				
				
			}
			
			//Naleteli smo na konec zanke
			else if (programArray[index] == ']') {
				
				//�e je zastavica na true, zmanj�amo �tevec, saj smo na�li en ]
				if(ignore) {
					ignoreCount--;
				}
				
				//Zastavica je na false - vrnemo se na za�etek zanke
				else {
					index = positions.pop();
					index--;
				}
			}
			
			//Naleteli smo na enostaven ukaz, ga izvedemo, �e je zastavica na false
			else {
				
				if(!ignore) {
					executeCommand(command, cells);
				}
				
			}
			index++;
			
			
			
		}
		
	}
	
	
	
	//Metoda, ki spro�i ustrezno akcijo glede na to, kak ukaz prejme - akcije so definirane v razredu Cells
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
