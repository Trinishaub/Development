//
//  ViewController.swift
//  Calculator
//
//  Created by Shaun Gomes on 2015-11-02.
//  Copyright © 2015 GOMESY. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var display: UILabel!
   
    var userIsInTheMiddleOfTypingNumber: Bool = false
    
    @IBAction func appendDigit(sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleOfTypingNumber{
        print("Digit= \(digit)")
        display.text = display.text! + digit
        }
        else{
            display.text = digit
            userIsInTheMiddleOfTypingNumber = true
        }
        
    }


}

