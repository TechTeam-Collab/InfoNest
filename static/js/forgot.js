document.getElementById("for-form").addEventListener('submit', function(event){
    event.preventDefault()
    const isValid=forgotForm()
   if(isValid){
    alert("Check your email for the verification code")
    window.location.href= "verify.html"
   }
   
   
})
function forgotForm(){
    let isValid=true
    const email =document.getElementById("mail")
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRegex.test(email.value.trim(email))){
        email.classList.add("invalid")
        email.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        email.classList.remove('invalid')
        email.nextElementSibling.style.display="none"
    }

    return isValid

}