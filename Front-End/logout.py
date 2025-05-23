
<!DOCTYPE html>
<html>
  <head>

    <style>
        .logout {
  width: 1440px;
  height: 1024px;
  background-color: #ffffff;
}

.logout .overlap-group {
  position: relative;
  height: 1024px;
}

.logout .frame {
  position: absolute;
  width: 1440px;
  height: 1024px;
  top: 0;
  left: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 44, 105, 1) 0%,
    rgba(15, 82, 186, 1) 95%
  );
}

.logout .text-wrapper {
  position: absolute;
  width: 817px;
  top: 470px;
  left: 311px;
  font-family: "DM Sans-Bold", Helvetica;
  font-weight: 700;
  color: #ffffff;
  font-size: 60px;
  letter-spacing: 0;
  line-height: normal;
}

.logout .psychiatrist-for {
  position: absolute;
  width: 1440px;
  height: 1024px;
  top: 0;
  left: 0;
  object-fit: cover;
}

.logout .div {
  position: absolute;
  width: 771px;
  top: 571px;
  left: 334px;
  font-family: "DM Sans-Regular", Helvetica;
  font-weight: 400;
  color: #ffffff;
  font-size: 40px;
  text-align: center;
  letter-spacing: 0;
  line-height: 50px;
}

.logout .text-wrapper-2 {
  position: absolute;
  top: 38px;
  left: 1173px;
  font-family: "DM Sans-Bold", Helvetica;
  font-weight: 700;
  color: #ffffff;
  font-size: 25px;
  letter-spacing: 0;
  line-height: normal;
}

.logout .text-wrapper-3 {
  position: absolute;
  top: 38px;
  left: 1281px;
  font-family: "DM Sans-Bold", Helvetica;
  font-weight: 700;
  color: #ffffff;
  font-size: 25px;
  letter-spacing: 0;
  line-height: normal;
}

    </style>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="globals.css" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="logout">
      <div class="overlap-group">
        <div class="frame">
          <div class="overlap-group">
            <p class="text-wrapper">You have been logged out</p>
            <img class="psychiatrist-for" src="img/child.png" />
          </div>
        </div>
        <div class="div">Thank you!</div>
        <div class="text-wrapper-2">Log In</div>
        <div class="text-wrapper-3">Sign Up</div>
      </div>
    </div>
  </body>
</html>
