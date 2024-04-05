//store instances of classes in variables
void main() {
  final cookie = Cookie('Hello', 29);
  print(cookie.shape);
  print(cookie.size);
}

class Cookie {
  String shape;
  double size;
  Cookie(this.shape, this.size) {
    print('Cookie constructor called');
    baking();
  }
  //vars

  //functions
  void baking() {
    print('baking has started');
  }

  bool isCooling() {
    return false;
  }
}
