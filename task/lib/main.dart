import 'package:flutter/material.dart';
import 'package:task/pages/registration_page.dart';

void main() => runApp(EventApp());

class EventApp extends StatelessWidget {
  const EventApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Event Registration",
      theme: ThemeData(primarySwatch: Colors.blue),
      home: RegistrationPage(),
    );
  }
}


