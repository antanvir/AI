import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;


public class TwoPlayerGame {

	private Board board;
	private boolean isFirstPlayersTurn = true;
	private boolean gameFinished = false;
	private int minimaxDepth = 3;
	private boolean aiStarts = true; // AI makes the first move
	private Minimax ai;
//	public static final String cacheFile = "score_cache.ser";
	private int winner; // 0: There is no winner yet, 1: Second Player Wins, 2: First Player Wins
	
	
	public TwoPlayerGame(Board board) {
		this.board = board;
		ai = new Minimax(board);
		
		winner = 0;
	}
	/*
	 * 	Loads the cache and starts the game, enabling human player interactions.
	 */
	public void start() {
		
		
		// Make the board start listening for mouse clicks.
		board.startListening(new MouseListener() {

			public void mouseClicked(MouseEvent arg0) {

				Thread mouseClickThread = new Thread(new MouseClickHandler(arg0));
				mouseClickThread.start();
				System.out.println("First Player Turn: " + isFirstPlayersTurn);
			}

			public void mouseEntered(MouseEvent arg0) {
				// TODO Auto-generated method stub
				
			}

			public void mouseExited(MouseEvent arg0) {
				// TODO Auto-generated method stub
				
			}

			public void mousePressed(MouseEvent arg0) {
				// TODO Auto-generated method stub
				
			}

			public void mouseReleased(MouseEvent arg0) {
				// TODO Auto-generated method stub
				
			}
			
		});
	}
	/*
	 * 	Sets the depth of the minimax tree. (i.e. how many moves ahead should the AI calculate.)
	 */
	public void setAIDepth(int depth) {
		this.minimaxDepth = depth;
		
	}
	
	
	public void setAIStarts(boolean aiStarts) {
		this.aiStarts = aiStarts;
	}
	
	
	public class MouseClickHandler implements Runnable{
		MouseEvent e;
		public MouseClickHandler(MouseEvent e) {
			this.e = e;
		}
		
		public void run() {
			if(gameFinished) return;
			
			// Find out which cell of the board do the clicked coordinates belong to.
			if(isFirstPlayersTurn) {
				System.out.println("Here BLACK STONE");
				int posX = board.getRelativePos( e.getX() );
				int posY = board.getRelativePos( e.getY() );
				
				// Place a black stone to that cell.
				if(!playMove(posX, posY, true)) {
					// If the cell is already populated, do nothing.
//					isFirstPlayersTurn = false;
					setPlayersTurn(!isFirstPlayersTurn);
					return;
				}
				
				// Check if the last move ends the game.
				winner = checkWinner();
				
				if(winner == 2) {
					System.out.println("1st PLAYER WON!");
					board.printWinner(winner, "1st PLAYER WON!");
					gameFinished = true;
					return;
				}
			}
			else {
				System.out.println("Here WHITE STONE");
				int posX = board.getRelativePos( e.getX() );
				int posY = board.getRelativePos( e.getY() );
				
				// Place a white stone to that cell.
				if(!playMove(posX, posY, false)) {
					// If the cell is already populated, do nothing.
//					isFirstPlayersTurn = true;
					setPlayersTurn(!isFirstPlayersTurn);
					return;
				}
				
				// Check if the last move ends the game.
				winner = checkWinner();
				
				if(winner == 1) {
					System.out.println("2nd Player WON!");
					board.printWinner(winner, "2nd PLAYER WON!");
					gameFinished = true;
					return;
				}
			}
			
			if(board.generateMoves().size() == 0) {
				System.out.println("No possible moves left. Game Over.");
				board.printWinner(0, "MATCH TIED!"); // Prints "TIED!"
				gameFinished = true;
				return;
				
			}
			setPlayersTurn(!isFirstPlayersTurn);
			
			
		}
		
	}
	
	private void setPlayersTurn(boolean PlayersTurn) {
		this.isFirstPlayersTurn = PlayersTurn;
		System.out.println("Let's see! " + isFirstPlayersTurn);
	}
	
	private int checkWinner() {
		if(Minimax.getScore(board, true, false) >= Minimax.getWinScore()) return 2; // Black stone, Human Player
		if(Minimax.getScore(board, false, true) >= Minimax.getWinScore()) return 1;
		return 0;
	}
	
	
	private boolean playMove(int posX, int posY, boolean black) {
		return board.addStone(posX, posY, black);
	}
	
}
