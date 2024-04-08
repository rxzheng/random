void main() {
  final employee1 = Employee('rxzheng', 'SWE');
  final employee2 = Employee('rivvan', 'Finance');
  final employee3 = Employee('whattheflip', 'heaheah');

  employee1.check();
  employee2.check();
  employee3.check();
}

enum EmployeeType {
  swe(20),
  finance(10), //enhanced enums
  marketing(1);

  final int salary;
  const EmployeeType(this.salary);
}

class Employee {
  final String name;
  final String type;
  Employee(this.name, this.type);

  void check() {
    switch (type) {
      case 'SWE':
        print('software eng');
      case 'Finance':
        print('ur in finance budo');
      default:
        print('u be trolling :skull:');
    }
    print(type.salary);
  }
}
