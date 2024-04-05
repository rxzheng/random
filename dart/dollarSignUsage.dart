void main() {
  var name = printName();
  print(name.$2); //gets the second parameter
}

(int, String, bool, int) printName() {
  return (12, "Richard", false, 13);
}
