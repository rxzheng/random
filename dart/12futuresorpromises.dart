Future<void> main() async {
  print('Hi');
  longRequest().then((value) => print(value));
  print('Greetings');
}

Future longRequest() async {
  return Future.delayed(Duration(seconds: 2), () async {
    print('hiiii');
  });
}
