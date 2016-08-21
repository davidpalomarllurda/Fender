Feature: I want to buy a guitar
  
    Scenario: Buying a Stratocaster Hendrix Guitar
     Given we are on the main page
      when I choose guitar main model "Stratocaster"
       And I choose guitar submodel "Hendrix"
      then I will get to the billing page
       
  
	Scenario: Buying a Jazzmaster Lacquer Guitar
	 Given we are on the main page
	  when I choose guitar main model "Jazzmaster"
	   And I choose guitar submodel "Lacquer"
	  then I will get to the billing page
  	   

	Scenario: Buying a Jazzmaster Troy Van Leeuwen Guitar
	 Given we are on the main page
	  when I choose guitar main model "Jazzmaster"
	   And I choose guitar submodel "Troy Van Leeuwen"
	  then I will get to the billing page
	  
	Scenario: Buying a Jaguar Kurt Cobain Guitar
	 Given we are on the main page
	  when I choose guitar main model "Jaguar"
	   And I choose guitar submodel "Kurt Cobain"
	  then I will get to the billing page
	   
    Scenario: Buying a Telecaster Chris Shiflett
	 Given we are on the main page
	  when I choose guitar main model "Telecaster"
	   And I choose guitar submodel "Chris Shiflett"
	  then I will get to the billing page
  