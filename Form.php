<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Personalize Greetings Form</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
</head>
<body>
    <?php if (!empty($_POST["name"])) {
        echo "Greetings, {$_POST['name']}, and welcome.";
    }?>
    <form action ="<?php echo $_SERVER ['PHP_SELF']; ?>" method ="post">
    Enter your name: <input type = "text" name="name" />
    <input type= "submit"/>
    </form>
</body>
</html>