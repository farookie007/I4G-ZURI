alert("SIMPLE CALCULATOR!!!");

let num1 = parseFloat(prompt("Enter your first Number: "));
let num2 = parseFloat(prompt("Enter your second Number: "));
let operator = prompt("Enter an operation:\n '+' - Add\n'-' - Subtract\n'/' - Divide\n'*' - Multiply");


function add(num1, num2) {
    alert((num1) + " + " + (num2) + " = " + (num1 + num2));
}
function minus(num1, num2) {
    alert((num1) + " - " + (num2) + " = " + (num1 - num2));
}
function divide(num1, num2) {
    alert((num1) + " / " + (num2) + " = " + (num1 / num2));
}
function multiply(num1, num2) {
    alert((num1) + " * " + (num2) + " = " + (num1 * num2));
}


function performOperation(num1, num2, operator) {
    if (operator == "+") {
        add(num1, num2);
    } else if (operator == "-") {
        minus(num1, num2);
    } else if (operator == "/") {
        divide(num1, num2);
    } else if (operator == "*") {
        multiply(num1, num2);
    } else {
        alert("Please enter a valid operator.");
    }
}

performOperation(num1, num2, operator);
