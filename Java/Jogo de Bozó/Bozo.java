public class Bozo{ 

    private static RolaDados;
    private static Placar;

    public static String leuString(){
            try{
                return EntradaTeclado.leString();
            }catch(Exception e){
                System.out.println("Erro ao ler o teclado!");
            }
        return null;
    }

    public static int leuInt(){

        double k = 0; 
        boolean leu = false;
        
        while(!leu){
            leu = true;            
            try{
                k = EntradaTeclado.leInt();
            } catch(Exception e){
                System.out.println("O valor digitado deve ser um número inteiro!");
                leu = false;
            }
        }
        return (int)k;
    } 

    public static void main(java.lang.String[] args) throws java.io.IOException{
        RolaDados dice = new RolaDados(5); // cria 5 dados
        Placar score = new Placar(); // cria um novo placar
        
        // formação das 10 rodadas
        for(int i = 0; i < 10; i++){
            System.out.println("Pressione ENTER para iniciar a rodada:");
            
            String enter = leuString();

            // aguarda o usuário pressionar ENTER para que a rodada comece
            if(enter == ""){
                int[] rollingDices = new int[5];
                rollingDices = bozo.dados.rolar();

                System.out.println(bozo.dados)

                for(int j = 0; j < 2; j++){
                    System.out.println("Escolha os dados a serem rolados!");

                    String out = leuString();
                    rollingDices = bozo.dados.rolar(out);
                }

                System.out.println(bozo.placar)
                System.out.println("Escolha a posição que deseja ocupar!");

                int pos = Bozo.leuInt();

                bozo.placar.add(pos, rollingDices);
                Systen.out.println(bozo.placar);
            }
        }
        
        System.out.println("Total de pontos obtidos: " + bozo.placar.getScore());
    }
}
