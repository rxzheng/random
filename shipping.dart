void main() {
  String location = 'XYZ';
  int cost;
  switch (location) {
    case 'XYZ':
      cost = 5;
      print(cost);
    case 'ABC':
      cost = 7;
      print(cost);
    case 'PQR':
      cost = 10;
      print(cost);
    default:
      print('what the flip');
  }
}
