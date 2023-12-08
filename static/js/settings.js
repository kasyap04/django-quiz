saveSettings = () => {
    let max_questions = document.getElementById('max_questions').value.trim(),
    mark_per_questions = document.getElementById('mark_per_questions').value.trim(),
    time_per_questions = document.getElementById('time_per_questions').value.trim(),
    pass_percentage = document.getElementById('pass_percentage').value.trim() ;

    if(!max_questions || !mark_per_questions || !time_per_questions || !pass_percentage){
        alert("Please fill all fields") ;
        return false ;
    }


    $.ajax({
        url : "/settings",
        type : 'POST',
        data : { 
            max_questions,
            mark_per_questions,
            time_per_questions,
            pass_percentage
         },
        success: (response) => {
            if(response.status){
                console.log(response);
                location.reload() ;
            } else {
                if(response.msg == 'login'){
                    location.reload() ;
                 }  
            }
        },
        error : () => {
            alert("Can't save settings") ;
        }
    }) ;
}