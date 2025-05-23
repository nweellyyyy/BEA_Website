
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="globals.css" />
    <link rel="stylesheet" href="style.css" />

    <style>.help {
        position: relative;
        width: 1440px;
        height: 1024px;
        background-color: #ffffff;
      }
      
      .help .frame {
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
      
      .help .dashboard {
        position: absolute;
        width: 173px;
        height: 48px;
        top: 340px;
        left: 29px;
      }
      
      .help .text-wrapper {
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
      
      .help .dashboard-icon {
        position: absolute;
        width: 48px;
        height: 48px;
        top: 0;
        left: 0;
        object-fit: cover;
      }
      
      .help .library {
        position: absolute;
        width: 125px;
        height: 39px;
        top: 398px;
        left: 35px;
      }
      
      .help .library-icon {
        position: absolute;
        width: 39px;
        height: 39px;
        top: 0;
        left: 0;
        object-fit: cover;
      }
      
      .help .div {
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
      
      .help .div-2 {
        position: absolute;
        width: 101px;
        height: 43px;
        top: 456px;
        left: 33px;
      }
      
      .help .text-wrapper-2 {
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
      
      .help .img {
        position: absolute;
        width: 43px;
        height: 43px;
        top: 0;
        left: 0;
        object-fit: cover;
      }
      
      .help .overlap-group {
        position: absolute;
        width: 330px;
        height: 142px;
        top: 40px;
        left: -17px;
      }
      
      .help .colored {
        position: absolute;
        width: 111px;
        height: 111px;
        top: 0;
        left: 109px;
        object-fit: cover;
      }
      
      .help .text-wrapper-3 {
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
      
      .help .group {
        position: absolute;
        width: 145px;
        height: 42px;
        top: 1254px;
        left: 47px;
      }
      
      .help .text-wrapper-4 {
        left: 41px;
        font-size: 32px;
        position: absolute;
        top: 0;
        font-family: "DM Sans-Regular", Helvetica;
        font-weight: 400;
        color: #ffffff;
        text-align: center;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .untitled-design {
        position: absolute;
        width: 32px;
        height: 32px;
        top: -5053px;
        left: -22px;
        object-fit: cover;
      }
      
      .help .group-2 {
        position: absolute;
        width: 103px;
        height: 30px;
        top: 911px;
        left: 52px;
      }
      
      .help .text-wrapper-5 {
        left: 28px;
        font-size: 23px;
        position: absolute;
        top: 0;
        font-family: "DM Sans-Regular", Helvetica;
        font-weight: 400;
        color: #ffffff;
        text-align: center;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .untitled-design-2 {
        position: absolute;
        width: 21px;
        height: 21px;
        top: 4px;
        left: 0;
        object-fit: cover;
      }
      
      .help .about {
        position: absolute;
        width: 120px;
        height: 43px;
        top: 282px;
        left: 31px;
      }
      
      .help .text-wrapper-6 {
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
      
      .help .p {
        position: absolute;
        top: 53px;
        left: 365px;
        font-family: "Karla-ExtraBold", Helvetica;
        font-weight: 800;
        color: #000000;
        font-size: 40px;
        letter-spacing: 0;
        line-height: normal;
        white-space: nowrap;
      }
      
      .help .welcome-to-the-BEA {
        position: absolute;
        width: 1000px;
        top: 105px;
        left: 365px;
        font-family: "Karla-Medium", Helvetica;
        font-weight: 500;
        color: #000000;
        font-size: 20px;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .overlap {
        position: absolute;
        width: 425px;
        height: 341px;
        top: 194px;
        left: 414px;
        background-color: #d9d9d9;
        border-radius: 30px;
      }
      
      .help .how-do-i-create-an {
        position: absolute;
        width: 403px;
        top: 69px;
        left: 11px;
        font-family: "Karla-Medium", Helvetica;
        font-weight: 500;
        color: #000000;
        font-size: 15px;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .text-wrapper-7 {
        position: absolute;
        top: 29px;
        left: 10px;
        font-family: "Karla-ExtraBold", Helvetica;
        font-weight: 800;
        color: #000000;
        font-size: 24px;
        letter-spacing: 0;
        line-height: normal;
        white-space: nowrap;
      }
      
      .help .overlap-2 {
        position: absolute;
        width: 425px;
        height: 341px;
        top: 577px;
        left: 414px;
        background-color: #d9d9d9;
        border-radius: 30px;
      }
      
      .help .getting-started {
        position: absolute;
        width: 403px;
        top: 57px;
        left: 11px;
        font-family: "Karla-Medium", Helvetica;
        font-weight: 500;
        color: #000000;
        font-size: 15px;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .text-wrapper-8 {
        position: absolute;
        top: 18px;
        left: 95px;
        font-family: "Karla-ExtraBold", Helvetica;
        font-weight: 800;
        color: #000000;
        font-size: 24px;
        letter-spacing: 0;
        line-height: normal;
        white-space: nowrap;
      }
      
      .help .overlap-3 {
        position: absolute;
        width: 425px;
        height: 341px;
        top: 577px;
        left: 888px;
        background-color: #d9d9d9;
        border-radius: 30px;
      }
      
      .help .email-beacompanion {
        position: absolute;
        width: 342px;
        top: 71px;
        left: 19px;
        font-family: "Karla-Medium", Helvetica;
        font-weight: 500;
        color: #000000;
        font-size: 15px;
        letter-spacing: 0;
        line-height: normal;
      }
      
      .help .text-wrapper-9 {
        position: absolute;
        top: 24px;
        left: 113px;
        font-family: "Karla-ExtraBold", Helvetica;
        font-weight: 800;
        color: #000000;
        font-size: 24px;
        letter-spacing: 0;
        line-height: normal;
        white-space: nowrap;
      }
      
      .help .overlap-4 {
        position: absolute;
        width: 425px;
        height: 341px;
        top: 194px;
        left: 888px;
        background-color: #d9d9d9;
        border-radius: 30px;
      }
      
      .help .text-wrapper-10 {
        position: absolute;
        top: 23px;
        left: 116px;
        font-family: "Karla-ExtraBold", Helvetica;
        font-weight: 800;
        color: #000000;
        font-size: 24px;
        letter-spacing: 0;
        line-height: normal;
        white-space: nowrap;
      }
      
      .help .website-not-loading {
        position: absolute;
        width: 403px;
        top: 63px;
        left: 10px;
        font-family: "Karla-Medium", Helvetica;
        font-weight: 500;
        color: #000000;
        font-size: 15px;
        letter-spacing: 0;
        line-height: normal;
      }
      </style>
  </head>
  <body>
    <div class="help">
      <div class="frame">
        <div class="dashboard">
          <div class="text-wrapper">Dashboard</div>
          <img class="dashboard-icon" src="img/dashboard-icon-1.png" />
        </div>
        <div class="library">
          <img class="library-icon" src="img/library-icon-1.png" />
          <div class="div">Library</div>
        </div>
        <div class="div-2">
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
      <p class="p">How can we help you?</p>
      <p class="welcome-to-the-BEA">
        Welcome to the BEA Help Center! If you have any questions or need assistance, you’re in the right place. Below,
        you&#39;ll find answers to common inquiries and guides to help you use BEA efficiently.
      </p>
      <div class="overlap">
        <p class="how-do-i-create-an">
          How do I create an account?<br />Click on the &#34;Sign Up&#34; button on the homepage and follow the
          instructions.<br /><br />What should I do if I forget my password?<br />Click &#34;Forgot Password?&#34; on
          the login page and follow the reset instructions.<br /><br />How do I update my profile information?<br />Go
          to &#34;Account Settings&#34; and select &#34;Edit Profile&#34; to make changes.<br /><br />How do I contact
          customer support?<br />See the &#34;Contact Support&#34; section below for details.
        </p>
        <div class="text-wrapper-7">Frequently Asked Questions (FAQ)</div>
      </div>
      <div class="overlap-2">
        <p class="getting-started">
          Getting Started<br />Power on BEA and ensure it is connected to a stable internet connection.<br /><br />Setting
          Up Your Profile<br />Log in to the BEA web application and complete your user profile.<br /><br />Using BEA
          for Behavioral Analysis<br />Place BEA in a well-lit room and let it monitor behavioral patterns.<br /><br />Viewing
          Reports &amp; Insights<br />Access real-time behavioral data through the BEA web dashboard.
        </p>
        <p class="text-wrapper-8">How to Use Our BEA</p>
      </div>
      <div class="overlap-3">
        <p class="email-beacompanion">
          Email: beacompanion.research@gmail.com<br /><br />Phone: 0969 084 8079<br /><br />Social Media: <br />Facebook
          - BeaCompanion PH
        </p>
        <div class="text-wrapper-9">Contact Support</div>
      </div>
      <div class="overlap-4">
        <div class="text-wrapper-10">Troubleshooting</div>
        <p class="website-not-loading">
          Website not loading?<br />Try clearing your cache and refreshing the page.<br /><br />Login issues?<br />Ensure
          your credentials are correct or reset your password.<br /><br />Payment failed?<br />Check your payment method
          or contact your bank for assistance.<br /><br />Feature not working?<br />Check our system status page or
          contact support for further help.
        </p>
      </div>
    </div>
  </body>
</html>
