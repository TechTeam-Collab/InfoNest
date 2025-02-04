document.getElementById("reset-form").addEventListener('submit', function(event){
    event.preventDefault()
    const isValid=verifyForm()
   if(isValid){
    alert("You can now login in with your new password 👌")
    window.location.href= "login.html" 
   }
   
})
function verifyForm(){
    let isValid=true
    const password=document.getElementById("password")
    if(!password.value.trim()){
        password.classList.add("invalid")
        password.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        password.classList.remove("invalid")
        password.nextElementSibling.style.display="none"
    }
    return isValid
}