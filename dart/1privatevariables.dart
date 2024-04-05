void main() {
  final cookie = Cookie(shape: 'Hello', size: 29);

  print(cookie._height);
  cookie.setHeight = 15; //change the var (h) beacuse of setter
  print(h);
}

class Cookie {
  final String shape;
  final double size;
  Cookie({required this.shape, required this.size}) {
    baking();
  }
  //private vars are private to a single FILE
  int _height = 4;
  int _width = 5;

  int calculateSize() {
    return _height * _width;
  }

  //getters
  int get height => _height;
  //setters
  set setHeight(int h) {
    _height = h;
  }

  //method
  void baking() {
    print('baking has started');
  }

  bool isCooling() {
    return false;
  }
}
