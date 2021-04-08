function restore(){
    const form = document.querySelectorAll("input[type='number']")
    form.forEach((input,index)=>{
        if(input.value){
            window.location.assign("/")
        }
    })
    
}