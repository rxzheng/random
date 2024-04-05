void main() {
  int someValue = 1;
  int age = 1;
  switch (someValue) {
    case 2:
      print("its 2");
    case 3:
      print("its 3");
    case 1:
      print("what the flips its 1");
    case 1 when age == 1:
      print('holy cow theyre both 1');

    default:
      print("what is going on");
  }
}
