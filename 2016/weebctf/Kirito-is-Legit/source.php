<!DOCTYPE html>
<html>
  <head>
    <title>Is Kirito Legit?</title>
  </head>
  <body>
    <center>
      <img src="kirito.jpg" />
      <form method="POST">
        Kirito is
        <select name="legit">
            <option value="not-legit">not</option>
        </select>
        legit.
      </form>
    </center>
    <script> /* source at /source.php */</script>
<?php
include("flag.php"); // import $flag
if (isset($_POST["legit"]) && $_POST["legit"] === "is-legit") {
  echo "<script>/* flag is $flag */</script>"
}
?>
  </body>
</html>
