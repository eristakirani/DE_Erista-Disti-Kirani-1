Nama: Erista Disti Kirani 

Summary Object Oriented Programming 

Programming paradigm which provides a means of structuring programs

so that properties and behaviors are bundled into individuals objects. 

Properties determined by the value of its attributes. 

Behavior determined by how the object acts or reacts to request. 

OOP Fundamental concept 

- Encapsulation 
- Data Abtraction 
- Inheritance 
- Polymorphism 

Encapssulation thus concept involve bundling attributes and methods 

within a single unit, know as a class. it helps to protect attributes and methods

from outside interference, as it restricts direct access to them. 

`	`Basic Encapsulation Analogy: 

`	`- Class 

`	`- Attributes 

`	`- Method 

Encapsulation - Class 

what is class? class is a “template” / “blueprint” that is used to create objects. 

“special code” template in python to make object: 

- contains of: 

  attributes 

  methods 

- has an init method to initiate object 

How to define a class 

start with the class keyword to indicate taht you are creating a class, then yo add 

the name of the class (using CamelCase notation, starting with a Capital letter) 

Make an instance 

an istance is a unique copy of a class that representing an object. 

- All classes create instance, and all instances contain characteristic called attributes 
- Use the \_\_init\_\_() method to initialize (e.g., specify) an objects initial attributes by giving them their default value (or state) 

Attribute type 

- public (name)  can be accessed from inside and outside class. 
- protected (\_name) only accessible from inside class and its child, not from outside class. 
- private (\_\_name) only accessible from inside class only, not even its child. 

Data Abtaction 

Hiding background process from user 

data abstraction - encapsulation - information hiding 

main goal 

- Handle complexity by hiding unnecessary detail
- it should only reveal operation relevant other objects 

Data Abtarction - setter & getter 

setter & getter: 

Make complex calculation in 1 function/method 

- Hide All Unnescessary process in object calling itself 
- Make simple calling from object variable 
- Think of it as a small set of public methods which any other class can call without “knowing” how they work. 

Inheritance 

Obejct fact: 

- Object are often very similar. they share common logic. 
- But they’re not entirely the same. 

Inheritance - example 

pre save word SUPER 

[Super is used to] return a proxy object that delegates method calls to a parent or sibling class of type. 

Method Overriding 

Overriding is using parent method but modified the logic 

Polymorphism 

- Poly = Many, Morphism = form, Polymorphism = Ability objects of different types to respond to function of the same name. 
- User does not have to know the exact object in advance. 
- The behaviour of object can be imlementes at run time. 


