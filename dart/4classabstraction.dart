void main() {
  final car = Car();
}

abstract class Vehicle {
  void accelerate();
  int noOfWheels = 10;
}

class Car implements Vehicle {
  @override
  void accelerating() {
    print('accelerating');
  }
}
