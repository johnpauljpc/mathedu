errl = document.querySelectorAll(".error-outline")

errl.forEach(err => {
    err.addEventListener('keyup', ()=>{
        if(err){
            err.classList.remove("error-outline")
        }
    })
});
    

messages = document.querySelectorAll(".messages")

function msgHide(messages){
    if (messages){
        setInterval(() => {
         messages.style.display="none"
        }, 8000); //takes effect after 8seconds
         
     }
}

messages.forEach(msg => {
    msgHide(msg)
});

// console.log("wwwwwwwwwwwwwwwwwwwwwwwww")