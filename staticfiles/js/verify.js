document.getElementById("ver-form").addEventListener('submit', function(event){
    event.preventDefault()
    const isValid=verifyForm()
   if(isValid){
    alert("You can now log in with your new password")
    window.location.href= "login.html"
   }
   
})
function verifyForm(){
    let isValid=true
    const code=document.getElementById("code")
    if(!code.value.trim()){
        code.classList.add("invalid")
        code.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        code.classList.remove("invalid")
        code.nextElementSibling.style.display="none"
    }
    return isValid
}