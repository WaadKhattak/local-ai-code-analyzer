const express = require('express');
const app = express();

app.get('/user', (req, res) => {
    // Hardcoded credentials and dangerous dynamic eval
    const secretKey = "SUPER_SECRET_KEY_12345";
    eval(req.query.user_code);
});
