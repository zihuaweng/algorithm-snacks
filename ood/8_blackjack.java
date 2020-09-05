public enum SUIT {
  HEART, SPADE, CLUB, DIAMOND
}




public class Card {
  private SUIT suit;
  private int faceValue;

 public SUIT getSuit() {
    return suit;
  }

  public int getFaceValue() {
    return faceValue;
  }

  Card(SUIT suit, int faceValue) {
    this.suit = suit;
    this.faceVale = faceValue;
  }
}







public class BlackjackCard extends Card {
  private int gameValue;

  public int getGameValue() {
    return gameValue;
  }

  public BlackjackCard(SUIT suit, int faceValue) {
    super(suit, faceValue);
    this.gameValue = faceValue;
    if(this.gameValue > 10) {
      this.gameValue = 10;
    }
  }
}








public class Deck {
  private List<BlackjackCard> cards;
  private Date creationDate;

  public Deck() {
    this.creationDate = new Date();
    this.cards = new ArrayList<BlackjackCard>();
    for(int value = 1 ; value <= 13 ; value++){
      for(SUIT suit : SUIT.values()){
        this.cards.add(new BlackjackCard(suit, value));
      }
    }
  }

  public List<BlackjackCard> getCards() {
    return cards;
}

public class Shoe {
  private List<BlackjackCard> cards;
  private int numberOfDecks;

  private void createShoe() {
    this.cards = new ArrayList<BlackjackCard>();
    for(int decks = 0 ; decks < numberOfDecks ; decks++){
      cards.add(new Deck().getCards());
    }
  }

  public Shoe(int numberOfDecks) {
    this.numberOfDecks = numberOfDecks;
    createShoe();
    shuffle();
  }

  public void shuffle() {
    int cardCount = cards.size();
    Random r = new Random();
    for (int i = 0; i < cardCount ; i++){
      int index = r.nextInt(cardCount-i-1);
      swap(i, index);
    }
  }

  public void swap(int i, int j) {
    BlackjackCard temp = cards[i];
    cards[i] = cards[j];
    cards[j] = temp;
  }

  //Get the next card from the shoe
  public BlackjackCard dealCard() {
    if(cards.size() == 0 ){
      createShoe();
    }
    return cards.remove(0);
  }
}









public class Hand {
  private ArrayList<BlackjackCard> cards;

  private List<Integer> getScores() {
    List<Integer> totals = new ArrayList();
    total.add(0);

    for (BlackjackCard card : cards) {
      List<Integer> newTotals = new ArrayList();
      for (int score : totals) {
        newTotals.add(card.faceValue() + score);
        if (card.faceValue() == 1) {
          newTotals.add(11 + score);
        }
      }
      totals = newTotals;
    }
    return totals;
  }

  public Hand(BlackjackCard c1, BlackjackCard c2) {
    this.cards = new ArrayList<BlackjackCard>();
    this.cards.add(c1);
    this.cards.add(c2);
  }

  public void addCard(BlackjackCard card) {
    cards.add(card);
  }

  // get highest score which is less than or equal to 21
  public int resolveScore() {
    List<Integer> scores = getScores();
    int bestScore = 0;
    for (int score : scores) {
      if (score <= 21 && score > bestScore) {
        bestScore = score;
      }
    }
    return bestScore;
  }
}










public abstract class BasePlayer {
  private String id;
  private String password;
  private double balance;
  private AccountStatus status;
  private Person person;
  private List<Hand> hands;

  public boolean resetPassword();

  public List<Hand> getHands() {
    return hands;
  }

  public void addHand(Hand hand) {
    return hands.add(hand);
  }

  public void removeHand(Hand hand) {
    hands.remove(hand);
  }
}

public class Player extends BasePlayer {
  private int bet;
  private int totalCash;

  public Player(Hand hand) {
    this.hands = new ArrayList<Hand>();
    this.hands.add(hand);
  }
}








public class Game {
  private Player player;
  private Dealer dealer;
  private Shoe shoe;
  private final int MAX_NUM_OF_DECKS = 3;

  private void playAction(string action, Hand hand) {
    switch(action) {
      case "hit": hit(hand); break;
      case "split": split(hand); break;
      case "stand pat": break; //do nothing
      case "stand": stand(); break;
      default: print("Wrong input");
    }
  }

  private void hit(Hand hand) {
    hand.addCard(shoe.dealCard());
  }

  private void stand() {
    int dealerScore = dealer.getTotalScore();
    int playerScore = player.getTotalScore();
    List<Hand> hands = player.getHands();
    for(Hand hand : hands) {
      int bestScore = hand.resolveScore();
      if(playerScore == 21){
        //blackjack, pay 3:2 of the bet
      } else if (playerScore > dealerScore) {
        // pay player equal to the bet
      } else if (playerScore < dealerScore) {
        // collect the bet from the player
      } else { //tie
        // bet goes back to player
      }
    }
  }

  private void split(Hand hand) {
    Cards cards = hand.getCards();
    player.addHand(new Hand(cards[0], shoe.dealCard()));
    player.addHand(new Hand(cards[1], shoe.dealCard()));
    player.removeHand(hand);
  }


 public Game(Player player, Dealer dealer) {
    this.player = player;
    this.dealer = dealeer;
    Shoe shoe= new Shoe(MAX_NUM_OF_DECKS);
  }

  public void start() {
    player.placeBet(getBetFromUI());

    Hand playerHand = new Hand(shoe.dealCard(), shoe.dealCard());
    player.addToHand(playerHand);

    Hand dealerHand = new Hand(shoe.dealCard(), shoe.dealCard());
    dealer.addToHand(dealerHand);

    while(true){
      List<Hand> hands = player.getHands();
      for(Hand hand : hands) {
        string action = getUserAction(hand);
        playAction(action, hand);
        if(action.equals("stand")) {
          break;
        }
      }
    }
  }

  public static void main(String args[]) {
    Player player = new Player();
    Dealer dealer = new Dealer();
    Game game = new Game(player, dealer);
    game.start();
  }
}









