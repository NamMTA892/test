<?php
if(isset($_GET['source'])){
    highlight_file(__FILE__);
    die();
}
if (isset($_POST["password"])) {
    try {
        include "./db.php";
        $sql = "SELECT * FROM users WHERE username = 'admin' AND password = '" . md5($_POST["password"], true) . "'";
        $db_result = $database->query($sql);
        if ($db_result->num_rows > 0) {
            $row = $db_result->fetch_assoc();
            $message = "Wow you can log in as admin, here is your flag nemnem";
        } else {
            $message = "Loserrrrr!!!!";
        }
    } catch (mysqli_sql_exception $e) {
        $message = $e->getMessage();
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Admin password</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <div class="container">
        <h1>I think you can't guess the password of admin</h1>
        <form class="form-login" method="post">
            <div>
                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="password" required>
                <button type="submit">Login</button>
                <br>
                <span class="message">
                    <?php if (isset($message)) echo $message; ?>
                </span>
            </div>
        </form>
    </div>
<!--/?source-->
</body>

</html>