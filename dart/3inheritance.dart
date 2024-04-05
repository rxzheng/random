//inheritance and implements

void main() {
  Car car = Car();
  print(car.speed);
}

class someClass {
  int speed = 15;
  void accelerate() {
    speed += 15;
  }
}

class Vehicle extends someClass {
  int speed = 10;
  bool isEngineWorking = false;
  bool isLightOn = true;
  @override
  void accelerate() {
    speed += 10;
  }
}

class Car extends Vehicle {
  int numberOfWheels = 4;
  void printSomething() {
    print(numberOfWheels);
  }
}

class Truck implements Vehicle {
  int speed = 15;
  bool isEngineWorking = true;
  bool isLightOn = true;
  void accelerate() {
    speed += 1;
  }
}
