import java.util.Map;
import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ContaPalavra {

	public static String ContaPalavra() throws FileNotFoundException, IOException {
        try (BufferedReader br = new BufferedReader(new FileReader("/home/gian/Documentos/file.txt"))) {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();     

            while (line != null) {
                sb.append(line);
                sb.append(System.lineSeparator());
                line = br.readLine();
            }
            
            return sb.toString();
        }     
	}
	
    public static void criaMapa(String line_words){
    	String str = line_words;
        Map<String, Integer> word_map = new HashMap<String, Integer>(); // Mapa de String para Integer
        
        String[] words = str.split(" "); 
        
        // Itera as palavras que estão espaçadas
        for(String word : words){
            if(word_map.containsKey(word))
                word_map.put(word, word_map.get(word) + 1); // Palavra já está no mapa, mas ocorre mais de uma vez
            else
                word_map.put(word, 1); // Caso a palavra ainda não esteja no mapa, adiciona ela
        }
        mostraMapa(word_map);
	}
    
    public static void mostraMapa(Map <String, Integer> map){
        for(Object key : map.keySet())
        	System.out.println("Palavra: " + key + "\tContador: " + map.get(key));
    }
        
	public static void main(String[] args) throws IOException{
		String current_line = ContaPalavra();
		
		criaMapa(current_line);
	}
}
