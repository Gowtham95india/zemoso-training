package gowtham.design.patterns;

import gowtham.design.patterns.LoginInterface;

public class LoginFactory{
	
	public LoginFactory(){
		//empty constructor
	}
	
	public LoginInterface Login(int Social_nw_name){
		switch(Social_nw_name){
			case 1:
			return new Facebook();
			case 2:
			return new Google();
			case 3:
			return new Twitter();
			default:
			return null;
		}
	}
}
