void main() async {
  countDown().listen((val) {
    print(val);
  }, onDone: () {
    print('done');
  });
  print('start'); //this thing starts first beacuse of async
}

Stream countDown() async* {
  for (int i = 5; i > 0; i--) {
    yield i;
    await Future.delayed(Duration(seconds: 1));
  }
}
