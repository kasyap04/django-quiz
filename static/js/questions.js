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



editQuestion = (id) => {
    console.log(id);
    $(`.question-${id} input, .question-${id} textarea`).attr("readonly", false) ;
    $(`.saveBtn${id}`).show() ;
}

saveQuestion = id => {
    let optA = document.getElementById(`qstn-optA-${id}`) ,
        optB = document.getElementById(`qstn-optB-${id}`) ,
        optC = document.getElementById(`qstn-optC-${id}`) ,
        optD = document.getElementById(`qstn-optD-${id}`) ;

    let data = {
        qstn : document.getElementById(`qstn-name-${id}`).value.trim(),
        id   : document.getElementById(`qstnId${id}`).value,
        desc : document.getElementById(`qstn-desc-${id}`).value.trim(),
        option : JSON.stringify([
            {
                value   : optA.value.trim(),
                id      : optA.getAttribute("data-id")
            },
            {
                value   : optB.value.trim(),
                id      : optB.getAttribute("data-id")
            },
            {
                value   : optC.value.trim(),
                id      : optC.getAttribute("data-id")
            },
            {
                value   : optD.value.trim(),
                id      : optD.getAttribute("data-id")
            },
        ])
    }

    $.ajax({
        url : "/edit-question",
        type : 'POST',
        data : data,
        success: (response) => {
            if(response.status){
                console.log(response);
                // alert(response.msg) ;
                location.reload() ;
            } else {
                if(response.msg == 'login'){
                    location.reload() ;
                 }  
            }
        },
        error : () => {
            alert("Can't edit questions") ;
        }
    }) ;

    console.log(data);
}

approveQuestion = id => {
    $.ajax({
        url : "/approve-question",
        type : 'POST',
        data : { id },
        success: (response) => {
            if(response.status){
                console.log(response);
                // alert(response.msg) ;
                location.reload() ;
            } else {
                if(response.msg == 'login'){
                    location.reload() ;
                 }  
            }
        },
        error : () => {
            alert("Can't approve question") ;
        }
    }) ;
}

deleteQuestion = id => {
    $.ajax({
        url : "/delete-question",
        type : 'POST',
        data : { id },
        success: (response) => {
            if(response.status){
                console.log(response);
                // alert(response.msg) ;
                location.reload() ;
            } else {
                if(response.msg == 'login'){
                    location.reload() ;
                 }  
            }
        },
        error : () => {
            alert("Can't delete questions") ;
        }
    }) ;
}