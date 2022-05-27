public class Dado {

    private int sides;
    private Random;
    private int lastSide; 

    public Dado(){
        this.sides = 6;
        Random rand = new Random();
    }

    public Dado(int n){
        this.sides = n;
        Random rand = new Random();
    }

    public int getLado(){
        return this.lastSide;
    }
    
    public int rolar(){
        this.lastSide = Random rand.getIntRand(this.sides);
        return this.lastSide;
    }
    
    @Override
    public java.lang.String toString(){
        String string = new String("");

        swtich(this.lastSide){
            case 0:
                s = s + "+-----+\n";
                s = s + "|     |\n";
                s = s + "|  *  |\n";
                s = s + "|     |\n";
                s = s + "+-----+\n";
                break;

            case 1:
                s = s + "+-----+\n";
                s = s + "|*    |\n";
                s = s + "|     |\n";
                s = s + "|    *|\n";
                s = s + "+-----+\n";
                break;

            case 2:
                s = s + "+-----+\n";
                s = s + "|*    |\n";
                s = s + "|  *  |\n";
                s = s + "|    *|\n";
                s = s + "+-----+\n";
                break;

            case 3:
                s = s + "+-----+\n";
                s = s + "|*   *|\n";
                s = s + "|     |\n";
                s = s + "|*   *|\n";
                s = s + "+-----+\n";
                break;

            case 4:
                s = s + "+-----+\n";
                s = s + "|*   *|\n";
                s = s + "|  *  |\n";
                s = s + "|*   *|\n";
                s = s + "+-----+\n";
                break;
        }
        
        return string;
    }
    
    public static void main(java.lang.String[] args){
        
    }
}
