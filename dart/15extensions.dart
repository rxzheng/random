void main() {
  String motivation = 'this is a good quote';
  motivation = motivation.capitaliseFirstLetter();
}

extension CapitaliseFirstLetter on String {
  String capitaliseFirstLetter() {
    return this[0].toUpperCase() + this.substring(1);
  }
}
