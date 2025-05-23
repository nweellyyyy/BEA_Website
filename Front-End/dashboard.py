<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="globals.css" />
    <link rel="stylesheet" href="style.css" />

    <style>.desktop {
      position: relative;
      width: 1440px;
      height: 1024px;
      background-color: #ffffff;
    }
    
    .desktop .frame {
      position: absolute;
      width: 296px;
      height: 968px;
      top: 28px;
      left: 22px;
      border-radius: 25px;
      overflow: hidden;
      background: linear-gradient(
        180deg,
        rgba(0, 44, 105, 1) 0%,
        rgba(111, 75, 188, 1) 68%,
        rgba(75, 175, 252, 1) 98%
      );
    }
    
    .desktop .dashboard {
      position: absolute;
      width: 173px;
      height: 48px;
      top: 340px;
      left: 29px;
    }
    
    .desktop .text-wrapper {
      position: absolute;
      top: 11px;
      left: 54px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 23px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .dashboard-icon {
      position: absolute;
      width: 48px;
      height: 48px;
      top: 0;
      left: 0;
      object-fit: cover;
    }
    
    .desktop .library {
      position: absolute;
      width: 125px;
      height: 39px;
      top: 398px;
      left: 35px;
    }
    
    .desktop .library-icon {
      position: absolute;
      width: 39px;
      height: 39px;
      top: 0;
      left: 0;
      object-fit: cover;
    }
    
    .desktop .div {
      position: absolute;
      top: 9px;
      left: 48px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 23px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .help {
      position: absolute;
      width: 101px;
      height: 43px;
      top: 456px;
      left: 33px;
    }
    
    .desktop .text-wrapper-2 {
      position: absolute;
      top: 7px;
      left: 50px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 23px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .img {
      position: absolute;
      width: 43px;
      height: 43px;
      top: 0;
      left: 0;
      object-fit: cover;
    }
    
    .desktop .overlap-group {
      position: absolute;
      width: 330px;
      height: 142px;
      top: 40px;
      left: -17px;
    }
    
    .desktop .colored {
      position: absolute;
      width: 111px;
      height: 111px;
      top: 0;
      left: 109px;
      object-fit: cover;
    }
    
    .desktop .text-wrapper-3 {
      position: absolute;
      width: 330px;
      top: 100px;
      left: 0;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #ffffff;
      font-size: 30px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .group {
      position: absolute;
      width: 145px;
      height: 42px;
      top: 1254px;
      left: 47px;
    }
    
    .desktop .text-wrapper-4 {
      position: absolute;
      top: 0;
      left: 41px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 32px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .untitled-design {
      position: absolute;
      width: 32px;
      height: 32px;
      top: -23px;
      left: -22px;
      object-fit: cover;
    }
    
    .desktop .group-2 {
      position: absolute;
      width: 103px;
      height: 30px;
      top: 911px;
      left: 52px;
    }
    
    .desktop .text-wrapper-5 {
      position: absolute;
      top: 0;
      left: 28px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 23px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .untitled-design-2 {
      position: absolute;
      width: 21px;
      height: 21px;
      top: 4px;
      left: 0;
      object-fit: cover;
    }
    
    .desktop .about {
      position: absolute;
      width: 120px;
      height: 43px;
      top: 282px;
      left: 31px;
    }
    
    .desktop .text-wrapper-6 {
      position: absolute;
      top: 7px;
      left: 52px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #ffffff;
      font-size: 23px;
      text-align: center;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .observation-and-wrapper {
      position: absolute;
      width: 1044px;
      height: 35px;
      top: 607px;
      left: 358px;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0px 4px 4px #00000040;
      background: linear-gradient(
        90deg,
        rgba(0, 44, 105, 1) 0%,
        rgba(0, 87, 207, 1) 100%
      );
    }
    
    .desktop .observation-and {
      position: absolute;
      width: 257px;
      height: 21px;
      top: 9px;
      left: 393px;
    }
    
    .desktop .overlap {
      position: absolute;
      width: 1052px;
      height: 556px;
      top: 44px;
      left: 354px;
    }
    
    .desktop .frame-2 {
      position: absolute;
      width: 1052px;
      height: 494px;
      top: 62px;
      left: 0;
    }
    
    .desktop .hello-user {
      position: absolute;
      width: 207px;
      top: 0;
      left: 4px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 35px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .span {
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 35px;
      letter-spacing: 0;
    }
    
    .desktop .text-wrapper-7 {
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
    }
    
    .desktop .group-3 {
      position: absolute;
      width: 1044px;
      height: 342px;
      top: 654px;
      left: 358px;
    }
    
    .desktop .frame-3 {
      position: absolute;
      width: 508px;
      height: 263px;
      top: 0;
      left: 536px;
      background-color: #e9edf0;
      border-radius: 25px;
      overflow: hidden;
    }
    
    .desktop .text-wrapper-8 {
      position: absolute;
      top: 168px;
      left: 24px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .excessive {
      position: absolute;
      top: 88px;
      left: 24px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-9 {
      position: absolute;
      width: 347px;
      top: 27px;
      left: 24px;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 22px;
      letter-spacing: 0;
      line-height: normal;
      white-space: nowrap;
    }
    
    .desktop .text-wrapper-10 {
      position: absolute;
      top: 95px;
      left: 452px;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-11 {
      top: 168px;
      left: 452px;
      position: absolute;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .frame-4 {
      position: absolute;
      width: 508px;
      height: 263px;
      top: 0;
      left: 2px;
      background-color: #e9edf0;
      border-radius: 25px;
      overflow: hidden;
    }
    
    .desktop .text-wrapper-12 {
      position: absolute;
      top: 208px;
      left: 29px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-13 {
      position: absolute;
      top: 168px;
      left: 29px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-14 {
      position: absolute;
      top: 128px;
      left: 29px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-15 {
      position: absolute;
      top: 88px;
      left: 29px;
      font-family: "DM Sans-Regular", Helvetica;
      font-weight: 400;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-16 {
      top: 88px;
      left: 443px;
      position: absolute;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-17 {
      top: 128px;
      left: 447px;
      position: absolute;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-18 {
      top: 168px;
      left: 447px;
      position: absolute;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-19 {
      top: 208px;
      left: 447px;
      position: absolute;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 20px;
      letter-spacing: 0;
      line-height: normal;
    }
    
    .desktop .text-wrapper-20 {
      position: absolute;
      width: 347px;
      top: 27px;
      left: 29px;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 22px;
      letter-spacing: 0;
      line-height: normal;
      white-space: nowrap;
    }
    
    .desktop .div-wrapper {
      position: absolute;
      width: 1044px;
      height: 64px;
      top: 278px;
      left: 0;
      background-color: #e9edf0;
      border-radius: 25px;
      overflow: hidden;
    }
    
    .desktop .text-wrapper-21 {
      position: absolute;
      width: 347px;
      top: 15px;
      left: 22px;
      font-family: "DM Sans-Bold", Helvetica;
      font-weight: 700;
      color: #000000;
      font-size: 22px;
      letter-spacing: 0;
      line-height: normal;
      white-space: nowrap;
    }
    </style>
  </head>
  <body>
    <div class="desktop">
      <div class="frame">
        <div class="dashboard">
          <div class="text-wrapper">Dashboard</div>
          <img class="dashboard-icon" src="img/dashboard-icon-1.png" />
        </div>
        <div class="library">
          <img class="library-icon" src="img/library-icon-1.png" />
          <div class="div">Library</div>
        </div>
        <div class="help">
          <div class="text-wrapper-2">Help</div>
          <img class="img" src="img/help-icon-1.png" />
        </div>
        <div class="overlap-group">
          <img class="colored" src="img/colored-1.png" />
          <div class="text-wrapper-3">BEACompanion</div>
        </div>
        <div class="group">
          <div class="text-wrapper-4">Logout</div>
          <img class="untitled-design" src="img/image.png" />
        </div>
        <div class="group-2">
          <div class="text-wrapper-5">Logout</div>
          <img class="untitled-design-2" src="img/logout.png" />
        </div>
        <div class="about">
          <div class="text-wrapper-6">About</div>
          <img class="img" src="img/about-icon-1.png" />
        </div>
      </div>
      <div class="observation-and-wrapper"><img class="observation-and" src="img/observation.png" /></div>
      <div class="overlap">
        <img class="frame-2" src="img/Library (4)-1.png" style="border-radius: 15px; overflow: hidden;" />

        <p class="hello-user">
          <span class="span">Hello, </span>
          <span class="text-wrapper-7">User</span>
          <span class="span">!</span>
        </p>
      </div>
      <div class="group-3">
        <div class="frame-3">
          <div class="text-wrapper-8">Rapid or Excessive Talking</div>
          <div class="excessive">Excessive Interruptions During<br />Conversations</div>
          <div class="text-wrapper-9">Speech Patterns</div>
          <div class="text-wrapper-10">5</div>
          <div class="text-wrapper-11">3</div>
        </div>
        <div class="frame-4">
          <div class="text-wrapper-12">Eye gaze shifting</div>
          <div class="text-wrapper-13">Difficulty Waiting for Turns</div>
          <div class="text-wrapper-14">Leaving Seat Inappropriately</div>
          <div class="text-wrapper-15">Fidgeting</div>
          <div class="text-wrapper-16">10</div>
          <div class="text-wrapper-17">3</div>
          <div class="text-wrapper-18">8</div>
          <div class="text-wrapper-19">4</div>
          <div class="text-wrapper-20">Behavioral Patterns</div>
        </div>
        <div class="div-wrapper"><div class="text-wrapper-21">Remarks:</div></div>
      </div>
    </div>
  </body>
</html>
