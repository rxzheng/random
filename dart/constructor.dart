//store instances of classes in variables
void main() {
  final cookie = Cookie(shape: 'Hello', size: 29);
}

class Cookie {
  final String shape;
  final double size;
  Cookie({required this.shape, required this.size}) {
    baking();
  }
  //vars

  //method
  void baking() {
    print('baking has started');
  }

  bool isCooling() {
    return false;
  }
}
