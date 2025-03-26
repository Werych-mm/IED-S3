import vetor.PrimeiroVetor;
import matriz.matriz;

public class App {
    public static void main(String[] args) throws Exception {
       PrimeiroVetor vetor = new PrimeiroVetor(5);
       matriz uva = new matriz(5, 5);
       uva.add(0, 0, 12);
       uva.add(0, 1, 18);
       uva.add(2, 1, 5);

      uva.exibir();
  
      uva.remove(2, 0, 0);
      uva.remove(3, 1, 0);
      uva.remove(5, 2, 1);
      
      uva.exibir();

       vetor.exibir();
       int [] valores = {10,20,30,40};
       for (int valor : valores) {
        vetor.adicionarTodos(valor);
           
       }
      vetor.exibir();
      System.out.println("Índice 2 = " + vetor.getElemento(2));
      System.out.println("Tamanho vetor 1 = " + vetor.getTamanho());
      System.out.println("--------------------------");
      vetor.removerPorIndiceNull(0);
      vetor.adicionarNull(20);
     // System.out.println("Indece 2 = " + vetor.getElemento(2));
      //System.out.println("Tamanho vetor 2 = " + vetor.getTamanho());
      vetor.exibir();
       

    }
}
