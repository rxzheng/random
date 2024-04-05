//store instances of classes in variables
void main() {
  //camelCase
  print('${Cookie().size} cm'); //concaconation
  //anstatiated the class

  Cookie().baking();

  final isCookieCooling = Cookie().isCooling();
  print(isCookieCooling);

  final cookie = Cookie();
  cookie.shape =
      'rectangle'; // even tho its final its cookie.shape therefore its fine
  print(cookie.shape);
}

class Cookie {
  //vars
  String shape = 'Circle';
  double size = 15.2;
  //functions
  void baking() {
    print('baking has started');
  }

  bool isCooling() {
    return false;
  }
}
