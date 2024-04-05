void main() {
  final stuff = printStuff();
  stuff();
  () {
    print('Yoo');
  }();
}

Function printStuff() {
  return () {
    print('Yoo');
  };
}
