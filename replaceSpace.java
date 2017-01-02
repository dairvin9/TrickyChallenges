public class ReplaceSpace
{

  public static char[] replaceSpaces(char[] original){
  	int size = original.length;
    int numSpaces = 0;
    for (int i = 0; i < size; i++){
      if (original[i] == ' '){
      	numSpaces++;
      }
    }
    char[] newArray = new char[size + numSpaces*2];
    
    int index = newArray.length - 1;
    for (int i = size - 1; i > -1; i-- ){
      if (original[i] ==  ' '){
      	newArray[index] = '0';
        index--;
        newArray[index] = '2';
        index--;
        newArray[index] = '%';
        index--;
      }
      else {
        newArray[index] = original[i];
        
        index--;
      }
    }
    
    return newArray;
    
  }
  
  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
    char[] str = {'w','e',' ','a','r','e',' ','f','a','m','i','l','y'};
    System.out.print(replaceSpaces(str));
  }
}
