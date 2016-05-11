package gowtham.design.patterns;

import gowtham.design.patterns.LoginInterface;

public class Twitter implements LoginInterface{
	Twitter(){
		//to be initialised
		System.out.println("Twitter Connected");
	}
	public void askLogin(){
		System.out.println("Twitter login asked");
	}
}