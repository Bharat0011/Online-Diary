
function validateForm()
{
    var returnval = true;
    var jname = document.getElementById('username').value;
    console.log(jname);
    if(jname.length<4)
    {

        document.getElementById('tp').innerHTML = "Username Cannot be less than 4 characters "
        document.getElementById('tp').style.visibility = "visible";
        // document.getElementsByClassName('form-control')[1].style.visibility = "visible";
        returnval = false;
    }
    if(jname.length==0)
    {

        document.getElementById('tp').innerHTML = "Username cannot be blank "
        document.getElementById('tp').style.visibility = "visible";
        returnval = false;
    }

    var jemail = document.getElementById('email').value;
    if(jemail.length>50)
    {
        document.getElementById('mail').innerHTML = " Invalid Email ID";
        document.getElementById('mail').style.visibility = "visible";
        returnval = false;
    }
    if(jemail.length==0)
    {

        document.getElementById('mail').innerHTML = "Email cannot be blank "
        document.getElementById('mail').style.visibility = "visible";
        returnval = false;
    }

    var jphone = document.getElementById('phone').value;
    if(jphone.length!=10)
    {
        document.getElementById('phne').innerHTML = "Phone Number should be of 10 digits";
        document.getElementById('phne').style.visibility = "visible";
        returnval = false;
    }

    var jpass = document.getElementById('password').value;
    var jcpass = document.getElementById('cpassword').value;
    if(jpass!=jcpass)
    {
        document.getElementById('cpass').innerHTML = "Password Doesnt Match";
        document.getElementById('cpass').style.visibility = "visible";
        returnval = false;
    }
    return returnval;
}