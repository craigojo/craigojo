#! /bin/bash
# A very simple calculator
read -p "Please enter a number " a
        while [[ a -lt 0 ]]
                do 
                read -p "Enter a value (must be a positve value: "	
                echo "You entered $a"
        done
read -p "Please enter a second value" b
        while [[ b -lt 0 ]]
        echo [["Must be a positve value"]]
        done
        
echo "A= " $a
read -p "Please enter a number " b
echo "B= " $b
c=$((a*b))
echo "The sum of A x B = "$c


#! /bin/bash
# A very simple calculator
read -p "Please enter a number " a
echo "A= " $a
read -p "Please enter a number " b
echo "B= " $b
c=$((a*b))
echo "The sum of A x B = "$c