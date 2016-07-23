"use strict";

/*
Slime Season 3 Brute Force
Used VPN and fake account as disguise
ABCTF 2016

Note, when correct answer is supplied, class green-background
replaces gray-background, to style container div, thats our queue
that the index is correct.
*/


// Targeting specific submit button
const $submit = $('#cliq')[0];
const $input = $('input[data-pid="f3c7a447ecfb75334aa14b57b889ac32"]')[0];
const $parentDiv = $('div[data-target="#f3c7a447ecfb75334aa14b57b889ac32"]');


//Brute force
for (var i=0; i<10000; i++) {
  if ($parentDiv.hasClass('green-background')) {
    console.log("The flag is: ABCTF{" + i + "}");
    break; // breaks at 7315
  } else {
    console.log(`${i} is not the solution`);
  }
  submitFn(i);
}


//Function to take care of submission
function submitFn(idx) {
  $input.value = "ABCTF{" + idx + "}";
  $submit.click();
}
