package gowtham.design.patterns;

import gowtham.design.patterns.LoginInterface;

public class Google implements LoginInterface{
	Google(){
		//to be initialised
		System.out.println("Google Connected");
	}
	public void askLogin(){
		System.out.println("Google Login asked");
	}
}
