void main() {
  final anim = Animal();
  anim.fn();
}

mixin Jump {
  //mixin basically does not make the parent child relationship that inheritance has
  int jumping = 10;
}
mixin Scream {
  String scream = 'AAAAAHHHH';
}

class Animal with Jump, Scream {
  void fn() {
    print(jumping);
  }
}
