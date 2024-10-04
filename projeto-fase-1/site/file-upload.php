<?php
if ($_FILES['file']['error'] == 0) {
    move_uploaded_file($_FILES['file']['tmp_name'], $_FILES['file']['name']);
    echo "Upload realizado com sucesso!";
}
?>