var SESSION_KEY = 'quiz' ;

var sessionData = sessionStorage.getItem(SESSION_KEY) ;
var timerObj    = document.getElementById('quiz-timer') ;

if(!sessionStorage.getItem('quiz-timer') && timerObj != null){
    var qstn_time   = parseInt(document.getElementById('max-time').value);
    var CONFIRM     = confirm(`Click OK to start quiz.\nQuiz will end in ${qstn_time} minutes`) ;
    
    if(!CONFIRM){
        history.back() ;
    } else {
        t = (qstn_time + 1) * 60 ;
        sessionStorage.setItem('quiz-timer', t) ;
    }
}

if(sessionData){
    try{
        var q   = document.getElementById('qstn-no').value ;
        var ans = JSON.parse(sessionData) ;
        
        document.getElementById(`opt${ans[q]}`).setAttribute('checked', true) ;
    }catch(e){
        console.log(e);
    }
}


formateTime = v => v.toString().length == 1 ? `0${v}` : v

displayTime = (minutes, seconds) => {
    let m = formateTime(minutes) ;
    let s = formateTime(seconds) ;
    document.getElementById('quiz-timer').innerHTML = `${m} : ${s}` ;
}




getSavedTime = () => {
    let time    = sessionStorage.getItem('quiz-timer') ; parseInt() ;
    if(!time){
        return false ;
    }

    time = parseInt(time) ;

    let minutes = Math.floor(time / 60),
    seconds     = time - minutes * 60; 

    if(minutes <= 0 || isNaN(time)){
        clearInterval(TIMER) ;
        minutes = seconds = 0 ;
        $(".outer-cont").show() ;
    }

    displayTime(minutes, seconds) ;

    return time ;
}

getSavedTime() ;

var TIMER =  setInterval(() => {
    let time = getSavedTime() ;
    
    if(time > 0){
        time-- ;
        sessionStorage.setItem('quiz-timer', time) ;
    }
}, 1000) ;


previousQuestion = (id) => {
    id -- ;
    location.href = `${id}` ;
}

nextQuestion = (id) => {
id ++ ;
    location.href = `${id}` ;
}


chooseOption = (qstnNo, opt) => {
    let data    = sessionStorage.getItem(SESSION_KEY) ;

    if(data){
        answers = JSON.parse(data) ;
    } else {
        answers = {} ;
    }
    answers[qstnNo] = opt ;
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(answers)) ;

}



finishQuiz = () => {
    let conform = confirm("Are you sure you want to finish the quiz") ;
    if(conform){
        let quiz = sessionStorage.getItem(SESSION_KEY) ;
        clearInterval(TIMER) ;
        sessionStorage.clear() ;

        let cat_id = document.getElementById('cat_id').value.trim() ;

        if(!cat_id){
            alert("Category not found") ;
            return false ;
        }

        $.ajax({
            url : "/quiz/save",
            type : 'POST',
            data : { 
                cat_id,
                quiz : quiz
             },
            success: (response) => {
                if(response.status){
                    console.log(response);
                    alert(response.msg) ;
                    location.href = response.loc ;
                    // location.reload() ;
                } else {
                    if(response.msg == 'login'){
                        location.reload() ;
                     }  
                }
            },
            error : () => {
                alert("Can't save results") ;
            }
        }) ;

    }
}