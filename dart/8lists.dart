void main() {
  List list = [1, 2, 3];
  //print(list[2]);

  List<int> marks = [10, 20, 30]; //says the stuff inside has to be ints
  //print(marks[2]);

  List<Student> stuffs = [
    Student('stiern'),
    Student('whatthesus'),
    Student('aoirestn'),
    Student('aoirettn'),
  ];
  final student = stuffs[1];
  print(student.name);

  stuffs.insert(0, Student('New Kid'));

  //if (student is Student) {
  //print(student.name);
  //} else {
  // print(student);
  //}
}

class Student {
  final String name;
  Student(this.name);

  @override
  String toString() => 'Student: $name';
}
