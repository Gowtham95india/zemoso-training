package gowtham.design.patterns;

import gowtham.design.patterns.LoginInterface;

public class Facebook implements LoginInterface{
	Facebook(){
		//to be initialised
		System.out.println("Facebook Connected");
	}
	public void askLogin(){
		System.out.println("Facebook Login asked");
	}
}
