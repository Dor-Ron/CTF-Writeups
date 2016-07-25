# Kirito Legit - 40, Solution
---

We navigate to **/source.php** to see what happens when we send a POST request using the form. We see that the *if-statement* within the PHP code checks for 2 conditions.

`if (isset($_POST["legit"]) && $_POST["legit"] === "is-legit")`

If the **select** element has a value set and that **option** tag value equals **is-legit.**

If those conditions hold true, then the response will be a commented out js string equivalent of the flag.

So, we open up the inspector change the value of the **value** attribute within the **select** tag from **not-legit** to **is-legit** and submit the form.

We check the network panel of the inspector tools for the HTTP response to our POST request and there we see the commented out flag.

Flag: **weeb{kirito_is\_most_/definitely/_legit}**
