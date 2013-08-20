object MyHomework3 {
var input = ""
  var str = ""
  var pos = 0
  
  def charsRemaining():Boolean = {
   if(pos<str.length()-1) {
     false
   } else {true}
  }
  
  def advance():Unit={
    pos+=1;
  }
  
  def peek(): Char = {
	if(pos+1==str.length()) {
	  '$'
	} else {
	  str.charAt(pos)
	} 
  }
  
  def main(args: Array[String]): Unit = {
  
    print("pattern? > ")
    val str = readLine
    val patternParsed = new Pat(0, str+"$")
    val pattern = patternParsed.parseS();
    print("string? > ")
    
    MyHomework3.str=readLine
    MyHomework3.str+="$"
    while(MyHomework3.str!="quit") {
      if (pattern.eval() && (MyHomework3.charsRemaining))
    	  print("\t  MATCH\n") 
      else print("\t  NO MATCH\n")
    
      print("\nstring? > ")
      MyHomework3.pos=0
      MyHomework3.str=readLine
      MyHomework3.str+="$"
    }
  }
}