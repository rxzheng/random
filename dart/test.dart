void main() {
  print('hellow rodl!');
  printName();
  print(returnAString());

  var (number, thing) = whatTheHellTwo();
  print(number);
  print(thing);
}

void printName() {
  print("what the flip is my name");
}

String returnAString() {
  return 'this is a string that is being returned';
}

(int, String) whatTheHellTwo() {
  return (3, 'what');
}
