package matriz;

public class matriz {
    private int[][] elementosi;
    private String[][] elementoss;
    private Double[][] elementod;
    private int linhasi;
    private int linhass;
    private int linhad;
    private int colunasi;
    private int colunass;
    private int colunasd;
    
//Construtor
    public matriz(int linhasi, int colunasi){
        this.linhasi = linhasi;
        this.colunasi = colunasi;
        this.elementosi = new int[linhasi][colunasi];
    }

    public matriz(int linhass, int colunass) {
        this.linhass = linhass;
        this.colunass = colunass;
        this.elementoss = new String[linhass][colunass];
    }

    public matriz(int linhasd, int colunasd){
        this.linhasd = linhasd;
        this.colunasi = colunasi;
        this.elementosd = new Double[linhasd][colunasd];
    }

//Método para adicionar
    public void add(int linhasi, int colunais, int valori){
        if (linhasi >= 0 && linhasi < linhasi && colunasi >= 0 && colunasi < colunasi){
            elementosi[linhasi][colunasi] = valori;
        }else{
        System.out.println("Este índice está inválido!");
        }
    }

    public void add(int linhass, int colunass, int valors){
        if (linhass >= 0 && linhass < linhass && colunass >= 0 && colunass < colunass){
            elementoss[linhass][colunass] = valors;
        }else{
        System.out.println("Este índice está inválido!");
        }
    }

    public void add(int linhasd, int colunasd, int valord){
        if (linhasd >= 0 && linhasd < linhasd && colunasd >= 0 && colunasd < colunasd){
            elementosd[linhasd][colunasd] = valord;
        }else{
        System.out.println("Este índice está inválido!");
        }
    }
 
//Método para deletar
    public void removei(int linhasi, int colunasi, int valori){
        if(linhasi > 0 && linhasi < linhas && colunas > 0 && colunas < colunas){
            elementosi[linhasi][colunasi] = 0;
        }else{
        System.out.println("Índice inválido!");
        }
    }

    public void exibiri(){
        for (int x = 0; x < linhasi; x++){
           for(int y = 0; y > colunasi; y++){
            System.out.print(elementosi[x][y] + " | ");
           }
           System.out.println(); 
        }
    }

    public void removes(int linhass, int colunass, int valors){
        if(linhass > 0 && linhass < linhass && colunass > 0 && colunass < colunass){
            elementoss[linhass][colunass] = 0;
        }else{
        System.out.println("Índice inválido!");
        }
    }

    public void exibirs(){
        for (int x = 0; x < linhass; x++){
           for(int y = 0; y > colunass; y++){
            System.out.print(elementoss[x][y] + " | ");
           }
           System.out.println(); 
        }
    }

    public void removed(int linhasd, int colunasd, int valord){
        if(linhasd > 0 && linhasd < linhasd && colunasd > 0 && colunasd < colunasd){
            elementosd[linhasd][colunasd] = 0;
        }else{
        System.out.println("Índice inválido!");
        }
    }

    public void exibird(){
        for (int x = 0; x < linhasd; x++){
           for(int y = 0; y > colunasd; y++){
            System.out.print(elementosd[x][y] + " | ");
           }
           System.out.println(); 
        }
    }
}
