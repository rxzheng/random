void main() {
  Map<String, String> marks = {'Hey': '2', 'They': '5', 'what': '7'};
  print(marks['Hey']);

  //list of maps
  List<Map<String, int>> stuffs = [
    {'what': 25, 'cool': 5, 'now': 65},
    {'what': 45, 'cool': 56, 'now': 635},
    {'what': 245, 'cool': 35, 'now': 265}
  ];
  stuffs.map((e) {
    e.forEach((key, value) {
      print('$key : $value');
    });
  }).toList;
}
