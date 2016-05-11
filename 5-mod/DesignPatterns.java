package gowtham.design.patterns;

import gowtham.design.patterns.LoginInterface;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import gowtham.design.patterns.Facebook;
import gowtham.design.patterns.Google;
import gowtham.design.patterns.Twitter;
import gowtham.design.patterns.LoginFactory;


class DesignPatterns{

	public static void main(String[] args) throws IOException{
		
		int Social_nw_name;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the choice");
		System.out.println("1. Facebook\n2. Google\n3. Twitter");
		String input = br.readLine();
		Social_nw_name = Integer.parseInt(input);
		LoginFactory loginFactory = new LoginFactory();
		LoginInterface instanceLogin = loginFactory.Login(Social_nw_name);
		//Facebook instanceLogin =(Facebook) Login(Social_nw_name);
		if(instanceLogin!=null){
			instanceLogin.askLogin();
		}
	}
}
