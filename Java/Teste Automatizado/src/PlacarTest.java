import static org.junit.Assert.*;

import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class PlacarTest {

	private Placar scoreboard;
	
	@Before
	public void setUp() throws Exception {
		scoreboard = new Placar();
	}

	@After
	public void tearDown() throws Exception {
		scoreboard = null;
	}
	
	@Test
	public void testAdd() {
		for(int i = 0; i < 11; i++){
			try {
				scoreboard.add(i, new int[] {1,2,3,4,5});
			} catch (Exception e) {
				;
			}
		}
		// Verifica o caso em que o score está cheio também
		assertEquals(35, scoreboard.getScore());
	}
	
	@Test
	public void testAddInvalidPos() {
		try {
			scoreboard.add(0, new int[] {1,1,1,1,1});
		} catch(Exception e) {
			;
		}
		try {
			scoreboard.add(-1, new int[] {1,2,3,4,5});
		} catch(Exception e) {
			;
		}
		try {
			scoreboard.add(11, new int[] {1,2,3,4,5});
		} catch(Exception e) {
			;
		}
	}
	
	@Test
	public void testReAdd(){
		try {
			scoreboard.add(1, new int[] {1,2,3,4,5});
		} catch (Exception e) {
			;
		}
		try {
			scoreboard.add(1, new int[] {1,2,3,4,5});
		} catch (Exception e) {
			;
		}
	}
	
	@Test
	public void testAddRepetitions(){
		for(int i = 0; i < 11; i++){
			try {
				scoreboard.add(i, new int[] {1,1,1,1,1});
			} catch (Exception e) {
				;
			}
		}
		assertEquals(90, scoreboard.getScore());
	}
	
	@Test
	public void testAddBreaks(){
		for(int i = 0; i < 11; i++){
			try {
				scoreboard.add(i, new int[] {1,2,1,1,1});
			} catch (Exception e) {
				;
			}
		}
		assertEquals(36, scoreboard.getScore());
	}

	@Test
	public void testGetScoreEmpty() {
		int k = scoreboard.getScore();
		assertEquals(0, k);
	}
	
	@Test
	public void testGetScoreFull() throws IllegalArgumentException, IOException {		
		scoreboard.add(1, new int[] {1, 1, 1, 1, 1} );
		scoreboard.add(2, new int[] {2, 2, 2, 2, 2} );
		scoreboard.add(3, new int[] {3, 3, 3, 3, 3} );
		scoreboard.add(4, new int[] {4, 4, 4, 4, 4} );
		scoreboard.add(5, new int[] {5 ,5, 5, 5, 5} );
		scoreboard.add(6, new int[] {6, 6, 6, 6, 6} );
		scoreboard.add(7, new int[] {2, 2, 2, 3, 3} );
		scoreboard.add(8, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(9, new int[] {1, 2, 2, 2, 2} );
		scoreboard.add(10, new int[] {1, 1, 1, 1, 1} );
		
		int k = scoreboard.getScore();
		assertEquals(210, k);
	}
	
	@Test
	public void testGetScoreFailFullHouse() throws IllegalArgumentException, IOException {
		scoreboard.add(1, new int[] {1, 1, 1, 1, 1} );
		scoreboard.add(2, new int[] {2, 2, 2, 2, 2} );
		scoreboard.add(3, new int[] {3, 3, 3, 3, 3} );
		scoreboard.add(4, new int[] {4, 4, 4, 4, 4} );
		scoreboard.add(5, new int[] {5 ,5, 5, 5, 5} );
		scoreboard.add(6, new int[] {6, 6, 6, 6, 6} );
		scoreboard.add(7, new int[] {3, 3, 1, 2, 2} );
		scoreboard.add(8, new int[] {2, 3, 4, 5, 6} );
		scoreboard.add(9, new int[] {1, 3, 2, 2, 2} );
		scoreboard.add(10, new int[] {1, 2, 1, 1, 1} );
		
		int k = scoreboard.getScore();
		assertEquals(125, k);
	}
	
	@Test
	public void testGetScoreCasosRestantes() throws IllegalArgumentException, IOException {
		scoreboard.add(1, new int[] {1, 1, 1, 1, 1} );
		scoreboard.add(2, new int[] {2, 2, 2, 2, 2} );
		scoreboard.add(3, new int[] {3, 3, 3, 3, 3} );
		scoreboard.add(4, new int[] {4, 4, 4, 4, 4} );
		scoreboard.add(5, new int[] {5 ,5, 5, 5, 5} );
		scoreboard.add(6, new int[] {6, 6, 6, 6, 6} );
		scoreboard.add(7, new int[] {3, 3, 1, 2, 2} );
		scoreboard.add(8, new int[] {2, 3, 5, 5, 6} );
		scoreboard.add(9, new int[] {1, 3, 2, 2, 2} );
		scoreboard.add(10, new int[] {1, 2, 1, 1, 1} );
		
		int k = scoreboard.getScore();
		assertEquals(105, k);
	}
	
	@Test
	public void testGetScoreCasosRestantes2() throws IllegalArgumentException, IOException {
		scoreboard.add(1, new int[] {1, 1, 1, 1, 1} );
		scoreboard.add(1, new int[] {1, 2, 2, 2, 2} );
	}

	@Test
	public void testToString() {
		scoreboard.toString();
	}
	
	@Test
	public void testToStringWithValues(){
		String str = "";
		
		scoreboard.add(1, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(2, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(3, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(4, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(5, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(6, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(7, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(8, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(9, new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(10, new int[] {1, 2, 3, 4, 5} );
		
		str += ("   " + scoreboard.placar[0] + "   |");
		str += ("  " + scoreboard.placar[6] + "   |");
		str += ("  " + scoreboard.placar[3] + "   |");
		
		str += '\n';
		str += ("------------------------\n");
		
		str += ("   " + scoreboard.placar[1] + "   |");
		str += ("  " + scoreboard.placar[7] + "   |");
		str += ("  " + scoreboard.placar[4] + "   |");
		
		str += '\n';
		str += ("------------------------\n");
		
		str += ("  " + scoreboard.placar[2] + "   |");
		str += ("  " + scoreboard.placar[8] + "   |");
		str += ("  " + scoreboard.placar[5] + "   |");
		
		str += '\n';
		str +=("------------------------\n");
		
		str += ("       |"  + "  " + scoreboard.placar[9] + "   " +  "|   ");
		
		str +='\n';
		str +=("       x-------x        \n");
		
		assertEquals(scoreboard.toString(), str);
	}
	
	@Test
	public void toStringNull() throws IllegalArgumentException, IOException {
		String str = "";
		
		str +=("  (1)  |");
		str += ("  (7)  |");
		str += ("  (4)  |");
		
		str += '\n';
		str += ("------------------------\n");
		
		str +=("  (2)  |");
		str +=("  (8)  |");
		str +=("  (5)  |");
		
		str += '\n';
		str += ("------------------------\n");
		
		str += ("  (3)  |");
		str += ("  (9)  |");
		str += ("  (6)  |");
		
		str += '\n';
		str +=("------------------------\n");
		
		str += ("       |  (10) |         ");
		
		str +='\n';
		str +=("       x-------x        \n");
		
		assertEquals(scoreboard.toString(), str);
	}
	
}
