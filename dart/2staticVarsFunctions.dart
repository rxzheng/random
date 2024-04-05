void main() {
  print(Constants.greeting);
  print(Constants.bye);
  print(Constants.giveMeSomeValue());
}

class Constants {
  Constants() {
    print('Constructor has been called');
  }
  static int height = 10;
  static String greeting = 'Hello, how are you';
  static String bye = 'Bye!';

  static int giveMeSomeValue() {
    return height;
  }
}
