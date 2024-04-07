void main() {
  //polymorphism
  Animal cat = Cat();
  cat.sound(); // polymorphism ://// basically what it is is that it allows objects to be reassignment
  cat = Dog(); // this does it through inheritance
  cat.sound();
  //abstraction
  Animal anim = Cat();
  anim.sound(); // abstract class cannot be instantiated
  Animal anim2 = Dog();
  anim2.sound();
}

class Person {
  String _name = 'hi'; //encapsulation uses private functions or variables
  void _getName() {
    print("what is the name");
    print(_name);
  }
}

abstract class Animal {
  void sound();
}

class Cat extends Animal {
  //inheritance
  @override
  void sound() {
    print('Cat making a sound');
  }
}

class Dog extends Animal {
  @override
  void sound() {
    print('Dog making a sound');
  }
}
