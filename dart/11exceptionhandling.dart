void main() {
  print(10 ~/ 3);
  try {
    print(10 ~/ 0);
  } on Exception catch (e) {
    print('what the flip $e');
  } catch (e) {
    print(e);
  } finally {
    print('finally done');
  }
  print('exception handled maybe');
}
