saveQustion = () => {
    
    let ques = document.getElementById('question-name').value.trim(),
        desc = document.getElementById('question-desc').value.trim(),
        optA = document.getElementById('option-a').value.trim(),
        optB = document.getElementById('option-b').value.trim(),
        optC = document.getElementById('option-c').value.trim(),
        optD = document.getElementById('option-d').value.trim() ;
    
    let correct = document.getElementById('correct').value ;
    let cat = document.getElementById('category').value ;

    if(ques && optA && optB && optC && optD){
        if(!correct){
            alert("Please choose correct answer") ;
            return false ;
        }
    
        if(!cat){
            alert("Please choose category") ;
            return false ;
        }
        

        $.ajax({
            usl : "",
            type : 'POST',
            data : {
                ques, desc, optA, optB, optC, optD, correct, cat
            },
            success: (response) => {
                if(response.status){
                    console.log(response);
                    alert(response.msg) ;
                    location.reload() ;
                } else {
                    if(response.msg == 'login'){
                        location.reload() ;
                     }  
                }
            },
            error : () => {
                alert("Can't add questions") ;
            }
        }) ;

    }
}