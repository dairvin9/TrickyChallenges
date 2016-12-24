// one class needs to have a main() method
public class removeDuplicates
{ 
  public static void removeDuplicates(char[] str) {
    if (str == null) return;
    int len = str.length;
    if (len < 2) return;
    
	// We dont have to touch str[o] bc its not a duplicate
	
    int nonDuplicate = 1;
    
    for (int i = 1; i < len; ++i) {
        int j;
        for (j = 0; j < nonDuplicate; ++j) {
            if (str[i] == str[j]) 
				break;
        }
        if (j == nonDuplicate) {
            str[nonDuplicate] = str[i];
            ++nonDuplicate;
        }
    }
    str[nonDuplicate] = 0; 
}
  
  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
    char[] str = {'p','i','z','z','a'};
    removeDuplicates(str);
    System.out.println(str);
  }
}