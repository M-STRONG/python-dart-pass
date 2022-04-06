abstract class Animal{

  void printName();

  void printSound();

}

class Dog extends Animal{

  @override

  void printName()

  {

    print('Dog');

  }

  

  @override

  void printSound()

  {

    print('hoho!');

  }

}

class Cat extends Animal{

  @override

  void printName()

  {

    print('Cat');

  }

  

  @override

  void printSound()

  {

    print('Meoo!');

  }

}

class Cow extends Animal{

  @override

  void printName()

  {

    print('Cow');

  }

  

  @override

  void printSound()

  {

    print('Moo!');

  }

}

void main() {

  Dog dog  = new Dog();

  dog.printName();

  dog.printSound();

  Cat cat  = new Cat();

  cat.printName();

  cat.printSound();

  Cow cow  = new Cow();

  cow.printName();

  cow.printSound();

}
