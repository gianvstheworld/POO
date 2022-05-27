public class RolaDados {    

    private int nDices; // número de dados
    private int[] rollingStats; // vetor que armazena o status de rolagem dos dados
    private Dado[] dicesList; // vetor que armazena os n dados criados

    // construtor de RolaDados que cria n dados
    public RolaDados(int n){
        this.nDices = n
        this.rollingStats = new int[n];
        this.dicesList = new Dado[n];

        int i = 0;

        while(i < this.nDices){
            Thread.sleep(100); // pausa o código por um intervalo de 1ms para gerar nova seed

            dicesList[i] = new Dado(6); // cria novo dado
            rollingStats[i] = 0;
        }

        i++;
    }
    
    // função responsável por rolar os dados
    public int[] rolar(){
        for(int i = 0; i < nDices; i++)
            this.rollingStats[i] = dicesList[i].rolar(); // rola todos os dados da classe

        return this.rollingStats; // retorna o vetor com os dados rolados
    }
    
    // função responsável por rolar dados específicos
    public int[] rolar(boolean[] quais){
        for(int i = 0; i < nDices; i++){
            if(quais[i]) // caso seja necessário rolar a i-ésima posição, rola o dado de novo
                this.rollingStats[i] = dicesList[i].rolar();
            else // caso contrário, pega o valor presente no dados
                this.rollingStats[i] = dicesList[i].getLado();
        }

        return this.rollingStats;
    }
    
    public int[] rolar(java.lang.String s){
        String rollingDices[] = s.replaceAll("[ " + this.nDices + " ]")

        if(rollingDices[0] != NULL){
            for(int i = 0; i < rollingDices.length; i++){
                int dice = Integer.parseInt(rollingDices[i]);
                
                this.rollingStats[dice] = dicesList[dice].rolar();
            }
        }

        return this.rollingStats
    }
    
    @Override
    // representação dos daddos por meio de uma string
    public java.lang.String toString(){
        String s = new String();

        // concatena em uma string a string de todos os dados
        for(int i = 0; i < dicesList.length; i++){
            s += dicesList[i].toString();
        }

        String split[] = s.split("\n"); // separa a string a partir dos \n
        s = ""; // string nula

        for(int i = 1; i < 6; i++){ 
            s += " " + i;

            for(int j = 0; j < 9; j++)
                s += " ";
        }

        s += "\n";
        
        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++) 
                s += split[i + 5*j] + "    ";

            s += "\n";
        }

        return (s + "\n");
    }
}
