void main() {
  String name = "globalvarisit?";
  printName(name);
}

printName(String name) {
  String name = 'localvar';
  print(name);
}
