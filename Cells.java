

import java.util.Scanner;



//Razred, ki vsebuje trak celic in index, ki ka�e na trenutno celico
public class Cells {
	
	
	
	private byte[] cells;
	private int index;
	
	
	
	//INICIALIZIRAMO CELICE
	public Cells() {
		this.cells = new byte[100000];
		this.index = 0;
	}
	
	
	//Pomaknemo se za eno celico naprej
	public void next() {
		this.index++;
	}
	
	
	//Pomaknemo se za eno celico nazaj
	public void previous() {
		this.index--;
	}
	
	
	//Pove�amo vrednost celice za 1
	public void increase() {
		cells[index]++;
	
	}
	
	//Zmanj�amo vrednost celice za ena
	public void decrease() {
		cells[index]--;
	}
	
	
	//Izpi�emo vrednost celice na zaslon
	public void print() {
		try {
			System.out.print((char)cells[index]);
		}
		catch(Exception e) {
			System.out.println("Napaka pri indeksu!");
			System.out.println("Velikost tabele: "+cells.length);
			System.out.println("Trenutni index: "+index);
			System.exit(0);
		}
	}
	
	
	//Preberemo vrednost iz standardnega vhoda in shranimo v celico, na katero trenutno ka�e kazalec - PREBEREMO LE PRVI ZNAK
	public void read(Scanner reader) {
		char input = reader.next().charAt(0);
		cells[index] = (byte)input;
		
	}
	
	
	//Vrnemo vrednost celice, na katero trenutno ka�e kazalec
	public byte currentCellContent() {
		
		try {
			return this.cells[this.index];
		}
		catch(Exception e) {
			System.out.println("Napaka pri indeksu!");
			System.out.println("Velikost tabele: "+cells.length);
			System.out.println("Trenutni index: "+index);
			System.exit(0);
			return 0;
		}
	}
	
//Komentar 

}
