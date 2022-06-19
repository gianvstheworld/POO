import static org.junit.Assert.*;

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
	public void testAddInvalidPos() {
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
	public void testGetScoreFull() {		
		scoreboard.add(1,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(2,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(3,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(4,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(5,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(6,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(7,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(8,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(9,  new int[] {1, 2, 3, 4, 5} );
		scoreboard.add(10, new int[] {1, 2, 3, 4, 5} );
		
		int k = scoreboard.getScore();
		assertEquals(35, k);
	}

	@Test
	public void testToString() {
		scoreboard.toString();
	}
	
	@Test
	public void testToStringWithValues(){
		try {
			scoreboard.add(1, new int[] {1,2,1,1,1});
		} catch (Exception e) {
			;
		}
		scoreboard.toString();
	}
}
